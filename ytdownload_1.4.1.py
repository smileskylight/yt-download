import os
import json
import time
import subprocess
import sys

def download():
    # 要檢查的套件列表
    required_packages = [
        "selenium",
        "undetected_chromedriver",
        # 添加其他套件的名稱
    ]

    missing_packages = []

    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)

    if missing_packages:
        print(f"缺少套件: {', '.join(missing_packages)}")
        req = input("是否下載套件 y/n : ")
        if req.lower() == "y":
            subprocess.call([sys.executable, "-m", "pip", "install"] + missing_packages)
        elif req.lower() == "n":
            print("拒絕下載即將關閉程式")
            time.sleep(3)
            sys.exit()

def sutch():
    print("\n-----=====  默認下載最高品質&最高畫質，並且會合併影片的縮圖  =====----- \n")
    print("說明: \n   cookies.txt:為下載影片所用 ,請以chrome控充功能\"Get cookies.txt LOAlly\" 取得\n   cookies1.txt:為抓取私人蒐藏夾所用,如需製作請輸入\"C\",並於40秒內登入帳號,等待系統生成後\n")
    print("指令: \n   yt:協助抓取播放列表的 URL,並下載影片 \n   dlp:請手動自行把影片加入video_urls.txt,直接開始下載影片 \n   c:抓取cookies1.txt \n")
    
    enter = input(" 請輸入指令 : ").lower()  # 確保輸入被轉換為小寫
    if enter == "c":
        createcookies1()
        sutch()
    elif enter == "yt":  # 正確匹配 "yt" 指令
        downloadYoutubeURL()
        ytdlp()
    elif enter == "dlp":  # 正確匹配 "dlp" 指令
        ytdlp()

def createcookies1():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    import undetected_chromedriver as uc
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import getpass

    # 設定你的 Google 帳號和密碼
    google_username = input("\n請輸入Google帳號: ")
    google_password = getpass.getpass("請輸入Google密碼: ")

    # 填寫webdriver的保存目錄
    chrome_driver_path = "supportexe/chromedriver.exe"
    service = Service(chrome_driver_path)
    options = uc.ChromeOptions()

    # 初始化瀏覽器
    driver = uc.Chrome(service=service, options=options)

    try:
        # 打開 Google 登入頁面
        driver.get('https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dzh-TW%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&ec=65620&hl=zh-TW&ifkv=Ab5oB3prG1ZlEi60whucMRvcVlTtUP8y1k0OQG7t6EJ62WRtLpMIPCPTVHgQAzOhVEDEhboXD-H-Ug&passive=true&service=youtube&uilel=3&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1460263717%3A1724399645395298&ddm=0')
        time.sleep(5)

        # 找到輸入帳號的欄位並填入帳號
        email_input = driver.find_element(By.ID, "identifierId")
        email_input.send_keys(google_username)
        time.sleep(5)
        email_input.click()
        time.sleep(1)
        next_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.LQeN7.BqKGqe.Jskylb.TrZEUc.lw1w4b'))
)
        driver.execute_script("arguments[0].click();", next_button)

        time.sleep(10)  # 等待下一頁載入

        # 找到輸入密碼的欄位並填入密碼
        password_input = driver.find_element(By.XPATH, "//input[@type='password']")
        password_input.send_keys(google_password)
        time.sleep(3)
        next_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.LQeN7.BqKGqe.Jskylb.TrZEUc.lw1w4b'))
)
        driver.execute_script("arguments[0].click();", next_button)
        time.sleep(8)  # 等待登入成功

        # 保存 cookies 為 json 格式
        with open('cookies/cookies1.txt', 'w') as f:
            f.write(json.dumps(driver.get_cookies()))


    finally:
        # 關閉瀏覽器
        try:
            driver.quit()
            print("抓取成功")
        except OSError as e:
            if e.winerror == 6:  # WinError 6 表示控制代碼無效
                print("抓取失敗")
                pass

def downloadYoutubeURL():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service

    # 讓使用者輸入目標網站的 URL
    playlist_url = input("請輸入 YouTube 播放列表的 URL: ")

    # 使用相對路徑指定 ChromeDriver 的路徑
    chrome_driver_path = "supportexe/chromedriver.exe"  # 使用相對路徑

    driver = webdriver.Chrome(service=Service(chrome_driver_path))

    # 讀取 cookies1.txt 文件
    cookie1file_path = "cookies/cookies1.txt"  # 使用相對路徑
    if os.path.exists(cookie1file_path):
        with open(cookie1file_path, 'r') as file:
            cookies = json.load(file)

        # 打開 YouTube 首頁並加載 cookies
        driver.get("https://youtube.com")
        time.sleep(5)  # 等待頁面加載完成

        for cookie in cookies:
            driver.add_cookie(cookie)

        # 重新加載頁面，以便應用 cookies
        driver.get(playlist_url)
    else:
        print("沒有偵測到 cookies.txt，可能無法提取\"私人/付費\"影片連結")
        driver.get(playlist_url)

    # 等待頁面加載完成
    time.sleep(5)

    # 找到所有影片的連結
    video_elements = driver.find_elements(By.XPATH, '//a[@id="video-title"]')

    # 提取連結並保存到列表
    video_urls = [element.get_attribute('href') for element in video_elements]

    # 清空 video_urls.txt 檔案
    with open("video_urls.txt", "w") as file:
        file.write("")  # 清空檔案

    # 將連結寫入 .txt 檔案
    with open("video_urls.txt", "w") as file:
        for url in video_urls:
            file.write(url + "\n")

    # 關閉瀏覽器
    driver.quit()


def ytdlp():
    # 讀取影片連結
    with open("video_urls.txt", "r") as file:
        video_urls = file.readlines()

    # 檢查 cookies.txt 文件是否存在
    cookiefile_path = "cookies.txt"  # 使用相對路徑
    if not os.path.exists(cookiefile_path):
        print("沒有偵測到 cookies.txt，可能無法下載會員/付費影片")

    # 設定下載選項
    ydl_opts = [
        'supportexe/yt-dlp.exe',   # 使用相對路徑
        '--format', 'bestvideo+bestaudio/best',
        '--merge-output-format', 'mp4',
        '--embed-thumbnail',  
        '--ffmpeg-location', 'supportexe/ffmpeg.exe'   # 使用相對路徑
    ]

    # 如果 cookies.txt 文件存在，則使用它
    if os.path.exists(cookiefile_path):
        ydl_opts += ['--cookies', cookiefile_path]
        print("找到cookies.txt")

    # 下載影片
    for url in video_urls:
        subprocess.run(ydl_opts + [url.strip()])

# 主程式
if __name__ == "__main__":
    download()  # 檢查並安裝缺少的套件
    sutch()


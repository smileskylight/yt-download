# 前言
此程式是依託於yt-dlp 與 selenium , 目的為大量快速抓取youtube影片,當然當然了你也可以選擇直接執行yt-dlp

## 先決條件
- Python >= 3.12
- 依附套件 selenium, undetected_chromedriver
- 調用檔 yt-dlp.exe, ffmpeg.exe, chromedriver.exe
- chrome 擴充功能 Get cookies.txt LOCKLLY

## 教學
### 下載
- 1.直接下載 .zip 檔並解壓縮
- 2.直接在CMD中存放目標位置執行
```bash
git clone https://github.com/smileskylight/yt-download.git
```
- 請勿動任何資料夾內.exe檔案位置,移動可能造成程式執行失敗
### 套件
- 請直接執行主程式,會自動偵測套件安裝情形,如缺少套件會詢問是否安裝補齊套件
- chromedriver.exe 需與所安裝的chrome版本相同,本站提供chromedriver 130 版,如不同請自行到下列網址下載
- https://googlechromelabs.github.io/chrome-for-testing/


### 使用
- 本程式暫不提供python argparse 請直接在CMD中執行檔案
```bash
python ytdownload_1.4.py
```
- 如果無安裝 python 可直接執行ytdownload_1.4.exe
### 指令
- yt:協助抓取播放列表的 URL,並下載影片
- dlp:請手動自行把影片加入video_urls.txt,直接開始下載影片
- c:抓取cookies1.txt
## cookies 製作
- #### 很重要 """"如果不需要cookies請刪除 cookies 資料夾內的文件"""" 
- cookie 請存放於 cookies 資料夾內
- cookies 的製作並非必要
- 因 selenium 與 yt-dlp 所調用 cookies 格式不同，製作的 cookies 區分為cookies.txt (yt-dlp使用)與cookies1.txt(selenium使用),但不下載會員/私人影片不需要cookies.txt,不抓取私人收藏夾的影片網址則不需要cookies1.txt,如cookies失效請重新抓取
### cookies.txt
- 使用chrome無痕分頁中使用擴充功能 Get cookies.txt LOCKLLY
```bash
https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc
```
- 下載後請於下面連結中設定開啟擴充功能可於無恆分頁開啟
```bash
chrome://extensions/
```
1.Get cookies.txt LOCKLLY 點選詳細資料  
2.開啟允許在無痕模式中執行
- 選擇 Netscape 模式,再點選 Export As 儲存,更改名字為 cookies.txt,儲存於 cookies 資料夾內
### coockies1.txt
開啟程式輸入 c ,直接在cmd上輸入google帳號與密碼,之後請耐心等待,程式會自行轉跳張貼抓取並生成檔案

#### 參考網址
https://github.com/yt-dlp/yt-dlp  
https://kkplay3c.net/chrome-incognito-window/  
https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc  
https://googlechromelabs.github.io/chrome-for-testing/  
https://www.ffmpeg.org/download.html  
https://home.gamer.com.tw/creationDetail.php?sn=5969214  
https://blog.maki0419.com/2022/01/youtube-download-ytdlp-ffmpeg.html 
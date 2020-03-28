import os
import urllib.request
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import ssl
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

ssl._create_default_https_context = ssl._create_unverified_context

#chrome driver 初始化
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:10046")
chrome_driver = "C://Users//liushuang//AppData//Local//Programs//Python//Python37//Scripts//chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)

region_url = "https://fabiaoqing.com/biaoqing/lists/page/165.html"
BASE_RES_DIR = 'k:' + os.sep + '表情包' + os.sep

def startLoadEmoij(url):
    print("load url:", url)
    driver.get(url)
    #time.sleep(1)
    print('open page...........')
    js="var q=document.documentElement.scrollTop=50000"  
    driver.execute_script(js)  
    print('scroll page...........')
    time.sleep(3)
    bsObj = BeautifulSoup(driver.page_source, "html.parser")
    imageList = bsObj.find_all("img")
    imageNum = 0
    for image in imageList:
        try:
            print("==============image=====================")
            print(image)
            imgSrc = image["src"]
            print(image["src"], image["title"], image["alt"])
            imageNum = imageNum + 1
            imgName = "1"
            if imgSrc.endswith(".jpg"):
                imgName = image["title"] + ".jpg"
            if imgSrc.endswith(".jpeg"):
                imgName = image["title"] + ".jpeg"
            if imgSrc.endswith(".png"):
                imgName = image["title"] + ".png"
            if imgSrc.endswith(".gif"):
                imgName = image["title"] + ".gif"
            imgName = imgName.replace(" ", "").replace("?", "").replace(",","").replace("，","").replace(":", "").replace("：", "").replace("*", "").replace("\n", "").replace("\t", "").replace("\\", "")
            if imgSrc.startswith("http"):
                urlretrieve(imgSrc, BASE_RES_DIR + imgName)
        except KeyError:
            print('key error')
        except OSError:
            print('os error')    
    print("共有图片：", imageNum)

#print("请输入表情包链接")
#url = input()
print("开始下载表情包")
for i in range(165, 200):
    region_url = region_url.replace(str(i), str(i + 1))
    print("下载第", i + 1, "次.......")
    startLoadEmoij(region_url)



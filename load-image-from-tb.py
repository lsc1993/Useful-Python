# 抓取1688详情页图片
import os
import urllib.request
from urllib.request import urlretrieve
import re
import ssl
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

ssl._create_default_https_context = ssl._create_unverified_context

BASE_RES_DIR = 'k:' + os.sep + '电商宝贝素材' + os.sep
reg = r'src="([^"]*jpg).*?<p><a href="([^"]*)" data-lazy-srcset="([^"]*jpg)"'
#url = 'https://detail.1688.com/offer/610637769380.html?spm=a26352.13672862.offerlist.8.a6817731hyX0U2&tracelog=p4p&clickid=d67b5901dd11438aa9d5bfb3d38735aa&sessionid=541c7dd125f02eb42026bbbe1296af85'

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:10046")
chrome_driver = "C://Users//liushuang//AppData//Local//Programs//Python//Python37//Scripts//chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)

def downImage(name_src, title):
    imgSaveDir = BASE_RES_DIR + title
    if (name_src.startswith("//")):
        name_src = "https:" + name_src
    if (name_src.endswith('.png') or name_src.endswith('.jpg') or name_src.endswith('.jpeg')):
        if name_src.find('.60x60') != -1:
            tmpname = name_src.replace('.60x60', '')
            print(tmpname)
            urlretrieve(tmpname, imgSaveDir + os.sep + tmpname[8:].replace('/', '-'))
        if name_src.find('.64x64') != -1:
            tmpname = name_src.replace('.64x64', '')
            print(tmpname)
            urlretrieve(tmpname, imgSaveDir + os.sep + tmpname[8:].replace('/', '-'))
        if name_src.find('.360x360') != -1:
            tmpname = name_src.replace('.360x360', '')
            print(tmpname)
            urlretrieve(tmpname, imgSaveDir + os.sep + tmpname[8:].replace('/', '-'))
        if name_src.find('.jpg_40x40') != -1:
            tmpname = name_src.replace('.jpg_40x40', '')
            print(tmpname)
            urlretrieve(tmpname, imgSaveDir + os.sep + tmpname[8:].replace('/', '-'))
        else:
            print(name_src)
            urlretrieve(name_src, imgSaveDir + os.sep + name_src[8:].replace('/', '-'))

def startLoad(url):
    driver.get(url)
    time.sleep(1)
    print('open page...........')
    js="var q=document.documentElement.scrollTop=50000"  
    driver.execute_script(js)  
    print('scroll page...........')
    time.sleep(3)
    bsObj = BeautifulSoup(driver.page_source, "html.parser")
    print('获取宝贝标题...........')
    #title_div = bsObj.find("div", {})
    title_text = bsObj.find("h1", {"data-spm":"1000983"})
    #print('标题是:' , title.get_text())
    title = title_text.get_text().replace('', '').replace('\t','').replace('\n','')
    print('标题是:' , title)
    imgSaveDir = BASE_RES_DIR + title
    os.makedirs(imgSaveDir, exist_ok = True)   
    imageList = bsObj.findAll("img")
    for name in imageList:
        try:
            name_src = name['src']
            downImage(name_src, title)
        except KeyError:
            print('KeyError:') 
    imageAList = bsObj.findAll("a")
    for name in imageAList:
        try:
            name_bg = name["style"]
            print(name_bg)
            startPos = name_bg.find("//")
            endPos1 = name_bg.find(".jpg")
            endPos2 = name_bg.find(".jpeg")
            endPos3 = name_bg.find(".png")
            endPos = 0
            if (endPos1 != -1):
                endPos = endPos1
            if (endPos2 != -1):
                endPos = endPos2
            if (endPos3 != -1):
                endPos = endPos3
            if (name_bg.startswith("//")):
                name_bg = "https:" + name_bg
            print('start pos:', startPos, 'end pos:', endPos)
            print(name_bg[startPos:endPos + 4])
            if startPos != -1 and endPos != -1:
                downImage(name_bg[startPos:endPos + 4], title)
        except KeyError:
            print('keyError')
    pList = bsObj.find("div", {"class": "content ke-post"})
    for child in pList.children:
        print("==============\n")
        print(child)
        print("==============\n")
        for cChild in child:
            try:
                print(cChild['src'])
                downImage(cChild['src'], title)
                downImage(cChild['data-ks-lazyload'], title)
            except Exception:
                print("")


print('请输入商品链接')
url = input()
startLoad(url)
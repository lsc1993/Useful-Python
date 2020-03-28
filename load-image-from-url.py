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

def loadPage(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'
    }
    req = urllib.request.Request(url=url, headers=headers)
    page = urllib.request.urlopen(req)
    return page

def loadHtml(url):
    page = loadPage(url)
    html = page.read()
    bsObj = BeautifulSoup(html, "html.parser")
    imageList = bsObj.findAll("img")
    for name in imageList:
        if name['src'].find('.60x60') != -1:
            print(name['src'].replace('.60x60', ''))
        print(name['src'])
    return html

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
    title_text = bsObj.find("h1", {"class":"d-title"})
    #print('标题是:' , title.get_text())
    title = title_text.get_text().replace('', '')
    print('标题是:' , title)
    imgSaveDir = BASE_RES_DIR + title
    os.makedirs(imgSaveDir, exist_ok = True)   
    imageList = bsObj.findAll("img")
    for name in imageList:
        try:
            if name['src'].startswith('http') and (name['src'].endswith('.png') or name['src'].endswith('.jpg') or name['src'].endswith('.jpeg')):
                if name['src'].find('.60x60') != -1:
                    tmpname = name['src'].replace('.60x60', '')
                    print(tmpname)
                    urlretrieve(tmpname, imgSaveDir + os.sep + tmpname[8:].replace('/', '-'))
                if name['src'].find('.32x32') != -1:
                    tmpname = name['src'].replace('.32x32', '')
                    print(tmpname)
                    urlretrieve(tmpname, imgSaveDir + os.sep + tmpname[8:].replace('/', '-'))
                if name['src'].find('.64x64') != -1:
                    tmpname = name['src'].replace('.64x64', '')
                    print(tmpname)
                    urlretrieve(tmpname, imgSaveDir + os.sep + tmpname[8:].replace('/', '-'))
                if name['src'].find('.360x360') != -1:
                    tmpname = name['src'].replace('.360x360', '')
                    print(tmpname)
                    urlretrieve(tmpname, imgSaveDir + os.sep + tmpname[8:].replace('/', '-'))
                else:
                    print(name['src'])
                    urlretrieve(name['src'], imgSaveDir + os.sep + name['src'][8:].replace('/', '-'))
        except KeyError:
            print('KeyError:') 

print('请输入商品链接')
url = input()
startLoad(url)

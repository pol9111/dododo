#!/usr/bin/python
# coding utf-8
import urllib.request
import re
#py抓取页面图片并保存到本地

#获取页面信息
page = urllib.request.urlopen('https://www.meitulu.com/item/2009.html').read()
page = page.decode()
#通过正则获取图片
def getImg(page):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,page)
    x = 0
    for imgurl in imglist:
        print(x)
        urllib.request.urlretrieve(imgurl,'E:\gobsen\%s.jpg'% x)
        x+=1

getImg(page)

#!/usr/bin/python
# coding utf-8
import re
import time
import urllib
import urllib.request


def getHtml():
    x = 0
    for i in range(2,10):
        url = 'http://www.youwu.cc/guonei/20151230/705_%s'% i
        page = urllib.request.urlopen(url)
        html = page.read()
        reg = 'src="(.+?\.jpg)"'
        imgre = re.compile(reg)
        imglist = re.findall(imgre, html.decode())
        print(imglist)

        for imgurl in imglist:
            urllib.request.urlretrieve(imgurl,'E:\gobsen%s.jpg' % x)
            x+=1

getHtml()



























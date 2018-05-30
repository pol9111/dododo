#!/usr/bin/python
# coding utf-8
import urllib.request
import re
#py抓取页面图片并保存到本地

#获取页面信息
def getHtml(url):
    html = urllib.request.urlopen(url).read()
    return html

#通过正则获取图片
def getImg(html):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
   # print(imglist)
    return imglist

html = getHtml("http://www.app111.com/doc/10112186.html")

list=getImg(html.decode('utf-8'))
print(list)
#循环把图片存到本地
x = 0
for imgurl in list:
    print(x)
    urllib.request.urlretrieve(imgurl,'E:\gobsen\%s.jpg'% x)
    x+=1

print("done")










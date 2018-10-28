import requests, re
from lxml import etree

url = 'http://www.quanben.co/files/article/html/0/49/930857.html'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

rs = requests.get(url=url, headers=headers).content
html = etree.HTML(rs.decode('gbk'))
result = html.xpath('//div[@class="novel_content"]/text()')

print(result)
# 正则去空格
# p = re.compile(r'\\xa0')
# r2 = p.sub(r' ', str(result))
# print(r2)

# split去空格
# r2 = "".join(result.split())
# count = re.findall(r'\\xa0', str(result))
# print(count)
with open('novel.txt', 'a+') as f:
    for each in result:
        # p = re.compile(r'\xa0')
        # change = p.sub(r'', each)
        # c3 = change
        # f.write(c3)
        r2 = "".join(each.split())
        r3 = r2 + '\n'
        f.write(r3)


# \xa0
# print result[0].text

# html = etree.parse('hello.html')
# result = html.xpath('//li[last()-1]/a')
# # result = html.xpath('//li[last()-1]/a/text()')
#
# # text 方法可以获取元素内容
# print result[0].text

# selector=etree.HTML(html)
# content=selector.xpath('//div[starts-with(@id,"a")]/text()') #这里使用starts-with方法提取div的id标签属性值开头为a的div标签
# for each in content:
    # print each
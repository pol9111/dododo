import urllib.request
import re

header = {
    'Cookie': 'UM_distinctid=163330979975c8-0093440c3ec9de-3961430f-100200-16333097998a81; PHPSESSID=8tvpdo3ufj5r1kqs1bhsj7jte5; CNZZDATA1273422572=579309142-1525567139-null%7C1529294663',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    'Referer': 'http://www.zimuzu.tv/resource/10407',
}

def gethtml(url):
    html = urllib.request.urlopen(url).read()
    return html

def geturl(html):
    reg = r'a href="(yyets://.*?)"'
    urllist = re.findall(reg, html)
    return urllist

html_rs = gethtml('http://zmz003.com/MtIyJ2')

list_url = geturl(html_rs.decode('utf-8'))
for each in list_url:
    print(each)






















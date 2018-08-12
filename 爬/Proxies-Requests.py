
import requests
import random

HEADERS = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
"Connect-Time": "0",
"Connection": "close",
"Cookie": "_gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
"Host": "httpbin.org",
"Referer": "https://github.com/luyishisi/Anti-Anti-Spider/tree/master/7.IP%E6%9B%B4%E6%8D%A2%E6%8A%80%E6%9C%AF",
"Total-Route-Time": "0",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
"Via": "1.1 vegur",
# "X-Forwarded-For": "45.177.173.115",
# "X-Forwarded-Port": "443",
"X-Forwarded-Proto": "https",
"X-Request-Id": "dd96776b-fd66-4d82-83bc-08d3a80799e4",
}

URL = 'https://httpbin.org/get?show_env=1'
URL1 = 'https://www.baidu.com/'



PROXIES = [
    {'https': 'https://122.245.134.173:3128'},
    {'https': 'https://203.201.170.2:8080'},
    {'http': 'http://180.122.146.112:22387'},
    {"https": "https://111.90.145.111:3128"},
    {"https": "https://103.112.129.86:8080"},
]

# proxies = {
#     "http": "http://" + ip + ':' + duankou,
#     "https": "http://" + ip + ':' + duankou,
# }

# 如果代理需要账户和密码，则需这样：
# proxies = {
#    "http": "http://user:pass@10.10.1.10:3128/",
# }

pool = random.choice(PROXIES)

resp = requests.get(URL, headers=HEADERS, proxies=pool)

rst = resp.text

print(rst)



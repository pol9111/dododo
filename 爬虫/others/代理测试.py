import random
import requests

URL = 'https://httpbin.org/get?show_env=1'
# URL = 'https://www.baidu.com/'

PROXIES = [
    {"https": "74.82.50.155:3128"},
    # {"https": "http://95.216.21.158:3128"},
    # {"https": "http://159.255.167.131:8080"},
]

proxie = {
  # "http": "http://12.34.56.79:9527",
  "https": "http://159.255.167.131:8080" # 或者不写
}


proxies = random.choice(PROXIES)
print(proxies)


# PROXY_POOL_URL = 'http://localhost:5555/random'
# PROXY_POOL_URL = 'http://47.75.52.39:5555/random'
# response = requests.get(PROXY_POOL_URL)
# proxies = {'https': response.text}
# print(proxies)

# resp = requests.get(URL, proxies=proxies)
resp = requests.get(URL, proxies=proxies)
print(resp.text)


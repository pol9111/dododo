
from concurrent.futures import ThreadPoolExecutor
import requests

def task(url):
    resp = requests.get(url)
    return resp

def parse(future, *args, **kwargs):
    resp = future.result()
    print(resp.status_code, resp.url, resp.text)

pool = ThreadPoolExecutor(32)

url_list = [
    'https://www.baidu.com/',
    'https://httpbin.org/get?show_env=1',
    'http://books.toscrape.com/index.html',
]

for i in url_list:
    rst = pool.submit(task, i)
    rst.add_done_callback(parse)
    # rst.add_done_callback(parse)

pool.shutdown(wait=True)




from concurrent.futures import ProcessPoolExecutor
import requests

def task(url):
    resp = requests.get(url)
    return resp

def parse(future, *args, **kwargs):
    resp = future.result()
    # print(resp.status_code, resp.url, resp.text)

pool = ProcessPoolExecutor(3)

url_list = [
    'https://www.baidu.com/',
    'https://httpbin.org/get?show_env=1',
    'http://books.toscrape.com/index.html',
]

for i in url_list:
    rst = pool.submit(task, i)
    # rst.add_done_callback(parse)
    # rst.add_done_callback(parse)

pool.shutdown(wait=True)




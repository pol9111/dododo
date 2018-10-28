from queue import Queue
from selenium import webdriver
from time import sleep, ctime
from concurrent.futures import ThreadPoolExecutor
from fake_useragent import UserAgent


def downloader(url):
    print('start:%s' % ctime())
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    sleep(2)
    print('succeed')
    driver.quit()


if __name__ == '__main__':
    threads = []
    url1 = "http://www.baidu.com"
    urls = [url1 for _ in range(8)]

    pool = ThreadPoolExecutor(32)

    pool.map(downloader, urls)
    print('end:%s' % ctime())
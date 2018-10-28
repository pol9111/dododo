from queue import Queue
from selenium import webdriver
from time import sleep, ctime
import threading


def downloader(url):
    print('start:%s' % ctime())
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    sleep(2)
    print('succeed')
    driver.quit()


if __name__ == '__main__':
    threads = []
    lock = threading.Lock()
    url1 = "http://www.baidu.com"
    num = 8

    urls = Queue(num)
    for _ in range(num):
        urls.put(url1)

    for _ in range(num):
        with lock:
            url = urls.get()
            t = threading.Thread(target=downloader, args=(url,))
            threads.append(t)

    for t in range(num):
        threads[t].start()
    for t in range(num):
        threads[t].join()
    print('end:%s' % ctime())
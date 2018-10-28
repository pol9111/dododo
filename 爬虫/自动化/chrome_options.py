from selenium import webdriver
from time import sleep, ctime
from concurrent.futures import ThreadPoolExecutor
from fake_useragent import UserAgent


def downloader(url):
    print('start:%s' % ctime())
    options = webdriver.ChromeOptions()
    # 不启动GUI
    # options.add_argument('--headless')


    # 设置编码格式
    options.add_argument('lang=zh_CN.UTF-8')


    # 个性化设置 0：禁止，1：询问，2：允许
    prefs = {
        'profile.default_content_setting_values': {
            # 'images': 2, # 禁止加载图片
            # 'javascript': 2, # 禁止加载js
            # 'adobe-flash-player': 2, # 禁止加载flash
            # 'media': 2, # 禁止加载视频(没用)
        }
    }
    options.add_experimental_option("prefs", prefs)


    # # 添加代理
    # proxy = proxy = eval(get_proxy())['https']
    # options.add_argument("--proxy-server={}".format(proxy))
    # # 静态IP：102.23.1.105：2005
    # # 阿布云动态IP：http://D37EPSERV96VT4W2:CERU56DAEB345HU90@proxy.abuyun.com:9020
    # PROXY = "proxy_host:proxy:port"
    # desired_capabilities = options.to_capabilities()
    # desired_capabilities['proxy'] = {
    #     "httpProxy": PROXY,
    #     "ftpProxy": PROXY,
    #     "sslProxy": PROXY,
    #     "noProxy": None,
    #     "proxyType": "MANUAL",
    #     "class": "org.openqa.selenium.Proxy",
    #     "autodetect": False
    # }


    # 设置UA
    # options.add_argument('user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"')
    # options.add_argument('user-agent={}'.format(UserAgent().safari))
    options.add_argument('user-agent={}'.format(UserAgent().random))


    # 添加插件
    # 插件下载: https://chrome-extension-downloader.com/1a7bd13c65e2890dd396cd65c079a7dd/Adblock-Plus.crx
    extension_path = '/extension/path'
    options.add_extension(extension_path)
    options.add_extension('AdBlock_v3.10.0.crx')


    # linux, docker需要添加
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')


    # 其他
    # 禁用js
    options.add_argument('-–disable-javascript') # 没用
    # 禁止加载所有插件
    options.add_argument('-–disable-plugins')
    # 自动播放视频
    options.add_argument('--autoplay-policy=no-user-gesture-required')


    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    sleep(20)
    print('succeed')
    driver.quit()


if __name__ == '__main__':
    threads = []
    # url1 = "http://www.baidu.com"
    url1 = "http://www.taobao.com"
    # url1 = "https://detail.tmall.com/item.htm?id=577415988218&ali_refid=a3_430583_1006:1106660572:N:%E6%97%A0%E4%BA%BA%E6%9C%BA:d27abd61b3b31b443f670d779485f0b3&ali_trackid=1_d27abd61b3b31b443f670d779485f0b3&spm=a230r.1.14.1"
    urls = [url1 for _ in range(1)]

    pool = ThreadPoolExecutor(32)

    pool.map(downloader, urls)
    print('end:%s' % ctime())




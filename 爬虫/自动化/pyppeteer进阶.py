import asyncio
from fake_useragent import UserAgent
from pyppeteer import launch


async def request_check(req):
    """请求过滤"""
    if req.resourceType in ['image', 'media', 'eventsource', 'websocket']:
        await req.abort()
    else:
        await req.continue_()


async def adownloader(url):
    CRX_PATH = '/path/to/crx/folder/'
    browser_options = {
        'headless': False, # 无界面模式
        'autoClose': False, # 自动关闭
        # 'user-agent': UserAgent().random,
        'args': [
            '--user-agent={}'.format(UserAgent().random), # 设置UA
            # '--proxy-server=http://127.0.0.1:8080', # 设置代理
            # '--no-sandbox',
            '--disable-extensions-except={}'.format(CRX_PATH),
            '--load-extension={}'.format(CRX_PATH),
                 ],
                       }

    browser = await launch(options=browser_options)
    page = await browser.newPage() # page_source
    await page.setRequestInterception(True)
    page.on('request', request_check)
    # await page.setUserAgent(UserAgent().random)
    await page.goto(url)
    print('succeed')
    # await page.screenshot({'path': 'example.png'})
    # content = await page.content()
    # cookies = await page.cookies()
    # await browser.close() # 默认自动关闭

loop = asyncio.get_event_loop()
# url1 = 'https://www.baidu.com/'
# url1 = 'https://www.taobao.com/'
# url1 = 'https://s.taobao.com/search?q=macbook&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306'
url1 = 'https://item.taobao.com/item.htm?spm=a230r.1.14.41.4485d644jkg4pN&id=555937880016&ns=1&abbucket=3#detail'
urls = [url1 for _ in range(1)]
tasks = [asyncio.ensure_future(adownloader(url)) for url in urls]
loop.run_until_complete(asyncio.gather(*tasks))

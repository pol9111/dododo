import asyncio
from fake_useragent import UserAgent
from pyppeteer import launch

async def adownloader(url):
    browser_options = {
        'headless': False,
        'autoClose': False,
        'no-sandbox': True,
        # 'user-agent': UserAgent().random,
                       }
    browser = await launch(options=browser_options)
    page = await browser.newPage() # page_source
    await page.setUserAgent(UserAgent().random)
    await page.goto(url)
    print('succeed')
    # await page.screenshot({'path': 'example.png'})
    content = await page.content()
    cookies = await page.cookies()
    # await browser.close() # 默认自动关闭

loop = asyncio.get_event_loop()
url1 = 'https://www.baidu.com/'
urls = [url1 for _ in range(1)]
tasks = [asyncio.ensure_future(adownloader(url)) for url in urls]
loop.run_until_complete(asyncio.gather(*tasks))

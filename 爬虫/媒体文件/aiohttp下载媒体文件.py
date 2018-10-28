
import asyncio
import aiohttp
import aiofiles


async def fetch(url, session):
    """异步下载器"""
    async with session.get(url, timeout=10) as resp:
        print('请求成功!!')
        f = await aiofiles.open(f'videos\qwe.ts', 'wb')
        await f.write(await resp.read())
        await f.close()


async def adownloader(urls):
    """运行器, 执行异步下载"""
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            print('正在请求: ', url)
            task = asyncio.ensure_future(fetch(url, session))
            tasks.append(task)
        return await asyncio.gather(*tasks)


url_list = []
loop = asyncio.get_event_loop()
tasks = [adownloader(url_list)]
loop.run_until_complete(asyncio.gather(*tasks))
loop.close()

import asyncio
from aiohttp import ClientSession
from two import *
import time

start_time = time.time()


# 下载器
async def fetch(sem, url, session):
    async with sem: # 限制最大操作
        async with session.get(url) as response: # 发送请求
            return await response.read() # 获取响应文件, 注意不是马上获取, 异步操作要加await
                                        # it just returns generator

async def run():
    """获取url列表"""
    url_list = []
    sem = asyncio.Semaphore(1024) # 设置最大操作
    # 创建可复用的 Session，减少开销
    async with ClientSession() as session: # 创建会话
        for each in range(0, 10000, 50):
            each_page_url = URL + '/f?kw={}&ie=utf-8&pn='.format(KW) + str(each)
            task = asyncio.ensure_future(fetch(sem, each_page_url, session)) # 每个预请求
            url_list.append(task)
        # 使用 gather(*tasks) 收集数据，wait(tasks) 不收集数据
        resp = await asyncio.gather(*url_list)
        print(resp)


# 实例化
loop = asyncio.get_event_loop()
# 待处理
future = asyncio.ensure_future(run())
# 启动
loop.run_until_complete(future)




end_time = time.time()
total_time = end_time - start_time
print(total_time)











import re
import aiofiles
import requests
import aiohttp
import asyncio
from fake_useragent import UserAgent
from tqdm import tqdm

URL = 'http://221.228.226.23/11/t/j/v/b/tjvbwspwhqdmgouolposcsfafpedmb/sh.yinyuetai.com/691201536EE4912BF7E4F1E2C67B8119.mp4'

HEADERS = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
'Cache-Control': 'no-cache',
'Host': '221.228.226.23',
'Pragma': 'no-cache',
'Proxy-Connection': 'keep-alive',
'Referer': 'http://221.228.226.23/11/t/j/v/b/tjvbwspwhqdmgouolposcsfafpedmb/sh.yinyuetai.com/691201536EE4912BF7E4F1E2C67B8119.mp4',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}


def to_range(file_size):
    # 获取视频总长度
    f = open('aio.mp4', 'wb')
    f.close()
    per_step = file_size // 25
    header_queue = []
    for i in range(0, file_size, per_step): # 切片
        start = i + 1 if not i is 0 else i
        end = i + per_step if start - 1 + per_step < file_size else file_size
        Range = 'bytes=%s-%s' % (start, end)
        header_queue.append(Range)
    return header_queue


async def fetch(chunk, session):
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'identity;q=1, *;q=0',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
        'Cache-Control': 'no-cache',
        'Host': '221.228.226.23',
        'Pragma': 'no-cache',
        'Proxy-Connection': 'keep-alive',
        'Range': chunk,
        'Referer': 'http://221.228.226.23/11/t/j/v/b/tjvbwspwhqdmgouolposcsfafpedmb/sh.yinyuetai.com/691201536EE4912BF7E4F1E2C67B8119.mp4',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }
    pos = int(re.findall('bytes=(.*?)-', chunk)[0])
    async with session.get(URL, headers=headers, timeout=10) as resp:
        print('请求成功!!')
        f = await aiofiles.open('aio.mp4', 'rb+')
        await f.seek(pos)
        await f.write(await resp.read())
        await f.close()


async def downloader(range_list, loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        tasks = [asyncio.ensure_future(fetch(chunk, session)) for chunk in range_list]
        await asyncio.gather(*tasks)


def run():
    print('开始下载视频')
    file_size = int(requests.get(URL, headers=HEADERS).headers['Content-Length'])
    l = to_range(file_size)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(downloader(l, loop))
    loop.close()


if __name__ == '__main__':
    run()
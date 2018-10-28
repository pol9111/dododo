import os
import requests
from fake_useragent import UserAgent
from tqdm import tqdm

url = 'http://221.228.226.23/11/t/j/v/b/tjvbwspwhqdmgouolposcsfafpedmb/sh.yinyuetai.com/691201536EE4912BF7E4F1E2C67B8119.mp4'

headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
'Cache-Control': 'no-cache',
'Host': '221.228.226.23',
'Pragma': 'no-cache',
'Proxy-Connection': 'keep-alive',
'Referer': 'http://221.228.226.23/11/t/j/v/b/tjvbwspwhqdmgouolposcsfafpedmb/sh.yinyuetai.com/691201536EE4912BF7E4F1E2C67B8119.mp4',
'Upgrade-Insecure-Requests': '1',
'User-Agent': UserAgent().random,
}

def download_media(url, dst):
    # 获取视频总长度
    file_size = int(requests.get(url, headers=headers).headers['Content-Length'])
    # 获取当前文件大小
    if os.path.exists(dst):
        first_byte = os.path.getsize(dst)
    else:
        first_byte = 0
    if first_byte >= file_size:
        return file_size
    # 构建请求头
    header = {"Range": "bytes=%s-%s" % (first_byte, file_size)}
    # 设置进度条 unit='B' 单位MB/s, desc进度条名
    pbar = tqdm(
        total=file_size, initial=first_byte,
        unit='B', unit_scale=True, desc=dst)

    resp = requests.get(url, headers=header, stream=True)
    with open(dst, 'ab') as f:
        for chunk in resp.iter_content(chunk_size=1024):
            f.write(chunk)
            pbar.update(1024)
    pbar.close()


download_media(url, 'frvc.mp4')

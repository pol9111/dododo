import requests

url = 'https://ip54177648.ahcdn.com/key=PkYUROS-HbZTFvf-IWTpWg,s=,end=1538346744,limit=2/data=1538346744/state=L0s0/referer=force,.avgle.com/reftag=56109644/media=hlsA/ssd3/177/3/110063493.mp4/seg-2-v1-a1.ts'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'referer': 'https://avgle.com/video/lAf5C5Czb5s/kbj-korean-bj-2018092108',
    'authority': 'ip54177648.ahcdn.com',
}

resp = requests.get(url, headers=headers, stream=True)

with open('qwe.ts', 'wb') as f:
    f.write(resp.content)

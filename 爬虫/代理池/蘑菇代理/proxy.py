from config import REDIS_CONN, PROIES, PROXY_URL
import requests
import random

def get_ips():
    html = requests.get(PROXY_URL).json()
    ips = html.get('msg')
    for dic in ips:
        ip = dic.get('ip')
        port = dic.get('port')
        ip_port = {'https': 'http://' + ip + ':' + port}
        REDIS_CONN.lpush(PROIES, ip_port)


def give_ips():
    proxy_list = REDIS_CONN.lrange(PROIES, 0, -1)
    # print(proxy_list)
    proxy = random.choice(proxy_list)
    return proxy


def update_proxy():
    REDIS_CONN.delete(PROIES)
    get_ips()
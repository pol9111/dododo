import redis
import requests
import random

REDIS_CLIENT = redis.StrictRedis(host='127.0.0.1', port=6379, db=6)
REDIS_DB_PROIES = 'proxies'
GET_PROXY_URL = 'http://piping.mogumiao.com/proxy/api/get_ip_bs?appKey=c9e9d5e5f95e439882c210fa895aa78a&count=30&expiryDate=0&format=1&newLine=2'

class Proxies:

    def __init__(self):
        self.redis_client = REDIS_CLIENT
        self.redis_db_proies = REDIS_DB_PROIES
        self.get_proxy_url = GET_PROXY_URL

    def get_ips(self):
        html = requests.get(self.get_proxy_url).json()
        ips = html.get('msg')

        ip_list = []
        for dic in ips:
            ip = dic.get('ip')
            port = dic.get('port')
            ip_port = {'https': ip + ':' + port}
            self.redis_client.sadd(ip_port)
            ip_list.append(ip_port)

        self.redis_client.lpush(self.redis_db_proies, ip_list)

    def give_ips(self):
        total = self.redis_client.llen(self.redis_db_proies)
        index = random.randint(0, total)
        ip = self.redis_client.lindex(self.redis_db_proies, index)

        return ip




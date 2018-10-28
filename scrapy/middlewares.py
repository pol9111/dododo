# -*- coding: utf-8 -*-
import random
import base64
from settings import USER_AGENTS
from settings import PROXIES


class RandomUserAgentMiddleware(object):

    def __init__(self, agents):
        self.agents = agents

    # 从settings构造，USER_AGENTS定义在settings.py中
    @classmethod
    def from_settings(cls, settings):
        return cls(settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        # 设置随机的User-Agent
        request.headers.setdefault('User-Agent', random.choice(self.agents))


class RandomProxyMiddleware(object):

    def __init__(self, proxies):
        self.proxies = proxies

    @classmethod
    def from_settings(cls, settings):
        return cls(settings.getlist('PROXIES'))

    def process_request(self, request, spider):
        if self.proxies['user_passwd'] is None:
            # 没有代理账户验证的代理使用方式
			proxy = random.choice(self.proxies)
			request.meta['proxy'] = proxy['ip_port']
			# request.meta['proxy'] = "http://" + self.proxies['ip_port']
        else:
            # 对账户密码进行base64编码转换
            base64_userpasswd = base64.b64encode(self.proxies['user_passwd'])
            # 对应到代理服务器的信令格式里
            request.headers['Proxy-Authorization'] = 'Basic ' + base64_userpasswd
            request.meta['proxy'] = "http://" + self.proxies['ip_port']
			




class RandomCookiesMiddleware(object):

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.cookies = cookies

    def _get_random_cookies(self):
        try:
            response = requests.get('http://127.0.01/weibo/random')
            if repsonse.status_code == 200:
                return json.loader(response.text)
        except ConnectionError:
            return None

    # 从crawler构造，USER_AGENTS定义在crawler的配置的设置中
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('COOKIES'))

    def process_request(self, request, spider):
        cookies = self._get_random_cookies()




    #
    # # 从crawler构造，USER_AGENTS定义在crawler的配置的设置中
    # @classmethod
    # def from_crawler(cls, crawler):
    #     return cls(crawler.settings.getlist('USER_AGENTS'))

















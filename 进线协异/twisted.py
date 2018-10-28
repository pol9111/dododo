from twisted.web.client import getPage, defer
from twisted.internet import reactor


def all_done(arg):
    reactor.stop() # 结束死循环


def callback(contents):
    print(contents.decode('utf-8'))


deferred_list = []

url_list = ['http://www.bing.com', 'http://www.baidu.com',]

for url in url_list:
    deferred = getPage(bytes(url, encoding='utf8')) # 发送请求
    deferred.addCallback(callback) # 回调函数
    deferred_list.append(deferred) # 收集结果

dlist = defer.DeferredList(deferred_list) # 延迟等待
dlist.addBoth(all_done)

reactor.run() # 死循环, 查看是否响应了





import gevent.monkey
import gevent
import requests
from datetime import datetime

gevent.monkey.patch_socket()

def fetch(pid):
   # response = requests.get('http://aljun.me')
   response = requests.get('http://www.baidu.com')
   result = response.text


   print('Process %s: %s' % (pid, datetime.now()))


def synchronous():
    for i in range(1,10):
        fetch(i)

def asynchronous():
    threads = []
    for i in range(1,1000):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)

print('Synchronous:')
# synchronous()

print('Asynchronous:')
asynchronous()



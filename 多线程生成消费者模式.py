import random
import queue
from threading import Thread, Lock

class Producer(Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            item = random.randint(0, 99)
            # lock.acquire()
            self.queue.put(item)
            # lock.release()
            print('生产者->已生产 %s, 并将其加入了队列' % item)

class Consumer(Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            # lock.acquire()
            item = self.queue.get()
            # lock.release()
            print('消费者: 从队里取出 %s' % item)
            self.queue.task_done()


if __name__ == '__main__':
    # lock = Lock()
    goods = queue.Queue(10)
    p1 = Producer(goods)
    c1 = Consumer(goods)
    c2 = Consumer(goods)
    p1.start()
    c1.start()
    c2.start()
    p1.join()
    c1.join()
    c2.join()





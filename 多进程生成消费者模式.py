import random
from multiprocessing import Process, Manager

class Producer(Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            item = random.randint(0, 99)
            self.queue.put(item)
            print('生产者->已生产 %s, 并将其加入了队列' % item)


class Consumer(Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            print('消费者: 从队里取出 %s' % item)

if __name__ == '__main__':
    goods = Manager().Queue(10)
    p1 = Producer(goods)
    c1 = Consumer(goods)
    p1.start()
    c1.start()
    p1.join()
    c1.join()




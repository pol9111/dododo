import time

import pika

# 连接
credentials = pika.PlainCredentials('bridi', 'qwe123')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost', credentials=credentials))
# 设置通道
channel = connection.channel()


# 在还没有生产者时可以先声明
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

# 设置消费参数
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
# 开始消费
channel.start_consuming()


#
# def callback(ch, method, properties, body):
#     print(" [x] Received %r" % body)
#     time.sleep(20)
#     print(" [x] Done")
#     print("method.delivery_tag", method.delivery_tag)
#     ch.basic_ack(delivery_tag=method.delivery_tag)
#
#
# channel.basic_consume(callback,
#                       queue='task_queue',
#                       no_ack=True
#                       )
#
# print(' [*] Waiting for messages. To exit press CTRL+C')
# channel.start_consuming()



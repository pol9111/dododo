# !/usr/bin/env python
import time

import pika

# 连接
credentials = pika.PlainCredentials('bridi', 'qwe123')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost', credentials=credentials))
# 设置通道
channel = connection.channel()

# 声明queue
channel.queue_declare(queue='hello')

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()




# # 声明queue
# channel.queue_declare(queue='task_queue')
#
# # n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
# import sys
#
# message = ' '.join(sys.argv[1:]) or "Hello World! %s" % time.time()
# channel.basic_publish(exchange='',
#                       routing_key='task_queue',
#                       body=message,
#                       properties=pika.BasicProperties(
#                           delivery_mode=2,  # 使消息持久化
#                       )
#                       )
# print(" [x] Sent %r" % message)
# connection.close()


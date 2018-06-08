import socket

sock_client = socket.socket() # 创建一个TCP套接字
sock_client.connect(('127.0.0.1', 8025)) # 连接远程服务器

while True:
    msg = input('>>>') # 当收到返回时输入发送信息
    sock_client.send(msg.encode()) # 不是byte会报错
    if msg == 'q':
        sock_client.close()
        break
    print(sock_client.recv(500), '返回成功！')


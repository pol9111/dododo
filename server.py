import socket

sock_server = socket.socket() # 创建一个TCP套接字
sock_server.bind(('127.0.0.1', 8025)) # 把套接字绑定到某一个端口上面
sock_server.listen(5) # 开始接听 等待客户端的请求 最大挂起数是5

while True:
    take = sock_server.accept() # 获取对等套接字 以及客户端的地址 可能会阻塞
    conn, addr = take
    while True:
        rs = conn.recv(1024) # 获取客户端发送的信息
        if rs.decode() == 'q':
            print('客户端{}已断开'.format(addr))
            break
        elif rs:
            print(rs.decode())
            conn.send(rs)
        else:
            break



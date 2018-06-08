import socket

sock_server = socket.socket() # 创建一个TCP套接字
sock_server.bind(('127.0.0.1', 8025)) # 把套接字绑定到某一个端口上面
sock_server.setblocking(False) # 服务器设置非阻塞
sock_server.listen(5) # 开始接听 等待客户端的请求 最大挂起数是5

print('开启监听')
client_list = []


while True:
    try:
        conn, addr= sock_server.accept() # 获取对等套接字 以及客户端的地址 可能会阻塞
    except BlockingIOError:
        pass
    else:
        print('客户端连{}接成功'.format(addr))
        conn.setblocking(False) # 连接设置非阻塞
        client_list.append(conn)
    try: # 无论如何都会执行这一步
        for client_socket in client_list:
            try:
                rs = client_socket.recv(1024) # 获取客户端发送的信息
            except BlockingIOError:
                pass
            else:
                if rs:
                    print(rs.decode(), client_socket)
                    client_socket.send(rs)
                else: # 正常断开
                    print('客户端{}已断开'.format(addr))
                    client_socket.close()
                    client_list.remove(client_socket)
    except: # 非正常断开执行这一步
        print('客户端{}已断开'.format(addr))
        client_socket.close()
        client_list.remove(client_socket)



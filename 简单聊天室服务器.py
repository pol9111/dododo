import selectors
import socket

server = socket.socket()
server.bind(('', 8050))
server.listen()

sel = selectors.DefaultSelector()
client_list = [] # 把房间里的人都放入这个列表

def accept(server):
    conn, addr = server.accept()
    client_list.append(conn)
    nick_name = conn.recv(1024)
    msg = 'Welcome {} to room!!!'.format(nick_name)
    print('当前人数:{}'.format(len(client_list)))
    for client in client_list: # 循环发送每个在房间的人欢迎信息
        client.send(msg.encode())
    sel.register(conn, selectors.EVENT_READ, read)
            # 套接字  可能发生的事情  回调函数

def read(conn):
    data = conn.recv(1024)
    if not data:
        conn.close()
        sel.unregister(conn)
        client_list.remove(conn)
    else:
        print('{}'.format(data.decode()))
        for client in client_list:
            if client is not conn: # 发送消息给,除了发消息的人外的房间里的所有人
                client.send(data)



sel.register(server, selectors.EVENT_READ, accept)
               #  套接字 发生了 调用哪个函数
# 套接字  可能发生的事情  回调函数
while True:
    events = sel.select() # 返回发生事件的列表
    for key,_ in events:
        callback = key.data # 某个套接字的函数
        sock = key.fileobj  # 在下面看参数
        callback(sock)  # 整个过程都封装在了每个event(sel.register)里面，
                       # 只要用event.key里面的函数去调用里面的对象

# [(SelectorKey(fileobj=<socket.socket fd=468, family=AddressFamily.AF_INET,
# type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8899),
#  raddr=('127.0.0.1', 57695)>, fd=468, events=1,
# data=<function read at 0x000001FFCC282E18>), 1)]

























import socket
import selectors

sel = selectors.DefaultSelector() # 实例化一个选择器

server = socket.socket()
server.bind(('', 8899))
server.listen()


def read(conn):
    try:
        data = conn.recv(1024)
        if data:
            print(data.decode())
            conn.send(b'%s' % data)
        else:
            sel.unregister(conn) # 取消监听
            conn.close()
    except:
        print('连接已断开', conn)
        sel.unregister(conn) # 取消监听
        conn.close()


def accept(server):
    conn, addr = server.accept()
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read) #上面的read函数
                #  套接字 发生了 调用哪个函数

sel.register(server, selectors.EVENT_READ, accept) #上面的accept函数
# 套接字  可能发生的事情  回调函数

while True:
    events = sel.select() # 返回发生事件的列表
    print(events)
    for key, _ in events:
        callback = key.data # 某个套接字的函数
        sock = key.fileobj # 在下面看参数
        callback(sock) # 整个过程都封装在了每个event(sel.register)里面，
                       # 只要用event.key里面的函数去调用里面的对象

# sel.select() 有两种情况
# 第一种 客户端请求连接  key.data 是 accept  key.fileobj 是  server
# 第二种 客户端发送了消息 key.data 是 read     key.fileobj 是 conn

# key.data  key.fileobj都在元祖的第一个值里面

# [(SelectorKey(fileobj=<socket.socket fd=468, family=AddressFamily.AF_INET,
# type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8899),
#  raddr=('127.0.0.1', 57695)>, fd=468, events=1,
# data=<function read at 0x000001FFCC282E18>), 1)]



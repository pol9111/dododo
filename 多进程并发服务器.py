import multiprocessing
import socket

server = socket.socket()
server.bind(('0.0.0.0', 8080))
server.listen(1000)

def worker(connection):
    while True:
        recv_data = connection.recv(1000) # 进程的逻辑
        if recv_data:
            print(recv_data.decode())
            connection.send(recv_data.encode())
        else:
            connection.close()
            break

while True: # 循环监听
    connection, remote_address = server.accept()
    # 每生成一个对等连接套接字,就生成一个进程并交由这个进程去服务
    process = multiprocessing.Process(target=worker, args=(connection,))
    process.start() # 启动进程

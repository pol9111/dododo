import threading, socket

server = socket.socket()
server.bind(('0.0.0.0', 8050))
server.listen(1000)

def worker(connection):
    while True:
        recv_data = connection.recv(1000)
        if recv_data:
            print(recv_data.decode())
        else:
            connection.close()
            break

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=worker, args=(conn,))
    thread.start()







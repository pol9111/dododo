import socket, threading

client = socket.socket()
client.connect(('127.0.0.1', 8050))


def read(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            print(data)
        except:
            break


t = threading.Thread(target=read, args=(client,), daemon=True)
t.start()

nick_name = input('input your nickname:')
client.send(nick_name.encode())

while True:
    msg = input('<<<')
    if msg == 'q':
        break
    client.send('{}:{}'.format(nick_name, msg).encode())

client.close()






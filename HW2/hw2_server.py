import socket
from tkinter.tix import Tree

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    client.send(b'Hello ' + addr[0].encode())
    msg = client.recv(1024)
    print(msg.decode())
    num = 20191512
    client.send(num.to_bytes(4, 'big'))
    client.close()
    
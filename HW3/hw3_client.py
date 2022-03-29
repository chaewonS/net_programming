from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    msg = input('Number to send:')
    if msg == 'q':
        break
    s. send(msg.encode())
    print('Recevied message:', s.recv(1024).decode())

s.close()

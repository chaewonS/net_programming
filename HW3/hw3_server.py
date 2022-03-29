from email import message
from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('waiting...')
while True:
    client, addr = s.accept()
    print('connection from ', addr)
    while True:
        data = client.recv(1024)
        if not data:
            break
        num1, op, num2 = data.decode().split() #공백 포함
        if op == '+':
            msg = int(num1)+int(num2)
        elif op == '-':
            msg = int(num1)-int(num2)
        elif op == '*':
            msg = int(num1)*int(num2)
        elif op == '/':
            msg = round((float(num1)/float(num2)),1)
        client.sendall(str(msg).encode())
    client.close()
        
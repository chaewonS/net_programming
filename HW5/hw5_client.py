import socket
import time

f = open("C:/Users/user/net_program/HW5/data.txt", "w")
sock_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr_1 = ('localhost', 9000)
sock_1.connect(addr_1)

sock_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr_2 = ('localhost', 9999)
sock_2.connect(addr_2)

while True:
    msg = input()
    if msg == '1':
        sock_1.send("Request".encode())
        data = sock_1.recv(1024).decode()
        f = open("C:/Users/user/net_program/HW5/data.txt", "a")
        f.write(f"{time.strftime('%c', time.localtime(time.time()))} Device1: {data}\n")
    elif msg == '2':
        sock_2.send("Request".encode())
        data = sock_2.recv(1024).decode()
        f = open("C:/Users/user/net_program/HW5/data.txt", "a")
        f.write(f"{time.strftime('%c', time.localtime(time.time()))}: Device2: {data}\n")
    elif msg == 'quit':
        sock_1.send("quit".encode())
        sock_2.send("quit".encode())
        break
    else: 
        print("Error")

sock_1.close()
sock_2.close()
f.close()
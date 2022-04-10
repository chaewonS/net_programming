from socket import *
import random
import time

port = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    #2
    sock.settimeout(None)
    while True:
        data, addr = sock.recvfrom(BUFF_SIZE)
        if random.random() <= 0.5:
            continue
        else:
            sock.sendto(b'ack', addr)
            print('<- ', data.decode())
            break

    #1
    msg = input('-> ')
    reTx = 0
    while reTx <= 3:
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), addr)
        sock.settimeout(2) #소켓의 timeout 설정

        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except timeout:
            reTx += 1
            continue
        else:
            break
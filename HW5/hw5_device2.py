from socket import *
import random

s = socket()
s.bind(('', 9999))
s.listen(10)
c, addr = s.accept()

while True:
    req_msg = c.recv(1024).decode()

    if req_msg == 'Request': 
        heart = random.randint(40, 140) 
        step = random.randint(2000, 6000) 
        calorie = random.randint(1000, 4000)
        text = f"Heartbeat={heart}, Steps={step}, Cal={calorie}"
        c.send(text.encode())
        
    elif req_msg == 'quit':
        c.close()
        break

    else:
        c.send(b'Error')
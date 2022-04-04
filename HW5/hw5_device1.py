from socket import *
import random

s = socket()
s.bind(('', 9000))
s.listen(10)
c, addr = s.accept()

while True:
    req_msg = c.recv(1024).decode()

    if req_msg == 'Request': 
        temp = random.randint(0, 40) 
        humid = random.randint(0, 100) 
        illum = random.randint(70, 150)
        text = f"Temp={temp}, Humid={humid}, lilum={illum}"
        c.send(text.encode())

    elif req_msg == 'quit':
        c.close()
        break

    else:
        c.send(b'Error')
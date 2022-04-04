from socket import *

BUFF_SIZE = 1024
port = 5555

s = socket(AF_INET, SOCK_DGRAM)
s.connect(('localhost', port))

while True:
    cmd = input("Enter a message:(\"send mboxId message\") or (\"receive mboxId\") : ")
    if cmd == 'quit':
        s.sendto(cmd.encode(), ('localhost', port))    
        break
    else: 
        s.sendto(cmd.encode(), ('localhost', port)) 
        cmd, addr = s.recvfrom(BUFF_SIZE) 
        print(cmd.decode())
s.close()
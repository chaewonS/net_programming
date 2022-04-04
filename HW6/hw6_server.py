from socket import *


BUFF_SIZE = 1024
port = 5555

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', port))

mboxID_msg = {} 

while True:    
    data, addr = s.recvfrom(BUFF_SIZE)

    cmd, mboxID, *msg = data.decode().split(maxsplit=2) 
    msg = " ".join(msg) #리스트를 문자열로 합치기

    if cmd == 'send': 
        if mboxID not in mboxID_msg: 
            mboxID_msg[mboxID] = []  #리스트 생성
        mboxID_msg[mboxID].append(msg) #mboxID에 msg 저장
        s.sendto("OK".encode(), addr) #클라이언트로 전송
        
    elif cmd == 'receive': 
        #존재하지 않은 mboxID OR 메시지가 없는 mboxID
        if (mboxID not in mboxID_msg) or (not(mboxID_msg[mboxID])):
            s.sendto("No messages".encode(), addr) #클라이언트로 전송
        else: 
            s.sendto(mboxID_msg[mboxID].pop(0).encode(), addr) #mboxID 제일 앞에 있는 메시지 전송
    
    elif data.decode() == "quit": 
        break

s.close()
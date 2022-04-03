from socket import *

s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()

    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')

    #웹 서버 코드 작성
    req_msg = req[0].split()[1].strip('/') #ex)127.0.0.1/index.html

    #동작1
    if req_msg == "index.html":
        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: text/html \r\n')
        c.send(b'\r\n')
        f = open("index.html", 'r', encoding='utf-8')
        data = f.read()
        c.send(data.encode('euc-kr'))

    #동작2
    elif req_msg == "iot.png":
        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: image/png\r\n')
        c.send(b'\r\n')
        f = open('iot.png', 'rb')
        data = f.read()
        c.send(data)

    #동작3
    elif req_msg == "favicon.ico":
        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: image/x-icon\r\n')
        c.send(b'\r\n')
        f = open('favicon.ico', 'rb')
        data = f.read()
        c.send(data)

    #동작4
    else:
        c.send(b'HTTP/1.1 404 Not Found\r\n')
        c.send(b'\r\n')
        c.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
        c.send(b'<BODY>Not Found</BODY></HTML>')

    # 객체 전송 후(동작 4가지), 소켓 닫기
    c.close()
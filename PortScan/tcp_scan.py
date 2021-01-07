# tcp scan
import socket
# cmd -> netstat -ano
# 열려있는 포트 확인 가능
with socket.socket() as s:
    addr = ("127.0.0.1", 8080)
    try:
        s.connect(addr)
        print("80 tcp socket is opened")
    except:
        print("80 tcp socket is closed")

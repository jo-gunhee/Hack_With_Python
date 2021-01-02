import socket

# s = socket.socket() ::socket을 수동으로 close해야함
with socket.socket() as s:
    addr = ("www.daum.net", 80)  # 웹 통신에는 80, 443 포트를 사용한다.
    s.connect(addr)  # 통신시작
    s.send("GET /\n".encode())
    data = s.recv(1024)  # receive 1024byte
    print(data.decode())

'''
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>302 Found</title>
</head><body>
<h1>Found</h1>
<p>The document has moved <a href="http://status.daum.net/error/error403.html">here</a>.</p> 
</body></html>
'''

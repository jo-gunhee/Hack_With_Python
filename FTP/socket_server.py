import socket

with socket.socket() as s:
    addr = ("0.0.0.0", 80)  # allow all addresses
    s.bind(addr)
    s.listen()
    print("start server..")

    conn, addr = s.accept()
    print("accept {}:{}".format(addr[0], addr[1]))
    # conn :: 1:1 통신을 위한 객체
    data = conn.recv(1024)
    conn.send("Hi this is web.".encode())

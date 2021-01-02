import socket

with socket.socket() as s:
    addr = ("0.0.0.0", 4444)
    s.bind(addr)
    s.listen()
    print("start server..")
    conn, addr = s.accept()
    print("accept {}:{}".format(addr[0], addr[1]))
    while(1):
        data = conn.recv(1024)
        if data.decode() == "quit":
            print("Quit connection")
            exit()
        conn.send(data)
        print(data.decode())

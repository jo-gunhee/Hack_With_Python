import socket


def call():
    data = s.recv(1024).decode()
    print(data)


s = socket.socket()
s.connect(("@.@.@.@", 21))  # Insert your IP
call()

s.send("PWD".encode())
call()

s.send("LIST".encode())
call()

s.send("USER anonymous".encode())
call()

s.send("PASS anonymous".encode())
call()

s.send("PORT 192,168,1,36,25,25".encode())  # 25*255+25
call()

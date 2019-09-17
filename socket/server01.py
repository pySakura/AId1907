# -*- coding:utf-8 -*-
import socket
server = socket.socket()
server.bind(('127.0.0.1',9999))
server.listen()

s,raddr = server.accept()   #等待对方连过来
while True:
    data = s.recv(1024)
    print(data.decode())
    s.send(b'ack')

s.close()
server.close()
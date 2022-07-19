#!/usr/bin/env python3

import socket

server_address = "B8:27:EB:75:E6:45"
server_port = 1
with socket.socket(socket.AF_BLUETOOTH,
                   socket.SOCK_STREAM,
                   socket.BTPROTO_RFCOMM) as c:

    c.connect((server_address, server_port))
    c.send(b"desserts")
    print(c.recv(1024).decode())


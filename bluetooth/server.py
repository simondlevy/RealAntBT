#!/usr/bin/env python3

import socket

server_address = 'B8:27:EB:75:E6:45'
server_port = 1
backlog = 1
size = 1024
while True:
    with socket.socket(socket.AF_BLUETOOTH,
                       socket.SOCK_STREAM,
                       socket.BTPROTO_RFCOMM) as s:
        s.bind((server_address, server_port))
        s.listen(backlog)
        print('Waiting for connection...')
        client, address = s.accept()
        print(f'Connection from {address}')
        while True:
            try:
                data = client.recv(size)
                if data:
                    print(data)
                    client.send(data)
            except ConnectionResetError:
                print('Client disconnected')
                break


#!/usr/bin/python3

import socket
import os

ADDRESS = 'B8:27:EB:75:E6:45'
PORT    = 1
MSGSIZE = 1024

# Enable bluetooth
os.system('sudo hciconfig hci0 piscan')

while True:

    with socket.socket(socket.AF_BLUETOOTH,
                       socket.SOCK_STREAM,
                       socket.BTPROTO_RFCOMM) as s:

        s.bind((ADDRESS, PORT))

        s.listen(1) # support only one client

        print('Waiting for connection...')
        client, address = s.accept()

        print(f'Connection from {address}')

        while True:

            try:
                data = client.recv(MSGSIZE)

                if data:
                    print(data)

            except ConnectionResetError:
                print('Client disconnected')
                break

            except KeyboardInterrupt:
                break

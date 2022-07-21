#!/usr/bin/python3

import socket
import os

ADDRESS = 'B8:27:EB:75:E6:45'
PORT = 1
MSGSIZE = 1024


def serve_connection(client):

    try:

        data = client.recv(MSGSIZE)

        if data:

            print([int(d)-90 for d in data])

    except ConnectionResetError:
        print('Client disconnected')


def accept_connections():

    with socket.socket(socket.AF_BLUETOOTH,
                       socket.SOCK_STREAM,
                       socket.BTPROTO_RFCOMM) as s:

        s.bind((ADDRESS, PORT))

        s.listen(1)  # support only one client

        print('Waiting for connection...')
        client, address = s.accept()

        print(f'Connection from {address}')

        while True:

            try:
                serve_connection(client)

            except KeyboardInterrupt:
                break


def main():

    # Enable bluetooth
    os.system('sudo hciconfig hci0 piscan')

    while True:

        try:
            accept_connections()

        except KeyboardInterrupt:
            break


main()

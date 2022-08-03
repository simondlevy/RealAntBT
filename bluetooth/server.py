#!/usr/bin/python3

'''
Server program to send accepts commands for the RealAnt
over a Bluetooth socket

Copyright (c) 2022 Matt Stock, Simon D. Levy

MIT License
'''

from time import sleep
import socket
import os
import argparse

from realant import RealAnt

BLUETOOTH_PORT = 1
MSGSIZE = 1024


def handle_message(client, ant):

    # Client will send an all-None message to set this flag to False when done
    more = True

    try:

        data = client.recv(MSGSIZE)

        if data:

            # Convert bytes into angles; then convert out-of-bounds to None
            angles = [a if abs(a) <= 90 else None
                      for a in [int(d)-90 for d in data]]
            print(angles)
            if all(map(lambda a: a is None, angles)):
                more = False
            ant.set(angles)

    except ConnectionResetError:
        print('Client disconnected')

    return more


def serve_connections(ant, address):

    with socket.socket(socket.AF_BLUETOOTH,
                       socket.SOCK_STREAM,
                       socket.BTPROTO_RFCOMM) as s:

        s.bind((address, BLUETOOTH_PORT))

        s.listen(1)  # support only one client

        print('Waiting for connection...')
        client, address = s.accept()

        print(f'Connection from {address}')

        while True:

            try:
                if not handle_message(client, ant):
                    break

            except KeyboardInterrupt:
                break


def main():

    parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-p', '--commport', help='com port',
                        default='/dev/ttyACM0')
    parser.add_argument('-d', '--delay', help='startup delay in seconds',
                        type=float, default=0)
    parser.add_argument('-s', '--server', help='server address',
                        default='B8:27:EB:75:E6:45')

    args = parser.parse_args()

    # Wait a bit before starting
    sleep(args.delay)

    # Enable bluetooth
    os.system('sudo hciconfig hci0 piscan')

    # Start the RealAnt
    ant = RealAnt(args.commport)
    ant.connect()

    # Loop forever, accepting new clients
    while True:

        try:
            serve_connections(ant, args.server)

        except KeyboardInterrupt:
            break


main()

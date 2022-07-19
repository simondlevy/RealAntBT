#!/usr/bin/python3
'''
Subclasses BluetoothSocket to serve messages for running the RealAnt

Copyright 2022  Matt Stock, Simon D. Levy

MIT License
'''

from bluetooth_server import BluetoothServer


class RealAntServer(BluetoothServer):

    def __init__(self):

        BluetoothServer.__init__(self)

    def handleMessage(self, message):

        print(message)


if __name__ == '__main__':

    server = RealAntServer()

    server.start()

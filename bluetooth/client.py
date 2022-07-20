#!/usr/bin/python3

import socket
import numpy as np

server_address = 'B8:27:EB:75:E6:45'

server_port = 1

with socket.socket(socket.AF_BLUETOOTH,
                   socket.SOCK_STREAM,
                   socket.BTPROTO_RFCOMM) as c:

    c.connect((server_address, server_port))

    angle = -90

    while True:

        # c.send(b'Move, ant!')
        #c.send(str(count).encode('utf8'))
        c.send(bytearray([angle+90]))

        angle += 1

        if angle > 90:
            angle = 0


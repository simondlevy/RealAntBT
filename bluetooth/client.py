#!/usr/bin/python3

import socket
import numpy as np

server_address = 'B8:27:EB:75:E6:45'

server_port = 1

with socket.socket(socket.AF_BLUETOOTH,
                   socket.SOCK_STREAM,
                   socket.BTPROTO_RFCOMM) as c:

    c.connect((server_address, server_port))

    while True:

        angles = [int(v) for v in np.random.random(8) * 180 - 90]

        # We add 90 because we can't encode negative values
        c.send(bytearray([a+90 for a in angles]))

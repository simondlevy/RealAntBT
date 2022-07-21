#!/usr/bin/python3

import socket
import numpy as np

import time
from optparse import OptionParser

server_address = 'B8:27:EB:75:E6:45'

server_port = 1


def stand(conn, sleep_time):

    behavior = [
            [45, None, 45, None, 45, None, 45, None],
            [30, None, 45, None, 45, None, 45, None],
            [30, 50, 45, None, 45, None, 45, None],
            [45, 50, 45, None, 45, None, 45, None],
            [45, 50, 30, None, 45, None, 45, None],
            [45, 50, 30, -50, 45, None, 45, None],
            [45, 50, 45, -50, 45, None, 45, None],
            [45, 50, 45, -50, 30, None, 45, None],
            [45, 50, 45, -50, 30, 0, 45, None],
            [45, 50, 45, -50, 45, 0, 45, None],
            [45, 50, 45, -50, 45, 0, 30, None],
            [45, 50, 45, -50, 45, 0, 30, 0],
            [45, 50, 45, -50, 45, 0, 45, 0]
            ]

    for angles in behavior:
        
        # XXX Send angles over conn
        for a in angles:
            if a != None:
                a += 90
        conn.send(bytearray(angles))
        time.sleep(sleep_time)


def step(conn, sleep_time, max_time):
    '''
    Returns total time taken on this step, rounded to sleep_time
    '''

    behavior = [
            [45, 50, 45, -50, 45, 0, 45, 0],
            [30, 50, 45, -50, 45, 0, 45, 0],
            [30, -20, 45, -50, 45, 0, 45, 0],
            [45, -20, 45, -50, 45, 0, 45, 0],
            [45, 0, 45, 0, 45, -20, 45, -50],
            [45, 0, 45, 0, 30, -20, 45, -50],
            [45, 0, 45, 0, 30, 50, 45, -50],
            [45, 0, 45, 0, 45, 50, 45, -50],
            [45, 0, 45, 0, 45, 50, 30, -50],
            [45, 0, 45, 0, 45, 50, 30, 20],
            [45, 0, 45, 0, 45, 50, 45, 20],
            [45, 50, 45, 20, 45, 0, 45, 0],
            [45, 50, 30, 20, 45, 0, 45, 0],
            [45, 50, 30, -50, 45, 0, 45, 0]
            ]

    for (count, angles) in enumerate(behavior):

        # XXX send angles over conn
        conn.send(bytearray([a+90 for a in angles]))

        time.sleep(sleep_time)

        if count*sleep_time >= max_time:
            break

    return sleep_time * len(angles)


def main():

    # Allow user to specify a non-default com port and runtime
    # XXX also allow specifying server address
    parser = OptionParser()

    parser.add_option('-a', '--server_address', dest='server_address',
                      help='server address', type='str',
                      default='B8:27:EB:75:E6:45')

    parser.add_option('-p', '--port', dest='port',
                      help='com port, metavar="FILE',
                      default='/dev/ttyACM0')
    parser.add_option('-t', '--time', dest='time', help='run time',
                      type='float', default=5)
    parser.add_option('-s', '--sleep', dest='sleep', help='sleep time',
                      type='float', default=0.4)

    (opts, _) = parser.parse_args()


    with socket.socket(socket.AF_BLUETOOTH,
                       socket.SOCK_STREAM,
                       socket.BTPROTO_RFCOMM) as conn:

        conn.connect((server_address, server_port))

        start = time.time()

        time_left = opts.time

        # XXX open connection to server

        while True:

            try:
                time_left -= step(conn, opts.sleep, time_left)

                if time_left <= 0:
                    break

            except KeyboardInterrupt:
                break

    print(time.time()-start)


if __name__ == "__main__":
    main()

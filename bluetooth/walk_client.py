#!/usr/bin/python3

'''
Client program to send walking commands to the RealAnt
over a Bluetooth socket

Copyright (c) 2022 Matt Stock, Simon D. Levy

MIT License
'''

import socket
import time
from optparse import OptionParser

SERVER_ADDRESS = 'B8:27:EB:75:E6:45'

SERVER_PORT = 1

# Out-of-bound value means unspecified angle
NO_ANGLE = 99


def send(conn, angles, sleep_time):

    try:
        conn.send(bytearray([a+90 for a in angles]))
        time.sleep(sleep_time)

    except ConnectionResetError:
        print('Server disconnected')
        exit(0)

    except KeyboardInterrupt:
        exit(0)


def stand(conn, sleep_time):

    none = NO_ANGLE

    behavior = [
            [45, none, 45, none, 45, none, 45, none],
            [30, none, 45, none, 45, none, 45, none],
            [30, 50, 45, none, 45, none, 45, none],
            [45, 50, 45, none, 45, none, 45, none],
            [45, 50, 30, none, 45, none, 45, none],
            [45, 50, 30, -50, 45, none, 45, none],
            [45, 50, 45, -50, 45, none, 45, none],
            [45, 50, 45, -50, 30, none, 45, none],
            [45, 50, 45, -50, 30, 0, 45, none],
            [45, 50, 45, -50, 45, 0, 45, none],
            [45, 50, 45, -50, 45, 0, 30, none],
            [45, 50, 45, -50, 45, 0, 30, 0],
            [45, 50, 45, -50, 45, 0, 45, 0]
            ]

    for angles in behavior:

        send(conn, angles, sleep_time)


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

        send(conn, angles, sleep_time)

        if count*sleep_time >= max_time:
            break

    return sleep_time * len(angles)


def quit(conn, sleep_time):

    send(conn, [NO_ANGLE]*8, sleep_time)


def walk(conn, total_time, sleep_time):

    time_left = total_time

    while True:

        try:
            time_left -= step(conn, sleep_time, time_left)

            if time_left <= 0:
                break

        except KeyboardInterrupt:
            break


def main():

    # Allow user to specify a non-default com port and runtime
    # XXX also allow specifying server address
    parser = OptionParser()

    parser.add_option('-a', '--SERVER_ADDRESS', dest='SERVER_ADDRESS',
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

        try:
            conn.connect((SERVER_ADDRESS, SERVER_PORT))

        except ConnectionRefusedError:
            print('Cannot connect to server.  Is it running?')
            exit(0)

        stand(conn, opts.sleep)

        walk(conn, opts.time, opts.sleep)

        quit(conn, opts.sleep)


if __name__ == "__main__":
    main()

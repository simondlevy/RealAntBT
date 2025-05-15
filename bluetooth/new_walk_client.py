#!/usr/bin/python3

'''
Client program to send walking commands to the RealAnt
over a Bluetooth socket

Copyright (c) 2022 Matt Stock, Simon D. Levy

MIT License
'''

import socket
import time
import argparse

# Out-of-bound value means unspecified angle
NO_ANGLE = 99

# XXX should optimize this
SLEEP = 0.4


def send(conn, angles):

    try:
        conn.send(bytearray([a+90 for a in angles]))
        time.sleep(SLEEP)

    except ConnectionResetError:
        print('Server disconnected')
        exit(0)

    except KeyboardInterrupt:
        exit(0)


def stand(conn):

    non = NO_ANGLE

    behavior = [
            # 1    2    3     4    5    6      7   8
            [+45, non, +45,  non, +45, non,  +45, non],
            [+30, non, +45,  non, +45, non,  +45, non],
            [+30, +50, +45,  non, +45, non,  +45, non],
            [+45, +50, +45,  non, +45, non,  +45, non],
            [+45, +50, +30,  non, +45, non,  +45, non],
            [+45, +50, +30, -50,  +45, non,  +45, non],
            [+45, +50, +45, -50,  +45, non,  +45, non],
            [+45, +50, +45, -50,  +30, non,  +45, non],
            [+45, +50, +45, -50,  +30, 000,  +45, non],
            [+45, +50, +45, -50,  +45, 000,  +45, non],
            [+45, +50, +45, -50,  +45, 000,  +30, non],
            [+45, +50, +45, -50,  +45, 000,  +30, 000],
            [+45, -50, +45, -50,  +45, -50,  +45, -50]
            ]

    for angles in behavior:

        send(conn, angles)


def step(conn, max_time):
    '''
    Returns total time taken on this step, rounded to SLEEP
    '''

    behavior = [
            # 1    2    3    4    5    6    7    8
            [+45, +50, +45, -50, +45, 000, +45, 000],
            [+30, +50, +45, -50, +45, 000, +45, 000],
            [+30, -20, +45, -50, +45, 000, +45, 000],
            [+45, -20, +45, -50, +45, 000, +45, 000],
            [+45, 000, +45, 000, +45, -20, +45, -50],
            [+45, 000, +45, 000, +30, -20, +45, -50],
            [+45, 000, +45, 000, +30, +50, +45, -50],
            [+45, 000, +45, 000, +45, +50, +45, -50],
            [+45, 000, +45, 000, +45, +50, +30, -50],
            [+45, 000, +45, 000, +45, +50, +30, +20],
            [+45, 000, +45, 000, +45, +50, +45, +20],
            [+45, +50, +45, +20, +45, 000, +45, 000],
            [+45, +50, +30, +20, +45, 000, +45, 000],
            [+45, +50, +30, -50, +45, 000, +45, 000]
            ]

    for (count, angles) in enumerate(behavior):

        send(conn, angles)

        if count*SLEEP >= max_time:
            break

    return SLEEP * len(angles)


def quit(conn):

    send(conn, [NO_ANGLE]*8)


def walk(conn, total_time):

    time_left = total_time

    while True:

        try:
            time_left -= step(conn, time_left)

            if time_left <= 0:
                break

        except KeyboardInterrupt:
            break


def main():

    parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-s', '--server', help='server address')

    parser.add_argument('-p', '--port', help='server port',
                        type=int, default=1)

    parser.add_argument('-t', '--time', help='running time',
                        type=float, default=5.0)

    args = parser.parse_args()

    with socket.socket(socket.AF_BLUETOOTH,
                       socket.SOCK_STREAM,
                       socket.BTPROTO_RFCOMM) as conn:

        try:
            conn.connect((args.server, args.port))

        except ConnectionRefusedError:
            print('Cannot connect to server.  Is it running?')
            exit(0)

        stand(conn)

        #walk(conn, args.time)

        quit(conn)


if __name__ == "__main__":
    main()

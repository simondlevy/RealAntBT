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


def send(conn, angles, inverted=False):

    try:
        conn.send(bytearray([a+90 for a in angles]))
        time.sleep(SLEEP)

    except ConnectionResetError:
        print('Server disconnected')
        exit(0)

    except KeyboardInterrupt:
        exit(0)


def step(servo_id, conn, inverted, angle, max_time):

    x = NO_ANGLE

    behavior = [ [x, x, x, x, x, x, x, x] ]

    for (count, angles) in enumerate(behavior):

        angles[servo_id-1] = angle

        print(angles)

        send(conn, angles, inverted)

        if count*SLEEP >= max_time:
            break

    return SLEEP * len(angles)


def quit(conn):

    send(conn, [NO_ANGLE]*8)


def test(servo_id, conn, inverted, angle, total_time):

    time_left = total_time

    while True:

        try:
            time_left -= step(servo_id, conn, inverted, angle, time_left)

            if time_left <= 0:
                break

        except KeyboardInterrupt:
            break


def main():

    parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n', '--number', help='servo number (1..8)',
                        type=int, default=1)

    parser.add_argument('-a', '--angle', help='servo angle (-50..+50)',
                        type=int, default=0)

    parser.add_argument('-s', '--server', help='server address')

    parser.add_argument('-i', '--inverted',
                        help='inverted motor numbering (odd numbers inside)',
                        action='store_true')

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

        test(args.number, conn, args.inverted, args.angle, args.time)

        quit(conn)


if __name__ == "__main__":
    main()

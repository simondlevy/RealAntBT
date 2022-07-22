#!/usr/bin/python3
'''
Make the RealAnt wiggle a bit in place

Copyright (c) 2022 Matt Stock, Simon D. Levy

MIT License
'''

from realant import RealAnt

from time import sleep
from optparse import OptionParser

JOINT = 3
ANGLE_STEP = 1


def main():

    # Allow user to specify a non-default com port
    parser = OptionParser()
    parser.add_option('-p', '--port', dest='port',
                      help='com port',
                      default='/dev/ttyACM0')
    (opts, _) = parser.parse_args()

    ant = RealAnt(opts.port)

    ant.connect()

    angles = [None]*8

    a = 0
    d = +1

    while True:

        try:

            angles[JOINT] = a
            ant.set(angles)

            print(ant.get())

            a += d*ANGLE_STEP

            if a >= ant.MAX_ANGLE:
                d = -1
            if a <= -ant.MAX_ANGLE:
                d = +1

        except KeyboardInterrupt:
            break

    ant.disconnect()


if __name__ == "__main__":

    main()

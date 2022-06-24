#!/usr/bin/python3
'''
Resets the real ant's joint angles to zero

Copyright (c) 2022 Matt Stock, Simon D. Levy

MIT License
'''

from realant import RealAnt

from time import sleep
from optparse import OptionParser

JOINT = 6
DELAY = .01
ANGLE_STEP = 1


def main():

    # Allow user to specify a non-default com port
    parser = OptionParser()
    parser.add_option('-p', '--port', dest='port',
                      help='com port, metavar="FILE',
                      default='/dev/ttyACM0')
    (opts, _) = parser.parse_args()

    ant = RealAnt(opts.port)

    ant.connect()

    angles = [0]*8

    ant.set(angles)

    sleep(1)

    ant.disconnect()


if __name__ == "__main__":

    main()

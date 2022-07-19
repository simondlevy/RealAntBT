#!/usr/bin/python3
'''
Make the RealAnt wiggle a bit in place

Copyright (c) 2022 Matt Stock, Simon D. Levy

MIT License
'''

from realant import RealAnt

from time import sleep
from optparse import OptionParser


def moveAll(ant, pos):
    ant.set([pos]*8)


def moveOuter(ant, pos):
    ant.set([pos, None, pos, None, pos, None, pos, None])


def moveInner(ant, pos):
    ant.set([None, pos, None, pos, None, pos, None, pos])


def stand(ant):
    moveInner(ant, 0)
    moveOuter(ant, 60)


def sit(ant):
    moveAll(ant, 0)


def rotate(ant, rot="CW"):
    sit(ant)
    sleep(0.5)
    angle = 90 if rot == "CW" else -90
    moveInner(ant, angle)
    sleep(0.5)
    stand(ant)
    sleep(0.5)
    moveInner(ant, 0)


def main():

    # Allow user to specify a non-default com port
    parser = OptionParser()
    parser.add_option('-p', '--port', dest='port',
                      help='com port, metavar="FILE',
                      default='/dev/ttyACM0')
    (opts, _) = parser.parse_args()

    ant = RealAnt(opts.port)

    ant.connect()

    sit(ant)
    sleep(1)
    stand(ant)
    sleep(1)
    rotate(ant)

    ant.disconnect()


if __name__ == "__main__":
    main()

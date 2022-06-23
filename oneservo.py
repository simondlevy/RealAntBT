#!/usr/bin/python3
'''
Make the RealAnt wiggle a bit in place
'''

from realant import RealAnt

from time import sleep
from optparse import OptionParser

JOINT = 1


def main():

    # Allow user to specify a non-default com port
    parser = OptionParser()
    parser.add_option('-p', '--port', dest='port',
                      help='com port, metavar="FILE',
                      default='/dev/ttyACM0')
    (opts, _) = parser.parse_args()

    ant = RealAnt(opts.port)

    angles = [None]*8

    angles[JOINT] = 0

    print(angles)

    ant.set(angles)

    exit(0)

    sleep(1)

    for a in range(0, 45):

        angles[JOINT] = a

        ant.set(angles)

        sleep(.1)

    ant.connect()

    ant.disconnect()


if __name__ == "__main__":

    main()

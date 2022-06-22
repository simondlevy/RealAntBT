#!/usr/bin/python3
'''
Make the RealAnt wiggle a bit in place
'''

from realant import sit, stand, rotate, connect
from ax12 import Ax12

from time import sleep
from optparse import OptionParser

def main():

    # Allow user to specify a non-default com port
    parser = OptionParser()
    parser.add_option('-p', '--port', dest='port',
            help='com port, metavar="FILE',
            default='/dev/ttyACM0')
    (opts,_) = parser.parse_args()

    servos = connect(opts.port)

    sit(servos)
    sleep(1)
    stand(servos)
    sleep(1)
    # flip(servos)
    rotate(servos)
    # sleep(1)
    # walk(servos)
    # sit(servos)

    Ax12.disconnect()


if __name__ == "__main__":
    main()

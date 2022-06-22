#!/usr/bin/python3
'''
Run one servo on the RealAnt
'''

from ax12.movement import moveServo, connect
from ax12 import Ax12

from optparse import OptionParser
from time import sleep

# 210 = 90 deg (down)
# 512 = 0 deg (straight out)
# 600 = 45 deg
# 775 = 80 deg (max safe up)

IDX = 8
POS = 600

def main():

    # Allow user to specify a non-default com port
    parser = OptionParser()
    parser.add_option('-p', '--port', dest='port',
            help='com port, metavar="FILE',
            default='/dev/ttyACM0')
    (opts,_) = parser.parse_args()

    servos = connect(opts.port)

    moveServo(servos, IDX, POS)

    sleep(1)

    Ax12.disconnect()


if __name__ == "__main__":
    main()

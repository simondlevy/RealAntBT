#!/usr/bin/python3
'''
Run one servo on the RealAnt
'''

from realant import moveServo, connect
from ax12 import Ax12

from optparse import OptionParser
from time import sleep

# 210 = 90 deg (down)
# 512 = 0 deg (straight out)
# 600 = 45 deg
# 775 = 80 deg (max safe up)

MOTOR   = 8
POS_MIN = 210
POS_MAX = 775
DELAY   = 0.1

def main():

    # Allow user to specify a non-default com port
    parser = OptionParser()
    parser.add_option('-p', '--port', dest='port',
            help='com port, metavar="FILE',
            default='/dev/ttyACM0')
    (opts,_) = parser.parse_args()

    servos = connect(opts.port)

    moveServo(servos, MOTOR, int((POS_MIN+POS_MAX)/2))

    sleep(1)

    Ax12.disconnect()


if __name__ == "__main__":
    main()

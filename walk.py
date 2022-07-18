#!/usr/bin/python3


from realant import RealAnt

import time
from optparse import OptionParser

SLEEP_TIME = 0.4


def stand(ant):

    angles = [
            [45, None, 45, None, 45, None, 45, None],
            [30, None, 45, None, 45, None, 45, None],
            [30, 50, 45, None, 45, None, 45, None],
            [45, 50, 45, None, 45, None, 45, None],
            [45, 50, 30, None, 45, None, 45, None],
            [45, 50, 30, -50, 45, None, 45, None],
            [45, 50, 45, -50, 45, None, 45, None],
            [45, 50, 45, -50, 30, None, 45, None],
            [45, 50, 45, -50, 30, 0, 45, None],
            [45, 50, 45, -50, 45, 0, 45, None],
            [45, 50, 45, -50, 45, 0, 30, None],
            [45, 50, 45, -50, 45, 0, 30, 0],
            [45, 50, 45, -50, 45, 0, 45, 0]
            ]

    for angle in angles:
        ant.set(angle)
        time.sleep(SLEEP_TIME)


def step(ant, maxtime):
    '''
    Returns total time taken on this step, rounded to SLEEP_TIME
    '''

    angles = [
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

    for (count, angle) in enumerate(angles):
        ant.set(angle)
        time.sleep(SLEEP_TIME)
        if count*SLEEP_TIME >= maxtime:
            break

    return SLEEP_TIME * len(angles)


def main():

    # Allow user to specify a non-default com port and runtime
    parser = OptionParser()
    parser.add_option('-p', '--port', dest='port',
                      help='com port, metavar="FILE',
                      default='/dev/ttyACM0')
    parser.add_option('-t', '--time', dest='time', help='run time',
                      type='float', default=5)

    (opts, _) = parser.parse_args()

    ant = RealAnt(opts.port)

    ant.connect()

    stand(ant)

    start = time.time()

    timeleft = opts.time

    while True:

        try:
            timeleft -= step(ant, timeleft)

            if timeleft <= 0:
                break

        except KeyboardInterrupt:
            break

    print(time.time()-start)

    ant.disconnect()


if __name__ == "__main__":
    main()

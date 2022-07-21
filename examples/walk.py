#!/usr/bin/python3

'''
Make the RealAnt walk

Copyright (c) 2022 Matt Stock, Simon D. Levy

MIT License
'''


from realant import RealAnt

import time
from optparse import OptionParser

def stand(ant, sleep_time):

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
        time.sleep(sleep_time)


def step(ant, sleep_time, max_time):
    '''
    Returns total time taken on this step, rounded to sleep_time
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
        time.sleep(sleep_time)
        if count*sleep_time >= max_time:
            break

    return sleep_time * len(angles)


def main():

    # Allow user to specify a non-default com port and runtime
    parser = OptionParser()
    parser.add_option('-p', '--port', dest='port',
                      help='com port, metavar="FILE',
                      default='/dev/ttyACM0')
    parser.add_option('-t', '--time', dest='time', help='run time',
                      type='float', default=5)
    parser.add_option('-s', '--sleep', dest='sleep', help='sleep time',
                      type='float', default=0.4)

    (opts, _) = parser.parse_args()

    ant = RealAnt(opts.port)

    ant.connect()

    stand(ant, opts.sleep)

    start = time.time()

    time_left = opts.time

    while True:

        try:
            time_left -= step(ant, opts.sleep, time_left)

            if time_left <= 0:
                break

        except KeyboardInterrupt:
            break

    print(time.time()-start)

    ant.disconnect()


if __name__ == "__main__":
    main()

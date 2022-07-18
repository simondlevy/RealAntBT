#!/usr/bin/python3


from realant import RealAnt

from time import sleep
from optparse import OptionParser

SLEEP_TIME = 0.4


def stand(ant):

    ant.set([45, None, 45, None, 45, None, 45, None])
    sleep(SLEEP_TIME)
    ant.set([30, None, 45, None, 45, None, 45, None])
    sleep(SLEEP_TIME)
    ant.set([30, 50, 45, None, 45, None, 45, None])
    sleep(SLEEP_TIME)
    ant.set([45, 50, 45, None, 45, None, 45, None])
    sleep(SLEEP_TIME)
    ant.set([45, 50, 30, None, 45, None, 45, None])
    sleep(SLEEP_TIME)
    ant.set([45, 50, 30, -50, 45, None, 45, None])
    sleep(SLEEP_TIME)
    ant.set([45, 50, 45, -50, 45, None, 45, None])
    sleep(SLEEP_TIME)
    ant.set([45, 50, 45, -50, 30, None, 45, None])
    sleep(SLEEP_TIME)
    ant.set([45, 50, 45, -50, 30, 0, 45, None])
    sleep(SLEEP_TIME)
    ant.set([45, 50, 45, -50, 45, 0, 45, None])
    sleep(SLEEP_TIME)
    ant.set([45, 50, 45, -50, 45, 0, 30, None])
    sleep(SLEEP_TIME)
    ant.set([45, 50, 45, -50, 45, 0, 30, 0])
    sleep(SLEEP_TIME)
    ant.set([45, 50, 45, -50, 45, 0, 45, 0])


def sleepfor(sec):
    sleep(sec)
    return sec


def step(ant):

    t = 0

    ant.set([45, 50, 45, -50, 45, 0, 45, 0])
    t += sleepfor(SLEEP_TIME)
    ant.set([30, 50, 45, -50, 45, 0, 45, 0])
    t += sleepfor(SLEEP_TIME)
    ant.set([30, -20, 45, -50, 45, 0, 45, 0])
    t += sleepfor(SLEEP_TIME)
    ant.set([45, -20, 45, -50, 45, 0, 45, 0])
    t += sleepfor(SLEEP_TIME)
    ant.set([45, 0, 45, 0, 45, -20, 45, -50])
    t += sleepfor(SLEEP_TIME)
    ant.set([45, 0, 45, 0, 30, -20, 45, -50])
    t += sleepfor(SLEEP_TIME)
    ant.set([45, 0, 45, 0, 30, 50, 45, -50])
    t += sleepfor(SLEEP_TIME)
    ant.set([45, 0, 45, 0, 45, 50, 45, -50])
    t += sleepfor(SLEEP_TIME)
    ant.set([45, 0, 45, 0, 45, 50, 30, -50])
    t += sleepfor(SLEEP_TIME)
    ant.set([45, 0, 45, 0, 45, 50, 30, 20])
    t += sleepfor(SLEEP_TIME)
    ant.set([45, 0, 45, 0, 45, 50, 45, 20])
    t += sleepfor(SLEEP_TIME)
    ant.set([45, 50, 45, 20, 45, 0, 45, 0])
    t += sleepfor(SLEEP_TIME)
    ant.set([45, 50, 30, 20, 45, 0, 45, 0])
    t += sleepfor(SLEEP_TIME)
    ant.set([45, 50, 30, -50, 45, 0, 45, 0])
    t += sleepfor(SLEEP_TIME)

    return t


def main():

    # Allow user to specify a non-default com port and runtime
    parser = OptionParser()
    parser.add_option('-p', '--port', dest='port',
                      help='com port, metavar="FILE',
                      default='/dev/ttyACM0')
    parser.add_option('-t', '--time', dest='time',
                      help='run time', default=5)

    (opts, _) = parser.parse_args()

    ant = RealAnt(opts.port)

    ant.connect()

    stand(ant)

    total_time = 0

    while total_time < opts.time:

        try:
            total_time += step(ant)

        except KeyboardInterrupt:
            break

    ant.disconnect()


if __name__ == "__main__":
    main()

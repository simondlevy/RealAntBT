#!/usr/bin/python3


import numpy as np
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



def crawl(ant):


    while True:

        ant.set([45, 50, 45, -50, 45, 0, 45, 0])
        sleep(SLEEP_TIME)
        ant.set([30, 50, 45, -50, 45, 0, 45, 0])
        sleep(SLEEP_TIME)
        ant.set([30, -20, 45, -50, 45, 0, 45, 0])
        sleep(SLEEP_TIME)
        ant.set([45, -20, 45, -50, 45, 0, 45, 0])
        sleep(SLEEP_TIME)
        ant.set([45, 0, 45, 0, 45, -20, 45, -50])
        sleep(SLEEP_TIME)
        ant.set([45, 0, 45, 0, 30, -20, 45, -50])
        sleep(SLEEP_TIME)
        ant.set([45, 0, 45, 0, 30, 50, 45, -50])
        sleep(SLEEP_TIME)
        ant.set([45, 0, 45, 0, 45, 50, 45, -50])
        sleep(SLEEP_TIME)
        ant.set([45, 0, 45, 0, 45, 50, 30, -50])
        sleep(SLEEP_TIME)
        ant.set([45, 0, 45, 0, 45, 50, 30, 20])
        sleep(SLEEP_TIME)
        ant.set([45, 0, 45, 0, 45, 50, 45, 20])
        sleep(SLEEP_TIME)
        ant.set([45, 50, 45, 20, 45, 0, 45, 0])
        sleep(SLEEP_TIME)
        ant.set([45, 50, 30, 20, 45, 0, 45, 0])
        sleep(SLEEP_TIME)
        ant.set([45, 50, 30, -50, 45, 0, 45, 0])
        sleep(SLEEP_TIME)


def main():

    # Allow user to specify a non-default com port
    parser = OptionParser()
    parser.add_option('-p', '--port', dest='port',
                      help='com port, metavar="FILE',
                      default='/dev/ttyACM0')
    (opts, _) = parser.parse_args()

    ant = RealAnt(opts.port)

    ant.connect()
    
    #stand(ant)
    crawl(ant)
    ant.disconnect()


if __name__ == "__main__":
    main()
             

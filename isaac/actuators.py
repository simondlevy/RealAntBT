#!/usr/bin/python3

# Simple actuator class for printing actions
#
# Copyright (c) 2022, Matt Stock & Simon D. Levy
#
# MIT License

from realant import RealAnt

from time import sleep


class RealActuator:

    def __init__(self, port='/dev/ttyACM0'):

        self.ant = RealAnt(port)
        self.ant.connect()

        self.JOINT_MAP = [1, 0, 7, 6, 5, 4, 3, 2]

        self.DELAY = 0.05

    def use(self, action):

        angles = action[self.JOINT_MAP] * self.ant.MAX_ANGLE

        sleep(self.DELAY)

        self.ant.set(angles)


class PrintActuator:
    '''
    A stubbed actuator for testing; just prints out the motor values
    '''

    def use(self, action):

        print(action)


class NullActuator:
    '''
    A stubbed actuator for testing; does nothing
    '''

    def use(self, action):

        return

def main():

    RealActuator()

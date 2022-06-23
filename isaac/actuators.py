#!/usr/bin/python3

# Simple actuator class for printing actions
#
# Copyright (c) 2022, Matt Stock & Simon D. Levy
#
# MIT License

from realant import RealAnt


class RealActuator:

    def __init__(self, port='/dev/ttyACM0'):

        self.ant = RealAnt(port)
        self.ant.connect()

        self.JOINT_MAP = [1, 0, 7, 6, 5, 4, 3, 2]

    def use(self, action):

        self.ant.set(action[self.JOINT_MAP] * 45)


class PrintActuator:
    '''
    A stubbed actuator for testing; just prints out the motor values
    '''

    def use(self, action):

        print(action)


def main():

    RealActuator()

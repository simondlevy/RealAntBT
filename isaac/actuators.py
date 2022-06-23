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

    def use(self, action):

        MOTOR = 0

        angles = [None]*8

        angles[MOTOR] = action[MOTOR] * 45

        self.ant.set(angles)


class PrintActuator:
    '''
    A stubbed actuator for testing; just prints out the motor values
    '''

    def use(self, action):

        print(action)


def main():

    RealActuator()

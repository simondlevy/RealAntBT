#!/usr/bin/python3

# Simple actuator class for printing actions
#
# Copyright (c) 2022, Matt Stock & Simon D. Levy
#
# MIT License

from realant import RealAnt

class RealActuator:

    def __init__(self):

        return

    def use(self, action):

        print(action)


class PrintActuator:
    '''
    A stubbed actuator for testing; just prints out the motor values
    '''

    def use(self, action):

        print(action)

def main():

    RealActuator()

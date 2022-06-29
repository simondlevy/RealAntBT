#!/usr/bin/python3

# A class for overriding the learned gait in RealAnt
#
# Copyright (c) 2022, Matt Stock & Simon D. Levy
#
# MIT License

import numpy as np


class Motionless:

    def __init__(self):

        return

    def get(self):

        return np.zeros(8)


class Walking:

    def __init__(self):

        self.angles = np.array([

            [-90, -50, -90, 0, -90, 0, -90, 50],
            [-45, -50, -90, 0, -90, 0, -90, 50],
            [-45, 20, -90, 0, -90, 0, -90, 50],
            [-90, 20, -90, 0, -90, 0, -90, 50],
            [-90, 0, -90, 50, -90, 20, -90, 0],
            [-90, 0, -90, 50, -45, 20, -90, 0],
            [-90, 0, -90, 50, -45, -50, -90, 0],
            [-90, 0, -90, 50, -90, -50, -90, 0],
            [-90, 0, -45, 50, -90, -50, -90, 0],
            [-90, 0, -45, -20, -90, -50, -90, 0],
            [-90, 0, -90, -20, -90, -50, -90, 0],
            [-90, -50, -90, 0, -90, 0, -90, -20],
            [-90, -50, -90, 0, -90, 0, -45, -20],
            [-90, -50, -90, 0, -90, 0, -45, 50],
            [-90, -50, -90, 0, -90, 0, -90, 50]
            ]) / 90

        self.index = 0

    def get(self):

        action = self.angles[self.index]

        self.index = (self.index + 1) % len(self.angles)

        return action

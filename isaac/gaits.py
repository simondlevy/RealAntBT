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

        self.JOINT_MAP = [1, 0, 7, 6, 5, 4, 3, 2]

        self.ANGLES = np.array([

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

        action = self.ANGLES[self.index][self.JOINT_MAP]

        self.index = (self.index + 1) % len(self.ANGLES)

        return action

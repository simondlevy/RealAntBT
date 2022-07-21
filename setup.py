#!/usr/bin/env python3

'''
Python distutils setup file for RealAnt package.

Copyright (c) 2022 Matt Stock, Simon D. Levy

MIT License
'''

from setuptools import setup

setup(
    name='realant',
    version='0.1',
    install_requires=['dynamixel-ax12'], # Not required for bluetooth client
    description='Python library for RealAnt',
    packages=['realant'],
    author='Matt Stock, Simon D. Levy',
    author_email='simon.d.levy@gmail.com',
    url='https://github.com/simondlevy/RealAnt',
    license='MIT',
    platforms='Linux'
    )

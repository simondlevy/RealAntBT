#!/usr/bin/python3
'''
Subclasses BluetoothSocket to serve messages for running a servo motor on Raspberry Pi.

Copyright 2018  Gunnar Bowman, Emily Boyes, Trip Calihan, Simon D. Levy, Shepherd Sims

MIT License
'''

from bluetooth_server import BluetoothServer
import RPi.GPIO as GPIO

class ServoServer(BluetoothServer):

    def __init__(self):

        BluetoothServer.__init__(self)

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(11,GPIO.OUT)

        self.pwm = GPIO.PWM(11, 50)
        self.pwm.start(5)

    def handleMessage(self, message):

        # Convert [0,100] => [1,11]
        duty = float(message)/10 + 1

        # Don't know why we need this range check!
        if duty >= 1 and duty <= 11:
            self.pwm.ChangeDutyCycle(duty)


if __name__ == '__main__':

    server = ServoServer()

    server.start()

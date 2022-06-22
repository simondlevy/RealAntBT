from ax12 import Ax12


class RealAnt:

    def __init__(self, devicename):

        self.devicename = devicename

        self.servos = [None]*8

    def connect(self):

        # e.g 'COM3' windows or '/dev/ttyUSB0' for Linux
        Ax12.DEVICENAME = self.devicename

        Ax12.BAUDRATE = 1_000_000

        # sets baudrate and opens com port
        Ax12.connect(self.devicename)

        for k in range(8):
            servo = Ax12(k+1)
            servo.enable_torque()
            servo.set_moving_speed(200)
            self.servos[k] = servo

    def set(self, values):
        '''
        Accepts an eight-tuple of motor values in [-1,+1] and sets the motors
        to those values.  Use None for an unspecified value.
        '''
        for k in range(8):
            value = values[k]
            if value is not None:
                self.servos[k].set_goal_position(value)

    def disconnect(self):

        Ax12.disconnect()

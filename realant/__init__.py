from ax12 import Ax12


class RealAnt:

    def __init__(self, devicename):

        self.devicename = devicename

        self.servos = [None]*8

        self.MIN_ANGLE = -60
        self.MAX_ANGLE = +60

        self.connected = False

    def connect(self):

        # e.g 'COM3' windows or '/dev/ttyUSB0' for Linux
        Ax12.DEVICENAME = self.devicename

        Ax12.BAUDRATE = 1_000_000

        Ax12.DEBUG = False

        # sets baudrate and opens com port
        Ax12.connect(self.devicename)

        for k in range(8):
            servo = Ax12(k+1)
            servo.enable_torque()
            servo.set_moving_speed(200)
            self.servos[k] = servo

        self.connected = True

    def set(self, angles):
        '''
        Accepts an eight-tuple of motor angles in [-90,+90] and sets the motors
        to those angles.  Use None for an unspecified angle.
        '''

        if not self.connected:
            raise Exception('Not connected: did you call connect()?')

        for k in range(8):

            angle = angles[k]

            if angle is not None: 

                angle = max(min(angle, self.MAX_ANGLE), self.MIN_ANGLE)

                self.servos[k].set_goal_position(int(-3.36*angle+512))

    def disconnect(self):

        Ax12.disconnect()

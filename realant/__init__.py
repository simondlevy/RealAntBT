from ax12 import Ax12


class RealAnt:

    def __init__(self, devicename):

        self.devicename = devicename

        self.servos = [None]*8

        self.MAX_ANGLE = 90
        self.SCALE_A = -3.36
        self.SCALE_B = 512

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

                angle = max(min(angle, self.MAX_ANGLE), -self.MAX_ANGLE)

                pos = int(self.SCALE_A*angle+self.SCALE_B)

                self.servos[k].set_goal_position(pos)

    def get(self):
        '''
        Returns current joint angles
        '''

        return tuple(int((servo.get_present_position() -
                          self.SCALE_B)/self.SCALE_A) for servo in self.servos)

    def disconnect(self):

        Ax12.disconnect()

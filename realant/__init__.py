import time
from ax12 import Ax12

STANDING_POS = 300


def moveAll(servoList, pos):
    for i in range(8):
        servoList[i].set_goal_position(pos)


def moveOuter(servoList, pos):
    for i in range(0, 8, 2):
        servoList[i].set_goal_position(pos)


def moveInner(servoList, pos):
    for i in range(1, 8, 2):
        servoList[i].set_goal_position(pos)


def moveServo(servos, id, pos):
    servos[id - 1].set_goal_position(pos)


def moveServos(servoIds, pos):
    for id in servoIds:
        moveServo(id, pos)


def connect(devicename):

    # e.g 'COM3' windows or '/dev/ttyUSB0' for Linux
    Ax12.DEVICENAME = devicename

    Ax12.BAUDRATE = 1_000_000

    # sets baudrate and opens com port
    Ax12.connect(devicename)

    servos = []
    for i in range(8):
        servo = Ax12(i+1)
        servo.enable_torque()
        servo.set_moving_speed(200)
        servos.append(servo)

    return servos


def stand(servos):
    moveInner(servos, 512)
    moveOuter(servos, STANDING_POS)


def sit(servos):
    moveAll(servos, 512)


def walk(servos):
    for _ in range(5):
        # Forward step
        moveServo(servos, 3, 400)
        time.sleep(0.5)
        moveServo(servos, 2, 300)
        moveServo(servos, 6, 700)

        time.sleep(0.5)
        moveServo(servos, 3, STANDING_POS)
        time.sleep(0.5)

        moveServo(servos, 1, 350)
        moveServo(servos, 5, 350)

        time.sleep(0.5)

        moveServo(servos, 2, 512)
        moveServo(servos, 6, 512)

        time.sleep(0.5)

        moveServo(servos, 1, STANDING_POS)
        moveServo(servos, 5, STANDING_POS)

        time.sleep(0.5)


def rotate(servos, rot="CW"):
    sit(servos)
    time.sleep(0.5)
    angle = 200 if rot == "CW" else 820
    moveInner(servos, angle)
    time.sleep(0.5)
    stand(servos)
    time.sleep(0.5)
    moveInner(servos, 512)


def flip(servos):
    # Move back legs outward
    moveServo(servos, 6, 824)
    moveServo(servos, 8, 200)
    time.sleep(0.5)

    # Extend back legs
    moveServo(servos, 5, 512)
    moveServo(servos, 7, 512)
    time.sleep(0.5)

    # Retract back legs
    moveServo(servos, 5, 200)
    moveServo(servos, 7, 200)
    time.sleep(0.5)

    # Flip forward legs
    moveServo(servos, 1, 724)
    moveServo(servos, 3, 724)
    time.sleep(0.5)

    # Move back legs inward
    moveServo(servos, 6, 512)
    moveServo(servos, 8, 512)
    time.sleep(0.5)

    # Flip back legs
    moveServo(servos, 5, 724)
    moveServo(servos, 7, 724)
    time.sleep(0.5)

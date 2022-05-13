import RPi.GPIO as GPIO
import random
GPIO.setwarnings(False)

from classes.ultrasonesensor import ultrasonesensor
from classes.motor import motor
import time


ultrasonesensor = ultrasonesensor(16)

randomint = random.randint(0,1)
def find_blik(distance, speed, motor1, motor2):
    e = 0
    motor1.drive(0)
    motor2.drive(0)
    if (randomint == 1):
        while ultrasonesensor.get_data() >= distance:
            e = ultrasonesensor.get_data()
            motor1.drive(-20)
            motor2.drive(20)
        while ultrasonesensor.get_data() <= e:
            f = ultrasonesensor.get_data()
            if f < e:
                e = f
            motor1.drive(-20)
            motor2.drive(20)
    else:
        while ultrasonesensor.get_data() >= distance:
            e = ultrasonesensor.get_data()
            motor1.drive(20)
            motor2.drive(-20)

        while ultrasonesensor.get_data() <= e:
            f = ultrasonesensor.get_data()
            if f < e:
                e = f
            motor1.drive(-20)
            motor2.drive(20)
    motor1.drive(speed)
    motor2.drive(speed)

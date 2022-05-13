import RPi.GPIO as GPIO
import random
GPIO.setwarnings(False)

from classes.ultrasonesensor import ultrasonesensor
from classes.motor import motor
import time


ultrasonesensor = ultrasonesensor(16)

randomint = random.randint(0,1)
def find_blik(distance, speed, motor1, motor2):
    if (randomint == 1):
        motor1.drive(10)
        motor2.drive(-10)
        if ultrasonesensor.get_distance() < distance:
            motor1.drive(speed)
            motor2.drive(speed)
    else:
        motor1.drive(-10)
        motor2.drive(10)
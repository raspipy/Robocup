import RPi.GPIO as GPIO
import random
GPIO.setwarnings(False)

from classes.ultrasonesensor import ultrasonesensor
from classes.lijnsensor import lijnsensor
from classes.motor import motor
import time
motor1 = motor([10,12,33,8])
motor2 = motor([35,37,32,8])

ultrasonesensor = ultrasonesensor(16)

randomint = random.random(0,1)

if (randomint == 1):
    motor1.drive(10)
    motor2.drive(-10)
else:
    motor1.drive(-10)
    motor2.drive(10)
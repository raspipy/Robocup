import RPi.GPIO as GPIO
import random
GPIO.setwarnings(False)

from classes.ultrasonesensor import ultrasonesensor
from classes.motor import motor
import time


ultrasonesensor = ultrasonesensor(16)

randomint = random.randint(0,1)
def find_blik(distance, speed, motor1, motor2):
    motor1.drive(0)
    motor2.drive(0)
    if (randomint == 1):
        while ultrasonesensor.get_data() >= distance:
            motor1.drive(-20)
            motor2.drive(20)
        motor1.drive(-20)
        motor2.drive(0)
        time.sleep(0.1)
        motor1.drive(0)
        motor2.drive(0)
    else:
        while ultrasonesensor.get_data() >= distance:
            motor1.drive(20)
            motor2.drive(-20)
        motor1.drive(0)
        motor2.drive(-20)
        time.sleep(0.1)
        motor1.drive(0)
        motor2.drive(0)

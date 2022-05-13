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
        #motor1.drive(10)
        #if ultrasonesensor.get_data() <= distance:
        print(ultrasonesensor.get_data())

        while ultrasonesensor.get_data() >= distance:
            motor1.drive(-20)
            print(ultrasonesensor.get_data())
            motor2.drive(20)
        motor1.drive(0)
        motor2.drive(0)

    
        #motor2.drive(-10)
    else:
       # motor1.drive(-10)
        #if ultrasonesensor.get_data() <= distance:
        print(ultrasonesensor.get_data())
        while ultrasonesensor.get_data() >= distance:
            motor1.drive(20)
            print(ultrasonesensor.get_data())
            motor2.drive(-20)
        motor1.drive(0)
        motor2.drive(0)

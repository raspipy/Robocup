import RPi.GPIO as GPIO
import random
GPIO.setwarnings(False)

from classes.json_loader import json_loader
from classes.ultrasonesensor import ultrasonesensor
from classes.motor import motor
import time



ultrasonesensor = ultrasonesensor(16)

randomint = random.randint(0,1)
def find_blik(distance, speed, motor1, motor2):
    e = 0
    motor1.drive(0)
    motor2.drive(0)
    if (json_loader("classes/calibratie_waarden.json").load(False, True) == 1):
        json_loader("classes/calibratie_waarden.json").write(0, False, True, 4)
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
        json_loader("classes/calibratie_waarden.json").write(1, False, True, 4)
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
    time.sleep(2)
    motor1.drive(0)
    motor2.drive(0)

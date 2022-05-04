import RPi.GPIO as GPIO
GPIO.setwarnings(False)

from classes.ultrasonesensor import ultrasonesensor
from classes.lijnsensor import lijnsensor
from classes.motor import motor
import time
motor1 = motor([10,12,33,8])
motor2 = motor([35,37,32,8])

ultrasonesensor = ultrasonesensor(16)
while ultrasonesensor.get_data() >= 20.0:
    motor1.drive(-0)
    motor2.drive(20)
while ultrasonesensor.get_data() >= 5.0:
    motor1.drive(20)
    motor2.drive(20)
motor1.drive(0)
motor2.drive(0)
GPIO.cleanup()
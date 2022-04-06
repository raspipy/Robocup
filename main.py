import RPi.GPIO as GPIO

from classes.lijnsensor import lijnsensor
from classes.motor import motor

GPIO.setwarnings(False)

lijnsensor = lijnsensor([11, 13, 15, 19, 21, 23, 29, 31])
print(lijnsensor.readData())

motor1 = motor([35,37,32,8])
while True:
    motor1.drive(0)

GPIO.cleanup()
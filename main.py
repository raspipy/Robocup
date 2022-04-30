#############################
#     importing libaries     #
#############################
import time
from classes.ultrasonesensor import ultrasonesensor
from classes.lijnsensor import lijnsensor
from classes.motor import motor
from classes.kleurensensor import kleurensensor
import RPi.GPIO as GPIO

#############################
#     variables             #
#############################

lijnsensor = lijnsensor([11, 13, 15, 19, 21, 23, 29, 31])
kleurensensoren = kleurensensor([40, 38, 36, 26], [22, 18])
motor1 = motor([35,37,32,8])
ultrasonesensor = ultrasonesensor(16)
GPIO.setwarnings(False)
GPIO.cleanup()

print(lijnsensor.get_data())
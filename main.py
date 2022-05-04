#############################
#     importing libaries     #
#############################
import time
from classes.ultrasonesensor import ultrasonesensor
from classes.lijnsensor import lijnsensor
from classes.motor import motor
from classes.kleurensensor import kleurensensor
import classes.json_loader as json_loader
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#############################
#     variables             #
#############################

lijnsensor = lijnsensor([11, 13, 15, 19, 21, 23, 29, 31])
kleurensensoren = kleurensensor([40, 38, 36, 26], [22, 18])
motor1 = motor([35,37,32,8])
ultrasonesensor = ultrasonesensor(16)
GPIO.setwarnings(False)

while True:
    print(str(lijnsensor.get_data()) + "\t" + str(lijnsensor.get_data_raw()))
    time.sleep(0.1)

GPIO.cleanup()
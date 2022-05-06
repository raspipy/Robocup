import time
from classes.ultrasonesensor import ultrasonesensor
from classes.lijnsensor import lijnsensor
from classes.motor import motor
from classes.kleurensensor import kleurensensor
import classes.json_loader as json_loader
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

lijnsensor = lijnsensor([11, 13, 15, 19, 21, 23, 29, 31])
kleurensensoren = kleurensensor([40, 38, 36, 26], [22, 18])
motor1 = motor([35,37,32,8], 10)
ultrasonesensor = ultrasonesensor(16)
GPIO.setwarnings(False)
class Drive_JJ:
    def __init__(self, input, base_speed):
        self.input = input
        self.base_speed = base_speed
    def follow_black_line(self):
        if lijnsensor.get_position() == 0:
            speed
            motor2.drive(0)
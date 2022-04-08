import RPi.GPIO as GPIO

from classes.lijnsensor import lijnsensor
from classes.motor import motor
from classes.kleurensensor import kleurensensor

GPIO.setwarnings(False)

lijnsensor = lijnsensor([11, 13, 15, 19, 21, 23, 29, 31])
print(lijnsensor.readData())

motor1 = motor([35,37,32,8])
kleurensensoren = kleurensensor([40, 38, 36, 26], [22, 18])

print(kleurensensoren.get_data())

while True:
    motor1.drive(50)

GPIO.cleanup()

import RPi.GPIO as GPIO
import time
import random
from classes.ultrasonesensor import ultrasonesensor
from classes.lijnsensor import lijnsensor
from classes.motor import motor
from classes.kleurensensor import kleurensensor

GPIO.setwarnings(False)

lijnsensor = lijnsensor([11, 13, 15, 19, 21, 23, 29, 31])
print(lijnsensor.readData())

motor1 = motor([35,37,32,8])
ultrasonesensor = ultrasonesensor(16)
kleurensensoren = kleurensensor([40, 38, 36, 26], [22, 18])

print(kleurensensoren.get_data_full())

while True:
    print(ultrasonesensor.get_data())
    time.sleep(0.1)
    motor1.drive(random.randint(0, 100))

GPIO.cleanup()

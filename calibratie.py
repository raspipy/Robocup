from classes.lijnsensor import lijnsensor
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
lijnsensor = lijnsensor([11, 13, 15, 19, 21, 23, 29, 31])

lijnsensor.get_data()
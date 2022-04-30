from classes.lijnsensor import lijnsensor
import RPi.GPIO as GPIO


lijnsensor = lijnsensor([11, 13, 15, 19, 21, 23, 29, 31])

lijnsensor.get_data()
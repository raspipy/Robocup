from classes.lijnsensor import lijnsensor
import RPi.GPIO as GPIO


GPIO.setwarnings(False)
lijnsensor = lijnsensor([11, 13, 15, 19, 21, 23, 29, 31])
data_raw = []
data = 0
for i in range(5):
    input("Zet op een ander plaats op het zwart")
    data_raw.append(lijnsensor.get_data())
for i in range(len(data_raw)):
    data = data + data_raw[i]
data = data / len(data_raw)


GPIO.cleanup()
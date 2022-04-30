from classes.lijnsensor import lijnsensor
import RPi.GPIO as GPIO


GPIO.setwarnings(False)
lijnsensor = lijnsensor([11, 13, 15, 19, 21, 23, 29, 31])
data_raw = []
data = [0,0,0,0,0,0,0,0]
for i in range(5):
    input("Zet op een ander plaats op het zwart")
    data_raw = lijnsensor.get_data()
    for y in range(8):
        data[i] += data_raw[i]
for i in range(8):
    data[i] = data[i] / 5
print(data)

GPIO.cleanup()
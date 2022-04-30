from classes.lijnsensor import lijnsensor
import RPi.GPIO as GPIO
import os

GPIO.setwarnings(False)
lijnsensor = lijnsensor([11, 13, 15, 19, 21, 23, 29, 31])
data_raw = []
data = [0,0,0,0,0,0,0,0]
for i in range(5):
    input("Zet op een ander plaats op het zwart")
    data_raw = lijnsensor.get_data()
    for y in range(8):
        data[y] += data_raw[y]
for i in range(8):
    data[i] = data[i] / 5
print(data)

data_raw = []
data_white = [0,0,0,0,0,0,0,0]

for i in range(5):
    input("Zet op een ander plaats op het wit!")
    data_raw = lijnsensor.get_data()
    for y in range(8):
        data_white[y] += data_raw[y]
for i in range(8):
    data_white[i] = data_white[i] / 5
full_data = [data,data_white]

def Save(Loc,Data):
    File = open(Loc,"w")
    if os.stat(Loc).st_size == 0:
        File.write(Data)
        File.close()
    else:
        File.seek(0)
        File.truncate()
        File.write(Data)
        File.close()
Save("classes/calibratie_waarden.txt",str(full_data))
GPIO.cleanup()
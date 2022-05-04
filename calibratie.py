#############################
#     importing libaries    #
#############################
from classes.lijnsensor import lijnsensor
import RPi.GPIO as GPIO
import os
import json
from classes.json_loader import json_loader

#############################
#     craete variabels      #
#############################
GPIO.setwarnings(False)
lijnsensor = lijnsensor([11, 13, 15, 19, 21, 23, 29, 31])
data_raw = []
data = [0,0,0,0,0,0,0,0]
data_white = [0,0,0,0,0,0,0,0]
#############################
#     calibration           #
#############################

#calibration for black color
for i in range(100):
    input("Zet op een ander plaats op het zwart")
    data_raw = lijnsensor.get_data_raw()
    for y in range(8):
        data[y] += data_raw[y]
    print(str(data_raw) + "\t" + str(data))
for i in range(8):
    data[i] = data[i] / 100
print(data)

#calibration for white
for i in range(5):
    input("Zet op een ander plaats op het wit!")
    data_raw = lijnsensor.get_data_raw()
    for y in range(8):
        data_white[y] += data_raw[y]
    print(str(data_raw) + "\t" + str(data))
for i in range(8):
    data_white[i] = data_white[i] / 5
print(data_white)
full_data = [data,data_white]

#############################
#     saving                #
#############################

json_loader("./classes/calibratie_waarden.json").write(full_data)

"""def Save(Loc,Data):
    with open(Loc,"w") as File:
        json.dump(Data,File)
        if os.stat(Loc).st_size == 0:
            File.write()
            File.close()
        else:
            File.seek(0)
            File.truncate()
            File.write(Data)
            File.close()
Save("classes/calibratie_waarden.txt",str(full_data))"""
GPIO.cleanup()
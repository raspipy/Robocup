#############################
#     importing libaries    #
#############################
from classes.lijnsensor import lijnsensor
import RPi.GPIO as GPIO
import os
import json
from classes.json_loader import json_loader
from classes.kleurensensor import kleurensensor

kleurensensor = kleurensensor([40, 38, 36, 26], [22, 18])

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
for i in range(5):
    input("Zet op een ander plaats op het zwart")
    data_raw = lijnsensor.get_data_raw()
    for b in range(100):
        for y in range(8):
            data[y] += data_raw[y]
    print(str(data_raw) + "\t" + str(data))
for i in range(8):
    data[i] = data[i] / 500
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

#############################
#     saving                #
#############################

full_data = [data,data_white]
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

####################--------------------------------------------------------------------------------------------------#################################################
groen_filter = [(0,0),(0,0),(0,0)]
rood_filter = [(0,0),(0,0),(0,0)]
clear_filter = [(0,0),(0,0),(0,0)]
blue_filter = [(0,0),(0,0),(0,0)]

for i in range(5):
    print("Plaats robot op het zwart")
    for y in range(5):
        kleurensensor.set_filter("Green")
        data = kleurensensor.get_data()
        groen_filter[0][0] += data[0]
        groen_filter[0][1] += data[1]
        kleurensensor.set_filter("Red")
        data = kleurensensor.get_data()
        rood_filter[0][0] += data[0]
        rood_filter[0][1] += data[1]
        kleurensensor.set_filter("Blue")
        data = kleurensensor.get_data()
        blue_filter[0][0] += data[0]
        blue_filter[0][1] += data[1]
        kleurensensor.set_filter("Clear")
        data = kleurensensor.get_data()
        clear_filter[0][0] += data[0]
        clear_filter[0][1] += data[1]
    groen_filter[0][0] /= 25
    groen_filter[0][1] /= 25
    rood_filter[0][0] /= 25
    rood_filter[0][1] /= 25
    blue_filter[0][0] /= 25
    blue_filter[0][1] /= 25
    clear_filter[0][0] /= 25
    clear_filter[0][1] /= 25
for i in range(5):
    print("Plaats robot op het groen")
    for y in range(5):
        kleurensensor.set_filter("Green")
        data = kleurensensor.get_data()
        groen_filter[1][0] += data[0]
        groen_filter[1][1] += data[1]
        kleurensensor.set_filter("Red")
        data = kleurensensor.get_data()
        rood_filter[1][0] += data[0]
        rood_filter[1][1] += data[1]
        kleurensensor.set_filter("Blue")
        data = kleurensensor.get_data()
        blue_filter[1][0] += data[0]
        blue_filter[1][1] += data[1]
        kleurensensor.set_filter("Clear")
        data = kleurensensor.get_data()
        clear_filter[1][0] += data[0]
        clear_filter[1][1] += data[1]

groen_filter[1][0] /= 25
groen_filter[1][1] /= 25
rood_filter[1][0] /= 25
rood_filter[1][1] /= 25
blue_filter[1][0] /= 25
blue_filter[1][1] /= 25
clear_filter[1][0] /= 25
clear_filter[1][1] /= 25
for i in range(5):
    print("Plaats robot op het geel")
    for y in range(5):
        kleurensensor.set_filter("Green")
        data = kleurensensor.get_data()
        groen_filter[2][0] += data[0]
        groen_filter[2][1] += data[1]
        kleurensensor.set_filter("Red")
        data = kleurensensor.get_data()
        rood_filter[2][0] += data[0]
        rood_filter[2][1] += data[1]
        kleurensensor.set_filter("Blue")
        data = kleurensensor.get_data()
        blue_filter[2][0] += data[0]
        blue_filter[2][1] += data[1]
        kleurensensor.set_filter("Clear")
        data = kleurensensor.get_data()
        clear_filter[2][0] += data[0]
        clear_filter[2][1] += data[1]
groen_filter[2][0] /= 25
groen_filter[2][1] /= 25
rood_filter[2][0] /= 25
rood_filter[2][1] /= 25
blue_filter[2][0] /= 25
blue_filter[2][1] /= 25
clear_filter[2][0] /= 25
clear_filter[2][1] /= 25







GPIO.cleanup()
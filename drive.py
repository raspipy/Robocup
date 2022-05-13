#############################
#     importing libaries    #
#############################
import time
from turtle import speed

from numpy import False_
from blik import find_blik
from classes.ultrasonesensor import ultrasonesensor
from classes.lijnsensor import lijnsensor
from classes.motor import motor
from classes.kleurensensor import kleurensensor
import classes.json_loader as json_loader
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#############################
#     intalize              #
#############################
lijnsensor = lijnsensor([11, 13, 15, 19, 21, 23, 29, 31])
kleurensensoren = kleurensensor([40, 38, 36, 26], [22, 18])
motor2 = motor([35,37,32,8], 11)
motor1 = motor([10,12,33,8], 11)
ultrasonesensor = ultrasonesensor(16)
basespeed = int(input("BaseSpeed: "))

speedMotor1 = 0
speedMotor2 = 0
#############################
#     main                  #
#############################
sensitivity = float(input("enter sensitivity: "))
enabled = True
main_loop = True
first_black = False
motor1.drive(basespeed)
motor2.drive(basespeed)
time.sleep(0.4)
while main_loop:
    position = lijnsensor.get_position()
    color1 = kleurensensoren.get_data()
    color2 = kleurensensoren.get_data()
    if color1[0] == "Geel" and color2[0] == "Geel":
        if color1[0] == "Geel" and color2[0] == "Geel" and color1[1] == "Geel" and color2[1] == "Geel":
            find_blik(10, basespeed, motor1, motor2)
            main_loop = False
            break
            
        if first_black == False:
            print("geel")
        while enabled:
            begin_tijd = time.time()
            color1 = kleurensensoren.get_data()
            if color1[0] == "Zwart" and first_black ==  False:
                motor1.drive(-20)
                motor2.drive(20)
                first_black = True
                time.sleep(0.4)
                motor1.drive(basespeed)
                motor2.drive(basespeed)
                time.sleep(0.25)
                enabled = False
                break
            if color1[0] == "Groen":
                motor1.drive(basespeed + 30)
                motor2.drive(0)
            #elif color1[0] == "Zwart" and time.time() - begin_tijd >= 2:
            #    motor1.drive(0)
            #    motor2.drive(basespeed + 30)
            #    time.sleep(0.5)
            else:
                motor2.drive(basespeed + 30)
                motor1.drive(0)
    
    speedMotor1 = basespeed + position * sensitivity
    speedMotor2 = basespeed - position * sensitivity
    motor1.drive(speedMotor1)
    motor2.drive(speedMotor2)   

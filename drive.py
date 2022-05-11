#############################
#     importing libaries    #
#############################
import time
from turtle import speed
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
motor2 = motor([35,37,32,8], 10)
motor1 = motor([10,12,33,8], 10)
ultrasonesensor = ultrasonesensor(16)
basespeed = int(input("BaseSpeed: "))

speedMotor1 = 0
speedMotor2 = 0
#############################
#     main                  #
#############################
sensitivity = float(input("enter sensitivity: "))

while True:
    position = lijnsensor.get_position()
    colors = kleurensensoren.get_data()
    if colors[0] =="Geel":
        print(colors)
        print("Found Shortcut")
        break
    speedMotor1 = basespeed + position * sensitivity
    speedMotor2 = basespeed - position * sensitivity
    motor1.drive(speedMotor1)
    motor2.drive(speedMotor2)

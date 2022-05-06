#############################
#     importing libaries    #
#############################
import time
from classes.ultrasonesensor import ultrasonesensor
from classes.lijnsensor import lijnsensor
from classes.motor import motor
from classes.kleurensensor import kleurensensor
import classes.json_loader as json_loader
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#############################
#     variables             #
#############################

lijnsensor = lijnsensor([11, 13, 15, 19, 21, 23, 29, 31])
kleurensensoren = kleurensensor([40, 38, 36, 26], [22, 18])
motor2 = motor([35,37,32,8])
motor1 = motor([10, 12, 33, 8])
ultrasonesensor = ultrasonesensor(16)
pos = 35
lastPos = 35
baseMotorSpeed = 20
minMotorSpeed = 10
maxMotorSpeed = 100
proportional = 0.75
lMotorSpeed = 0
rMotorSpeed = 0

def getPosition(data):
    teller = 0*data[0] + 10*data[1] + 20*data[2] + 30*data[3] + 40*data[4] + 50*data[5] + 60*data[6] + 70*data[7]
    noemer = data[0] + data[1] + data[2] + data[3] + data[4] + data[5] + data[6] + data[7]
    if noemer != 0:
        return teller / noemer - 35
    else:
        return None

while True:
    motor1.drive(10)
    motor2.drive(10)
#    pos = getPosition(lijnsensor.get_data())
#    if pos == None:
#        pos = lastPos
#    lMotorSpeed = baseMotorSpeed + pos*proportional
#    rMotorSpeed = baseMotorSpeed - pos*proportional
#    if lMotorSpeed != 0 and abs(lMotorSpeed) < minMotorSpeed:
#        lMotorSpeed = minMotorSpeed*lMotorSpeed/abs(lMotorSpeed)
#    if abs(lMotorSpeed) > maxMotorSpeed:
#        lMotorSpeed = maxMotorSpeed*lMotorSpeed/abs(lMotorSpeed)
#    if rMotorSpeed != 0 and abs(rMotorSpeed) < minMotorSpeed:
#        rMotorSpeed = minMotorSpeed*rMotorSpeed/abs(rMotorSpeed)
#    if abs(rMotorSpeed) > maxMotorSpeed:
#        rMotorSpeed = maxMotorSpeed*rMotorSpeed/abs(rMotorSpeed)
#    motor1.drive(lMotorSpeed)
#    motor2.drive(rMotorSpeed)
#    print(str(lijnsensor.get_data_raw()) + "\t" + str(lijnsensor.get_data()) + "\t" + str(int(lMotorSpeed)) + "\t" + str(pos) + "\t" + str(int(rMotorSpeed)))
#    lastPos = pos



GPIO.cleanup()

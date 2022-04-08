import RPi.GPIO as GPIO

from classes.lijnsensor import lijnsensor
from classes.motor import motor
from classes.kleurensensor import kleurensensor

<<<<<<< HEAD
#############################
#     variables             #
#############################

motor_pins = []
lijnsensor_pins = []
ultrasonesensor_pins = []
kleurensensor = [kleurensensor([], [])]
motor1 = motor([])
motor2 = motor([])
=======
GPIO.setwarnings(False)
>>>>>>> 3f555f9697d8bf1eb57f9071584d35607f412554

lijnsensor = lijnsensor([11, 13, 15, 19, 21, 23, 29, 31])
print(lijnsensor.readData())

<<<<<<< HEAD


invoer = input("Hou nu zwart onder de robot (een blad) en type iets en klik enter om verder te gaan: ")
zwart = invoer # kleurensensor.get_data_full()
invoer = input("Hou nu geel onder de robot (een blad) en type iets en klik enter om verder te gaan: ")
geel = invoer # kleurensensor.get_data_full()
invoer = input("Hou nu groen onder de robot (een blad) en type iets en klik enter om verder te gaan: ")
groen = invoer # kleurensensor.get_data_full()
=======
motor1 = motor([35,37,32,8])
kleurensensoren = kleurensensor([40, 38, 36, 26], [22, 18])
>>>>>>> 3f555f9697d8bf1eb57f9071584d35607f412554

print(kleurensensoren.get_data())

while True:
    motor1.drive(0)

GPIO.cleanup()

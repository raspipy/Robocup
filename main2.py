
#############################
#     importing libarys     #
#############################

from classes.lijnsensor import lijnsensor
from classes.ultrasonesensor import ultrasonesensor
from classes.motor import motor

#############################
#     variables             #
#############################

motor_pins = []
lijnsensor_pins = []
ultrasonesensor_pins = []
kleurensensor = []
motor1 = motor([])
motor2 = motor([])

#############################
#     intalize              #
#############################

invoer = input("Hou nu zwart onder de robot (een blad) en type iets en klik enter om verder te gaan: ")
zwart = invoer
invoer = input("Hou nu geel onder de robot (een blad) en type iets en klik enter om verder te gaan: ")
geel = invoer
invoer = input("Hou nu groen onder de robot (een blad) en type iets en klik enter om verder te gaan: ")
groen = invoer

#############################
#     driving               #
#############################


#############################
#           end             #
#############################
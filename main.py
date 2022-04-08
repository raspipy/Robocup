
#############################
#     importing libarys     #
#############################

from classes.lijnsensor import lijnsensor
from classes.ultrasonesensor import ultrasonesensor
from classes.motor import motor
from classes.kleurensensor import kleurensensor

#############################
#     variables             #
#############################

motor_pins = []
lijnsensor_pins = []
ultrasonesensor_pins = []
kleurensensor = [kleurensensor([], [])]
motor1 = motor([])
motor2 = motor([])

#############################
#     intalize              #
#############################



invoer = input("Hou nu zwart onder de robot (een blad) en type iets en klik enter om verder te gaan: ")
zwart = invoer # kleurensensor.get_data_full()
invoer = input("Hou nu geel onder de robot (een blad) en type iets en klik enter om verder te gaan: ")
geel = invoer # kleurensensor.get_data_full()
invoer = input("Hou nu groen onder de robot (een blad) en type iets en klik enter om verder te gaan: ")
groen = invoer # kleurensensor.get_data_full()

#############################
#     driving               #
#############################


#############################
#           end             #
#############################
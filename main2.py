
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
kleurensensor_pins_in = []
kleurensensor_pins_out = []

#############################
#     objects               #
#############################

lijnsensor = lijnsensor(lijnsensor_pins)

kleurensensor = kleurensensor(kleurensensor_pins_out,kleurensensor_pins_in)

motor1 = motor([])
motor2 = motor([])

#############################
#     intalize              #
#############################

invoer = input("Hou nu zwart onder de robot (een blad) en type iets en klik enter om verder te gaan: ")
zwart = kleurensensor.get_data_full()
invoer = input("Hou nu geel onder de robot (een blad) en type iets en klik enter om verder te gaan: ")
geel = kleurensensor.get_data_full()
invoer = input("Hou nu groen onder de robot (een blad) en type iets en klik enter om verder te gaan: ")
groen = kleurensensor.get_data_full()

#############################
#     driving               #
#############################



#############################
#           end             #
#############################
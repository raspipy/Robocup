from classes.ultrasonesensor import ultrasonesensor
from classes.lijnsensor import lijnsensor
from classes.motor import motor
import time

while ultrasonesensor.get_data() <= 20.0:
    print(ultrasonesensor.get_data())
    time.sleep(0.1)
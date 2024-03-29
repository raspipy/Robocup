import RPi.GPIO as GPIO
import time
from classes.json_loader import json_loader
GPIO.setmode(GPIO.BOARD) # Sets the GPIO mode to BOARD
class kleurensensor():
    #############################
    #     intalize              #
    #############################
    def __init__(self, out_pins, in_pins):
        self.out_pins = out_pins
        self.in_pins = in_pins
        
        for i in self.out_pins:
            GPIO.setup(i, GPIO.OUT)
        for i in self.in_pins:
            GPIO.setup(i, GPIO.IN)
        self.calibration = json_loader("classes/calibratie_waarden.json").load(True, False)
        print(self.calibration)
        GPIO.output(self.out_pins[0], GPIO.LOW)

        GPIO.output(self.out_pins[1], GPIO.HIGH)

        self.set_filter(self.calibration[0])

    #######################
    #     read color      #
    #######################
    def get_data_raw(self):
        # --- Sensor 1 --- #
        rising = GPIO.wait_for_edge(self.in_pins[0], GPIO.BOTH, timeout=100)
        if rising is None:
            print("Timeout occured")
            return self.get_data_full()
        begin_tijd = time.time_ns()
        falling = GPIO.wait_for_edge(self.in_pins[0], GPIO.BOTH, timeout=100)
        if falling is None:
            print("Timeout occured")
            return self.get_data_full()
        tijdsduur1 = int((time.time_ns() - begin_tijd)/1000)
        rising2 = GPIO.wait_for_edge(self.in_pins[1], GPIO.BOTH, timeout=100)
        if rising2 is None:
            print("Timeout occured")
            return self.get_data_full() 
        begin_tijd = time.time_ns()
        rising3 = GPIO.wait_for_edge(self.in_pins[1], GPIO.BOTH, timeout=100)
        if rising3 is None:
            print("Timeout occured")
            return self.get_data_full()
        tijdsduur2 = int((time.time_ns() - begin_tijd)/1000)
        return (tijdsduur1, tijdsduur2) # Return the result in a tuple

    def set_filter(self, color):
        if (color == "Red"):
            GPIO.output(self.out_pins[2], GPIO.LOW)
            GPIO.output(self.out_pins[3], GPIO.LOW)
            #print("filter op rood gezet")
        if (color == "Blue"):
            GPIO.output(self.out_pins[2], GPIO.LOW)
            GPIO.output(self.out_pins[3], GPIO.HIGH)
            #print("filter op blauw gezet")
        if (color == "Clear"):
            GPIO.output(self.out_pins[2], GPIO.HIGH)
            GPIO.output(self.out_pins[3], GPIO.LOW)
            #print("filter op clear gezet")
        if (color == "Green"):
            GPIO.output(self.out_pins[2], GPIO.HIGH)
            GPIO.output(self.out_pins[3], GPIO.HIGH)
            #print("filter op groen gezet")
    
    def get_data(self):
        data = self.get_data_raw()



        results = ["","", data]
        for i in range(2):
            if (abs(self.calibration[1][0][i] - data[i]) <= min(abs(self.calibration[1][1][i] - data[i]), abs(self.calibration[1][2][i] - data[i]))):
                results[1-i] = "Zwart"
            elif (abs(self.calibration[1][1][i] - data[i]) <= min(abs(self.calibration[1][0][i] - data[i]), abs(self.calibration[1][2][i] - data[i]))):
                results[1 -i] = "Groen"
            else:
                results[1 -i] = "Geel"
        return results
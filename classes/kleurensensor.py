import RPi.GPIO as GPIO
import time
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

        GPIO.output(self.out_pins[0], GPIO.LOW)

        GPIO.output(self.out_pins[1], GPIO.HIGH)

        GPIO.output(self.out_pins[2], GPIO.HIGH)

        GPIO.output(self.out_pins[3], GPIO.HIGH)

    #######################
    #     read color      #
    #######################
    def get_data(self):
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
        tijdsduur1 = time.time_ns() - begin_tijd
        rising2 = GPIO.wait_for_edge(self.in_pins[1], GPIO.BOTH, timeout=100)
        if rising2 is None:
            print("Timeout occured")
            return self.get_data_full() 
        begin_tijd = time.time_ns()
        rising3 = GPIO.wait_for_edge(self.in_pins[1], GPIO.BOTH, timeout=100)
        if rising3 is None:
            print("Timeout occured")
            return self.get_data_full()
        tijdsduur2 = time.time_ns() - begin_tijd
        return (tijdsduur1, tijdsduur2) # Return the result in a tuple

    def setfilter(self, color):
        if (color == "Red"):
            GPIO.output(self.out_pins[2], GPIO.LOW)
            GPIO.output(self.out_pins[3], GPIO.LOW)
        if (color == "Blue"):
            GPIO.output(self.out_pins[2], GPIO.LOW)
            GPIO.output(self.out_pins[3], GPIO.HIGH)
        if (color == "Clear"):
            GPIO.output(self.out_pins[2], GPIO.HIGH)
            GPIO.output(self.out_pins[3], GPIO.LOW)
        if (color == "Green"):
            GPIO.output(self.out_pins[2], GPIO.HIGH)
            GPIO.output(self.out_pins[3], GPIO.HIGH)
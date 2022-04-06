import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD) # Sets the GPIO mode to BOARD
class kleurensensor():
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

    def get_data(self):
        # --- Sensor 1 --- #

        GPIO.wait_for_edge(self.in_pins[0], GPIO.BOTH)

        begin_tijd = time.time_ns()

        GPIO.wait_for_edge(self.in_pins[0], GPIO.BOTH)

        tijdsduur1 = time.time_ns() - begin_tijd
        # --- Sensor 2 --- #

        GPIO.wait_for_edge(self.in_pins[1], GPIO.BOTH)

        begin_tijd = time.time_ns()
        GPIO.wait_for_edge(self.in_pins[1], GPIO.BOTH)

        tijdsduur2 = time.time_ns() - begin_tijd


        return (tijdsduur1, tijdsduur2) # Return the result in a tuple


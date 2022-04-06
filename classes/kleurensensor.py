import RPi.GPIO as GPIO
import time
GPIO.set_mode(GPIO.BOARD)
class kleurensensors():
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

        GPIO.wait_for_edge(self.in_pins[0], GPIO.BOTH)
        begin_tijd = time.time_ns()
        GPIO.wait_for_edge(self.in_pins[0], GPIO.BOTH)
        tijdsduur1 = time.time_ns() - begin_tijd
        GPIO.wait_for_edge(self.in_pins[1], GPIO.BOTH)
        begin_tijd = time.time_ns()
        GPIO.wait_for_edge(self.in_pins[1], GPIO.BOTH)
        tijdsduur2 = time.time_ns() - begin_tijd
        return (tijdsduur1, tijdsduur2)


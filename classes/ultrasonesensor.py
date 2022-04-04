import RPi.GPIO as GPIO
import time
class ultrasonesensor:
    def __init__(self, pin):
        self.pin = pin

        
    def get_data(self):
        # --- Setup --- 
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)
        time.sleep(2/1000000)
        GPIO.output(self.pin, GPIO.HIGH)
        time.sleep(5/1000000)
        GPIO.output(self.pin, GPIO.LOW)
        
        # --- Measurement --- 
        GPIO.setup(self.pin, GPIO.IN)
        while GPIO.input(self.pin) != 1:
            pass
        begin_tijd = time.time_ns()
        while GPIO.input(self.pin) != 0:
            pass
        eind_tijd = time.time_ns()
        return ((begin_tijd - eind_tijd)/ 2 * 34 /1000000)








        




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
        rising = GPIO.wait_for_edge(self.pin, GPIO.RISING, timeout=100)
        if rising is None:
            print("Timeout occured")
            return self.get_data()

        begin_tijd = time.time_ns()

        falling = GPIO.wait_for_edge(self.pin, GPIO.FALLING, timeout=100)
        if falling is None:
            print("Timeout occured")
            return self.get_data()
        
        eind_tijd = time.time_ns()

        return ((eind_tijd- begin_tijd)/ 299792458)








        




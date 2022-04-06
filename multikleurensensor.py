import RPi.GPIO as GPIO

class multicolor:

    def __init__(self, in1, in2, in3, in4, in5, in6, in7, in8, vcc, gnd):

    # --- Setup ---
        self.in1 = in1
        self.in2 = in2
        self.in3 = in3
        self.in4 = in4
        self.in5 = in5
        self.in6 = in6
        self.in7 = in7
        self.in8 = in8
        self.vcc = vcc
        self.gnd = gnd
        self.all_in = [in1, in2, in3, in4, in5, in6, in7, in8]
        
    # --- Setup ---

    def get_data(self):
        for i in range(self.all_in):
            GPIO.setup(i, GPIO.IN) # Zet de status van alle pinnen naar input
            
        

        """
        Ik weet niet hoe het verder ging, de pololu documentation was niet heel duidelijk
        Kunnen we hier later aan werken? D:
        
        """
        
        


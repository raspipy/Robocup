import RPi.GPIO as GPIO

class multikleurensensor:

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
        all_in = [in1, in2, in3, in4, in5, in6,in7, in8]

        print(all_in)
        
    # --- Setup ---

    def get_data(self):
        #for i in 
        pass

"""Gewoon even een kleine test of alles werkt :D"""
if __name__ == '__main__':
    multikleurensensor(40,2,3,4,5,9,7,8,9,10)
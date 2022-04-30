import RPi.GPIO as PI
import time

PI.setmode(PI.BOARD)

class lijnsensor:
    def __init__ (self, pins):
        self.pins = pins
        
    def get_data(self):
        for each in self.pins:
            PI.setup(each,PI.OUT)
            PI.output(each,1)
        time.sleep(0.00001)
        for each in self.pins:
            PI.setup(each,PI.IN)
        sum = 8
        resultaten = [0,0,0,0,0,0,0,0]
        beginTime = time.time_ns()
        while sum != 0:
            sum = 0
            for each in self.pins:
                sum += PI.input(each)
            for i in range(0,8):
                if PI.input(self.pins[i]) == 0  and resultaten[i] == 0:
                    resultaten[i] = (time.time_ns() - beginTime) / 1000
        return resultaten
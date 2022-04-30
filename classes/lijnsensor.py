import RPi.GPIO as PI
import time

PI.setmode(PI.BOARD)

class lijnsensor:
    def __init__ (self, pins):
        self.pins = pins
        PI.setup(7, PI.OUT)
        PI.output(7, PI.HIGH)
        
    def get_data_raw(self):
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
                    resultaten[i] = int((time.time_ns() - beginTime) / 1000)
        return resultaten


    def get_data(self):
        calibration = [[114.2, 227.6, 156.4, 472.6, 265.2, 176.6, 188.0, 178.4], [127.6, 208.6, 158.4, 473.8, 267.2, 178.4, 189.8, 201.0]]
        raw_data = self.get_data_raw()
        result = []
        for i in range(0,8):
            if abs(raw_data[i] - calibration[0][i]) < abs(raw_data[i] - calibration[1][i]):
                result.append(1)
            else:
                result.append(0)
        return result

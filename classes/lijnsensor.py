import RPi.GPIO as PI
import time
import json
from classes.json_loader import json_loader
PI.setmode(PI.BOARD)

class lijnsensor:
    def __init__ (self, pins):
        self.pins = pins
        PI.setup(7, PI.OUT)
        PI.output(7, PI.HIGH)

        self.calibration = json_loader("classes/calibratie_waarden.json").load()
        
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
                if PI.input(self.pins[i]) == 0  and resultaten[7-i] == 0:
                    resultaten[7-i] = int((time.time_ns() - beginTime) / 1000)
        return resultaten

    def get_data(self):
        raw_data = self.get_data_raw()
        result = []
        #print(self.calibration)
        for i in range(0,8):
            if abs(raw_data[i] - self.calibration[0][i]) < abs(raw_data[i] - self.calibration[1][i]):
                result.append(1)
                #print(abs(raw_data[i] - self.calibration[0][i]))
            else:
                result.append(0)
        return result

    def get_position(self):
        values = self.get_data()
        teller = 0*values[0] + 10*values[1] + 20*values[2] + 30*values[3] + 40*values[3] +50*values[4]+ 60*values[5] +70*values[6] +80*values[7]
        noemer = values[0] + values[1] + values[2] + values[3] + values[4] + values[5] + values[6] + values[7]
        if noemer != 0:
            return teller/noemer - 35
        else:
            return None

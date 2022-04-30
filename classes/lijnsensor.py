import RPi.GPIO as PI
import time

from main import FileLoc



PI.setmode(PI.BOARD)

class lijnsensor:

    def __init__ (self, pins):
        self.pins = pins
        PI.setup(7, PI.OUT)
        PI.output(7, PI.HIGH)
        FileLoc = "classes/calibratie.txt"
        File = open(FileLoc,"r")
        FileData = File.readline(1)
        File.close
        self.calibration = FileData
        
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
        raw_data = self.get_data_raw()
        result = []
        for i in range(0,8):
            if abs(raw_data[i] - self.calibration[0][i]) < abs(raw_data[i] - self.calibration[1][i]):
                result.append(1)
            else:
                result.append(0)
        return result

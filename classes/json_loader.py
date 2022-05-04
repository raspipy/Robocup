#############################
#     importing libaries    #
#############################
import json
import os


class json_loader:
    def __init__(self, file):
        self.file = file

    def load(self):
        #load a .json file
        f = open(self.file,"r")
        data = json.loads(f.read())
        result_black = None
        for i in data["black"]:
            result_black = data["black"][0]
            print(result_black)
        for i in data["white"]:
            result_white = data["white"][0]
        results = [[],[]]
        for i in result_black:
            results[0].append(result_black[i])
        for i in result_white:
            results[1].append(result_white[i])
        f.close()
        return results        

    def write(self, data):
        #write data to .json file
        with open(self.file,"r+") as f:
            json_data = json.loads(f.read())

            for i in range(1,9):
                json_data["black"][0]['%d'%(i)] = data[0][i - 1]
            for i in range(1,9):
                json_data["white"][0]['%d'%(i)] = data[1][i - 1]
            if os.stat(self.file).st_size == 0:
                json.dump(json_data, f)

            else: #when fails
                f.seek(0)
                f.truncate()
                json.dump(json_data, f, indent=4)
            f.close()
        return 0

if __name__ == "__main__":
    json_loader("classes/calibratie_waarden.json").load()
#############################
#     importing libaries    #
#############################
import json
import os


class json_loader:
    def __init__(self, file):
        self.file = file

    def load(self, kleurensensor=bool()):
        #load a .json file
        f = open(self.file,"r")
        data = json.loads(f.read())
        if kleurensensor:
            results = []
            b = -1
            ###### Takes the green_filter data out of the JSON file ######
            for i in data["filters"]:
                b += 1
                result_green = data["filters"][b]
                print(result_green)
            for i in result_green: # Turns the raw data into a list
                results.append(result_green[i])
            b = -1
            return results
        else:
            result_black = None
            for i in data["black"]:
                result_black = data["black"][0]
            for i in data["white"]:
                result_white = data["white"][0]
            results = [[],[]]
            for i in result_black:
                results[0].append(result_black[i])
            for i in result_white:
                results[1].append(result_white[i])
            f.close()
            return results        

    def write(self, data, kleurensensor, indent ):
        #write data to .json file
        with open(self.file,"r+") as f:
            json_data = json.loads(f.read())
            if kleurensensor:
                b = 0
                for i in json_data["filters"][0]:
                    json_data["filters"][0][i] = data[b]
                    b += 1
                b = 0

            else:        
                for i in range(1,9):
                    json_data["black"][0]['%d'%(i)] = data[0][i - 1]
                for i in range(1,9):
                    json_data["white"][0]['%d'%(i)] = data[1][i - 1]
            if os.stat(self.file).st_size == 0:
                pass
                json.dump(json_data, f)

            else: #when fails
                f.seek(0)
                f.truncate()
                json.dump(json_data, f, indent=indent)
            f.close()
        return 0


if __name__ == "__main__":
    print(json_loader("classes/calibratie_waarden.json").load(True))
    json_loader("classes/calibratie_waarden.json").write([(10,10,10),(10,40, 10),(10,10, 10),(10,10, 10)],True, 2)

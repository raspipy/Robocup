from classes.kleurensensor import kleurensensor
import time


kleurensensor = kleurensensor([40, 38, 36, 26], [22, 18])

while True:
    print(str(kleurensensor.get_data()) + '\t' + str(kleurensensor.get_data_raw()))
    time.sleep(0.25)

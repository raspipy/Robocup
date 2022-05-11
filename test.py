from classes.kleurensensor import kleurensensor
import time


kleurensensor = kleurensensor([40, 38, 36, 26], [22, 18])

while True:
    print(kleurensensor.get_data())
    time.sleep(0.25)

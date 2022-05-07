from classes.kleurensensor import kleurensensor

kleurensensor = kleurensensor([40, 38, 36, 26], [22, 18])
groen_filter = [(0,0),(0,0),(0,0)]
rood_filter = [(0,0),(0,0),(0,0)]
clear_filter = [(0,0),(0,0),(0,0)]
blue_filter = [(0,0),(0,0),(0,0)]

for i in range(5):
    print("Plaats robot op het zwart")
    for y in range(5):
        kleurensensor.set_filter("Green")
        data = kleurensensor.get_data()
        groen_filter[0][0] += data[0]
        groen_filter[0][1] += data[1]
        kleurensensor.set_filter("Red")
        data = kleurensensor.get_data()
        rood_filter[0][0] += data[0]
        rood_filter[0][1] += data[1]
        kleurensensor.set_filter("Blue")
        data = kleurensensor.get_data()
        blue_filter[0][0] += data[0]
        blue_filter[0][1] += data[1]
        kleurensensor.set_filter("Clear")
        data = kleurensensor.get_data()
        clear_filter[0][0] += data[0]
        clear_filter[0][1] += data[1]
    groen_filter[0][0] /= 25
    groen_filter[0][1] /= 25
    rood_filter[0][0] /= 25
    rood_filter[0][1] /= 25
    blue_filter[0][0] /= 25
    blue_filter[0][1] /= 25
    clear_filter[0][0] /= 25
    clear_filter[0][1] /= 25
for i in range(5):
    print("Plaats robot op het groen")
    for y in range(5):
        kleurensensor.set_filter("Green")
        data = kleurensensor.get_data()
        groen_filter[1][0] += data[0]
        groen_filter[1][1] += data[1]
        kleurensensor.set_filter("Red")
        data = kleurensensor.get_data()
        rood_filter[1][0] += data[0]
        rood_filter[1][1] += data[1]
        kleurensensor.set_filter("Blue")
        data = kleurensensor.get_data()
        blue_filter[1][0] += data[0]
        blue_filter[1][1] += data[1]
        kleurensensor.set_filter("Clear")
        data = kleurensensor.get_data()
        clear_filter[1][0] += data[0]
        clear_filter[1][1] += data[1]
groen_filter[1][0] /= 25
groen_filter[1][1] /= 25
rood_filter[1][0] /= 25
rood_filter[1][1] /= 25
blue_filter[1][0] /= 25
blue_filter[1][1] /= 25
clear_filter[1][0] /= 25
clear_filter[1][1] /= 25
for i in range(5):
    print("Plaats robot op het geel")
    for y in range(5):
        kleurensensor.set_filter("Green")
        data = kleurensensor.get_data()
        groen_filter[2][0] += data[0]
        groen_filter[2][1] += data[1]
        kleurensensor.set_filter("Red")
        data = kleurensensor.get_data()
        rood_filter[2][0] += data[0]
        rood_filter[2][1] += data[1]
        kleurensensor.set_filter("Blue")
        data = kleurensensor.get_data()
        blue_filter[2][0] += data[0]
        blue_filter[2][1] += data[1]
        kleurensensor.set_filter("Clear")
        data = kleurensensor.get_data()
        clear_filter[2][0] += data[0]
        clear_filter[2][1] += data[1]
groen_filter[2][0] /= 25
groen_filter[2][1] /= 25
rood_filter[2][0] /= 25
rood_filter[2][1] /= 25
blue_filter[2][0] /= 25
blue_filter[2][1] /= 25
clear_filter[2][0] /= 25
clear_filter[2][1] /= 25


    
    



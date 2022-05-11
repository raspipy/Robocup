from classes.kleurensensor import kleurensensor
import os
import json
from classes.json_loader import json_loader

kleurensensor = kleurensensor([40, 38, 36, 26], [22, 18])
groen_filter = [[0,0],[0,0],[0,0]]
rood_filter = [[0,0],[0,0],[0,0]]
clear_filter = [[0,0],[0,0],[0,0]]
blue_filter = [[0,0],[0,0],[0,0]]
verschil_groen_filter = [[0,0],[0,0],[0,0]]
verschil_rood_filter = [[0,0],[0,0],[0,0]]
verschil_clear_filter = [[0,0],[0,0],[0,0]]
verschil_blue_filter = [[0,0],[0,0],[0,0]]
possible_results = ["Red","Green","Blue","Clear"]
texts = ["plaats de kleurensensors op het zwart","plaats de kleurensensors op het groen","plaats de kleurensensors op het geel"]
for i in range(0,3):
    for j in range(5):
        input(texts[i])
        for y in range(5):
            kleurensensor.set_filter("Green")
            data = kleurensensor.get_data()
            groen_filter[i][0] += data[0]
            groen_filter[i][1] += data[1]
            kleurensensor.set_filter("Red")
            data = kleurensensor.get_data()
            rood_filter[i][0] += data[0]
            rood_filter[i][1] += data[1]
            kleurensensor.set_filter("Blue")
            data = kleurensensor.get_data()
            blue_filter[i][0] += data[0]
            blue_filter[i][1] += data[1]
            kleurensensor.set_filter("Clear")
            data = kleurensensor.get_data()
            clear_filter[i][0] += data[0]
            clear_filter[i][1] += data[1]
        groen_filter[i][0] //= 25
        groen_filter[i][1] //= 25
        rood_filter[i][0] //= 25
        rood_filter[i][1] //= 25
        blue_filter[i][0] //= 25
        blue_filter[i][1] //= 25
        clear_filter[i][0] //= 25
        clear_filter[i][1] //= 25

verschil_groen_filter[0] = min(abs(groen_filter[1][0] - groen_filter[0][0]), abs(groen_filter[1][1] - groen_filter[0][1]))
verschil_groen_filter[1] = min(abs(groen_filter[2][0] - groen_filter[1][0]), abs(groen_filter[2][1] - groen_filter[1][1]))
verschil_groen_filter[2] = min(abs(groen_filter[2][0] - groen_filter[0][0]), abs(groen_filter[2][1] - groen_filter[0][1]))

verschil_rood_filter[0] = min(abs(rood_filter[1][0] - rood_filter[0][0]), abs(rood_filter[1][1] - rood_filter[0][1]))
verschil_rood_filter[1] = min(abs(rood_filter[2][0] - rood_filter[1][0]), abs(rood_filter[2][1] - rood_filter[1][1]))
verschil_rood_filter[2] = min(abs(rood_filter[2][0] - rood_filter[0][0]), abs(rood_filter[2][1] - rood_filter[0][1]))

verschil_blue_filter[0] = min(abs(blue_filter[1][0] - blue_filter[0][0]), abs(blue_filter[1][1] - blue_filter[0][1]))
verschil_blue_filter[1] = min(abs(blue_filter[2][0] - blue_filter[1][0]), abs(blue_filter[2][1] - blue_filter[1][1]))
verschil_blue_filter[2] = min(abs(blue_filter[2][0] - blue_filter[0][0]), abs(blue_filter[2][1] - blue_filter[0][1]))

verschil_clear_filter[0] = min(abs(clear_filter[1][0] - clear_filter[0][0]), abs(clear_filter[1][1] - clear_filter[0][1]))
verschil_clear_filter[1] = min(abs(clear_filter[2][0] - clear_filter[1][0]), abs(clear_filter[2][1] - clear_filter[1][1]))
verschil_clear_filter[2] = min(abs(clear_filter[2][0] - clear_filter[0][0]), abs(clear_filter[2][1] - clear_filter[0][1]))

minimale_verschillen = [
    min(verschil_rood_filter),
    min(verschil_groen_filter),
    min(verschil_blue_filter),
    min(verschil_clear_filter)
]
Max = max(minimale_verschillen)

gemiddeldes = [rood_filter, groen_filter, blue_filter, clear_filter]

full_data = [
    possible_results[minimale_verschillen.index(Max)],
    gemiddeldes[minimale_verschillen.index(Max)]
    ]


print(full_data)
json_loader("classes/calibratie_waarden.json").write(full_data, True, 4)

print("\n\t\t\tZWART\t\t\tGROEN\t\t\tGEEL")
print("Rode filter\t\t" + str(rood_filter[0]) + "\t\t" + str(rood_filter[1]) + "\t\t" + str(rood_filter[2]))
print("Groene filter\t\t" + str(groen_filter[0]) + "\t\t" + str(groen_filter[1]) + "\t\t" + str(groen_filter[2]))
print("Blauwe filter\t\t" + str(blue_filter[0]) + "\t\t" + str(blue_filter[1]) + "\t\t" + str(blue_filter[2]))
print("Clear filter\t\t" + str(clear_filter[0]) + "\t\t" + str(clear_filter[1]) + "\t\t" + str(clear_filter[2]) + "\n")

print("\n\t\t\tZWART-GROEN\t\tGROEN-GEEL\t\tZWART-GEEL")
print("Rode filter\t\t" + str([abs(rood_filter[1][0] - rood_filter[0][0]), abs(rood_filter[1][1] - rood_filter[0][1])])
    + "\t\t" + str([abs(rood_filter[2][0] - rood_filter[1][0]), abs(rood_filter[2][1] - rood_filter[1][1])])
    + "\t\t" + str([abs(rood_filter[2][0] - rood_filter[0][0]), abs(rood_filter[2][1] - rood_filter[0][1])]))
print("Groen filter\t\t" + str([abs(groen_filter[1][0] - groen_filter[0][0]), abs(groen_filter[1][1] - groen_filter[0][1])])
    + "\t\t" + str([abs(groen_filter[2][0] - groen_filter[1][0]), abs(groen_filter[2][1] - groen_filter[1][1])])
    + "\t\t" + str([abs(groen_filter[2][0] - groen_filter[0][0]), abs(groen_filter[2][1] - groen_filter[0][1])]))
print("Blauwe filter\t\t" + str([abs(blue_filter[1][0] - blue_filter[0][0]), abs(blue_filter[1][1] - blue_filter[0][1])])
    + "\t\t" + str([abs(blue_filter[2][0] - blue_filter[1][0]), abs(blue_filter[2][1] - blue_filter[1][1])])
    + "\t\t\t" + str([abs(blue_filter[2][0] - blue_filter[0][0]), abs(blue_filter[2][1] - blue_filter[0][1])]))
print("Clear filter\t\t" + str([abs(clear_filter[1][0] - clear_filter[0][0]), abs(clear_filter[1][1] - clear_filter[0][1])])
    + "\t\t" + str([abs(clear_filter[2][0] - clear_filter[1][0]), abs(clear_filter[2][1] - clear_filter[1][1])])
    + "\t\t\t" + str([abs(clear_filter[2][0] - clear_filter[0][0]), abs(clear_filter[2][1] - clear_filter[0][1])]))

print("\n\t\t\tmin(ZWART-GROEN)\tmin(GROEN-GEEL)\t\tmin(ZWART-GEEL)")
print("Rode filter\t\t" + str(min([abs(rood_filter[1][0] - rood_filter[0][0]), abs(rood_filter[1][1] - rood_filter[0][1])]))
    + "\t\t\t" + str(min([abs(rood_filter[2][0] - rood_filter[1][0]), abs(rood_filter[2][1] - rood_filter[1][1])]))
    + "\t\t\t" + str(min([abs(rood_filter[2][0] - rood_filter[0][0]), abs(rood_filter[2][1] - rood_filter[0][1])])))
print("Groen filter\t\t" + str(min([abs(groen_filter[1][0] - groen_filter[0][0]), abs(groen_filter[1][1] - groen_filter[0][1])]))
    + "\t\t\t" + str(min([abs(groen_filter[2][0] - groen_filter[1][0]), abs(groen_filter[2][1] - groen_filter[1][1])]))
    + "\t\t\t" + str(min([abs(groen_filter[2][0] - groen_filter[0][0]), abs(groen_filter[2][1] - groen_filter[0][1])])))
print("Blauwe filter\t\t" + str(min([abs(blue_filter[1][0] - blue_filter[0][0]), abs(blue_filter[1][1] - blue_filter[0][1])]))
    + "\t\t\t" + str(min([abs(blue_filter[2][0] - blue_filter[1][0]), abs(blue_filter[2][1] - blue_filter[1][1])]))
    + "\t\t\t" + str(min([abs(blue_filter[2][0] - blue_filter[0][0]), abs(blue_filter[2][1] - blue_filter[0][1])])))
print("Clear filter\t\t" + str(min([abs(clear_filter[1][0] - clear_filter[0][0]), abs(clear_filter[1][1] - clear_filter[0][1])]))
    + "\t\t\t" + str(min([abs(clear_filter[2][0] - clear_filter[1][0]), abs(clear_filter[2][1] - clear_filter[1][1])]))
    + "\t\t\t" + str(min([abs(clear_filter[2][0] - clear_filter[0][0]), abs(clear_filter[2][1] - clear_filter[0][1])])))

print("\n\t\t\tminimale verschillen")
print("Rode filter\t\t" + str(min([min([abs(rood_filter[1][0] - rood_filter[0][0]), abs(rood_filter[1][1] - rood_filter[0][1])]),
    min([abs(rood_filter[2][0] - rood_filter[1][0]), abs(rood_filter[2][1] - rood_filter[1][1])]),
    min([abs(rood_filter[2][0] - rood_filter[0][0]), abs(rood_filter[2][1] - rood_filter[0][1])])])))
print("Groene filter\t\t" + str(min([min([abs(groen_filter[1][0] - groen_filter[0][0]), abs(groen_filter[1][1] - groen_filter[0][1])]),
    min([abs(groen_filter[2][0] - groen_filter[1][0]), abs(groen_filter[2][1] - groen_filter[1][1])]),
    min([abs(groen_filter[2][0] - groen_filter[0][0]), abs(groen_filter[2][1] - groen_filter[0][1])])])))
print("Blauwe filter\t\t" + str(min([min([abs(blue_filter[1][0] - blue_filter[0][0]), abs(blue_filter[1][1] - blue_filter[0][1])]),
    min([abs(blue_filter[2][0] - blue_filter[1][0]), abs(blue_filter[2][1] - blue_filter[1][1])]),
    min([abs(blue_filter[2][0] - blue_filter[0][0]), abs(blue_filter[2][1] - blue_filter[0][1])])])))
print("Clear filter\t\t" + str(min([min([abs(clear_filter[1][0] - clear_filter[0][0]), abs(clear_filter[1][1] - clear_filter[0][1])]),
    min([abs(clear_filter[2][0] - clear_filter[1][0]), abs(clear_filter[2][1] - clear_filter[1][1])]),
    min([abs(clear_filter[2][0] - clear_filter[0][0]), abs(clear_filter[2][1] - clear_filter[0][1])])])))

print("\nmax(minimale verschillen):\t" + str(max([min([min([abs(rood_filter[1][0] - rood_filter[0][0]), abs(rood_filter[1][1] - rood_filter[0][1])]),
    min([abs(rood_filter[2][0] - rood_filter[1][0]), abs(rood_filter[2][1] - rood_filter[1][1])]),
    min([abs(rood_filter[2][0] - rood_filter[0][0]), abs(rood_filter[2][1] - rood_filter[0][1])])]),
    min([min([abs(groen_filter[1][0] - groen_filter[0][0]), abs(groen_filter[1][1] - groen_filter[0][1])]),
    min([abs(groen_filter[2][0] - groen_filter[1][0]), abs(groen_filter[2][1] - groen_filter[1][1])]),
    min([abs(groen_filter[2][0] - groen_filter[0][0]), abs(groen_filter[2][1] - groen_filter[0][1])])]),
    min([min([abs(blue_filter[1][0] - blue_filter[0][0]), abs(blue_filter[1][1] - blue_filter[0][1])]),
    min([abs(blue_filter[2][0] - blue_filter[1][0]), abs(blue_filter[2][1] - blue_filter[1][1])]),
    min([abs(blue_filter[2][0] - blue_filter[0][0]), abs(blue_filter[2][1] - blue_filter[0][1])])]),
    min([min([abs(clear_filter[1][0] - clear_filter[0][0]), abs(clear_filter[1][1] - clear_filter[0][1])]),
    min([abs(clear_filter[2][0] - clear_filter[1][0]), abs(clear_filter[2][1] - clear_filter[1][1])]),
    min([abs(clear_filter[2][0] - clear_filter[0][0]), abs(clear_filter[2][1] - clear_filter[0][1])])])])))

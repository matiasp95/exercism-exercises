COLORS_T = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
METRIC = ["","kilo", "mega",  "giga"]
def label(colors):
    resistor = value(colors)
    zeros = COLORS_T.index(colors[2])
    total = str(resistor) + "0"*zeros
    k = total.count("0")
    r = 0
    while(k>=3):
        r+=1
        total = total[:-3]
        k -= 3
    return total + " " + METRIC[r] + "ohms"
def value(colors):
    return int(str(COLORS_T.index(colors[0])) + str(COLORS_T.index(colors[1])))

print(label(["blue", "green", "yellow", "orange"]))
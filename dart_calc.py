import math
def score(x, y):
    ten_squared = 10
    five_squared = 5
    one_squared = 1
    h = math.sqrt(x**2 + y**2)
    if(h<=one_squared):
        return 10
    if(h<=five_squared):
        return 5
    if(h<=ten_squared):
        return 1
    return 0

print(score(0.5,-4.0))
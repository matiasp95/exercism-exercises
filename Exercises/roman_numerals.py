import time
pairs = [(1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),]
def roman(number):

    ret = ""
    for i,r in pairs:
        while number >= i:
            ret += r
            number-=i
    return ret

start = time.time()
print(roman(232))
end = time.time()
print(end-start)


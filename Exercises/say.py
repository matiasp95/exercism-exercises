ONES = ["", "one", "two","three", "four", "five", "six", "seven", "eight", "nine"]
SPECIAL = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen"]
TENS = ["twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
REST = ["","thousand", "million", "billion"]
def say(number):
    x = str(number)
    temp = len(x)//3 +1 if len(x)%3 != 0 else len(x)//3
    x = x.rjust(3*temp,"0")
    if number < 0:
        raise ValueError("input out of range")
    if number >= 1000000000000:
        raise ValueError("input out of range")
    if number == 0:
        return "zero"
    if len(x) == 1:
        return two(number)
    if len(x) == 2:
        return two(number)
    s = ""
    j = temp -1
    for i in range(0, len(x), 3):
        s += three(int(x[i])) + " " + two(int(x[i+1:i+3])) if (int(x[i:i+3])%100 != 0) else three(int(x[i]))
        s += " " + REST[j] if (int(x[i:i+3]) != 0) else ""
        j-= 1
    return s.strip()

def three(number):
    if(number == 0):
        return ""
    r =" " +ONES[number] + " " + "hundred"
    return r


def two(number):
    if number == 0:
        return ""
    if number <= 9:
        return one(number)
    if 10 <= number <= 15:
        return SPECIAL[number%10]
    if 16 <= number <= 19:
        return ONES[number%10] + "teen"
    if 20 <= number <= 99:
        return TENS[number//10-2] + "-" + one(number%10) if number%10 != 0 else TENS[number//10-2]
    
    
def one(number):
    if number == 0:
        return ""
    if number <= 9:
        return ONES[number]

print(say(1000000))

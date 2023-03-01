def rebase(input_base, digits, output_base):
    if(not all([0 <= d < input_base for d in digits])):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    x = to_decimal(digits, input_base)
    l = []
    base = output_base
    while(x >= 1):
        l.insert(0,x%base)
        x//=base
    if(len(l) == 0):
        return [0]
    return l    
def to_decimal(digits, input_base):
    l = len(digits)-1
    x = 0
    for i in range(len(digits)):
        pos = l-i
        x+=digits[i]*(input_base**pos)
    return x

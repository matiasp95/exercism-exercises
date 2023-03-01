def factors(value):
    if value <= 1:
        return []
    i = 2
    x = []
    # If i is greater than the square root of value, then value cannot be divisible by any number greater than i
    while(i**2 <= value):
        if(value%i != 0):
            i+=1
        else:
        #Append if divisible by i, and don't increment since it still can be divisible by i
            value//=i
            x.append(i)
    #If exit and greater than 1, this is also a prime and a factor
    if value>1:
        x.append(value)
    return x
    

print(factors(93819012551))
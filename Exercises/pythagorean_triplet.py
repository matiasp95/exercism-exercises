
import math


def triplets_with_sum(number):
    triplets = set()
    facts = factors(number//2) 
    for m in facts:
        for k in facts:
            n = number/(2*k*m) - m
            if n > 0 and n%1==0 and (m + n)%2==1 and m > n:
                a = int(k * (m*m - n*n))
                b = int(2*k*m*n)
                c = int(k*(m*m +n*n))
                triple= [a,b,c]
                triple.sort()
                triplets.add(tuple(triple))
    
    return [list(t) for t in triplets]
def factors(number):
    return [fac for fac in range(1, number+1) if number%fac==0]



def fibo_method(number):
    for i in range(1, int(number/3)):
        n = (i+1)/2
        a = math.sqrt(i)
        b = n-1
        c = n
        if a**2 + b**2 == c**2 and a+b+c == number:
            return [a,b,c]
        
print(triplets_with_sum(1000))
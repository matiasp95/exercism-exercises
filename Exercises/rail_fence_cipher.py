import pprint
def encode(message, rails):
    x = []
    for i in range(rails):
        x.append([])
    temp = list(message)
    temp = temp[::-1]
    i = 0
    f = 0
    for m in range(len(message)):
        x[i].append(m)
        if(i == rails -1):
            f = 1
        if(i == 0):
            f = 0
        i+= 1 if f == 0 else -1
    ret = flatten(x)
    s = ""
    for i in ret:
        s += message[i]
    return s

def decode(encoded_message, rails):
    x = []
    for i in range(rails):
        x.append([])
    i = 0
    f = 0
    s = ""
    for m in range(len(encoded_message)):
        x[i].append(m)
        if(i == rails -1):
            f = 1
        if(i == 0):
            f = 0
        i+= 1 if f == 0 else -1
    flat = flatten(x)
    s = [0]*len(encoded_message)
    for m in range(len(flat)):
        s[flat[m]] = encoded_message[m]
    return "".join(s)

def flatten(iterable):
    x = []
    for i in iterable:
        if(type(i) != list):
            x.extend((i,))
        else:
            x.extend(flatten(i))
    while(None in x):
        x.remove(None)
    return x

print("#"*50)

##################################################

def fence_pattern(rails, message_size):
    r = 2 * (rails - 1)
    x = []
    for z in range(message_size):
        if (z % r) < rails:
            x.append(((z % r),z))
        else:
            x.append((r - (z % r),z))    
    return sorted(x)

def encode_t(msg, rails):
    s = ""
    for _,i in fence_pattern(rails, len(msg)):
        s+= msg[i]
    return s

def decode_t(msg, rails):
    xx = zip(fence_pattern(rails, len(msg)), msg)
    return ''.join(ch for _, ch in sorted(xx, key=lambda i: i[0][1]))

from itertools import cycle
def rail_pattern(n):
    r = list(range(n))
    return cycle(r + r[-2:0:-1])
def encode(plaintext, rails):
    p = rail_pattern(rails)
    # this relies on key being called in order, guaranteed?
    return ''.join(sorted(plaintext, key=lambda i: next(p)))

print(encode("EXERCISES",4))
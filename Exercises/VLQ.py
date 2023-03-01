import math
asddd = 0xFF000000
def _get_hex_in_binary(hexnum, bits):
    s = str(bin(hexnum))[2:]
    x = bits
    return s.zfill(x)

s = _get_hex_in_binary(asddd, 64)

def _get_number_of_seven_bytes(hexnum):
    n_b = 1
    for i in range(7):
        if hexnum >= 2**(7*(i+1)):
             n_b += 1
    return n_b

num = _get_number_of_seven_bytes(asddd)
def _transpose_two(string, num_of_bytes):
    asd = []
    temp = string[::-1]
    for i in range(num_of_bytes):
        temp_two = temp[(7*i):(7*(i+1))]
        temp_two = temp_two.zfill(7)
        if i == 0:
            temp_two += "0"
        else:
            temp_two += "1"
        asd.append(temp_two[::-1])
    return asd
def _transpose_to_seven_bytes(string, num_of_bytes):
    asd = []
    k = len(string) -1
    for i in range(num_of_bytes):
        x = ""
        r = 7
        while(k !=-1):
            x += string[k]
            r -= 1
            k -= 1
            if(r == 0):
                break
            
        x = x.zfill(7)
        x = x[::-1]
        if i == 0:
            x = "0" + x
        else:
            x = "1" + x
        asd.append(x)
    return asd

temp = _transpose_two(s,num)

def _bin_to_hex(binaries):
    return [int(x, 2) for x in binaries]

def decode(bytes_):
    test = [_get_hex_in_binary(x,8) for x in bytes_]
    if test[-1][0] == "1":
        raise ValueError("incomplete sequence")
    asdd = []
    m = []
    for i in range(len(test)):
        if test[i][0] != "0":
            m.append(test[i])
        else:
            m.append(test[i])
            asdd.append(m)
            m = []    
    x = [int("".join(r[1:] for r in i),2) for i in asdd]
    return x    
        
    
print(decode([0xC0,
                    0x0,
                    0xC8,
                    0xE8,
                    0x56,
                    0xFF,
                    0xFF,
                    0xFF,
                    0x7F,
                    0x0,
                    0xFF,
                    0x7F,
                    0x81,
                    0x80,
                    0x0]))
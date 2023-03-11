import re
def cipher_text(plain_text):
    normalized = re.sub(r"[^A-Za-z0-9]+", '', plain_text.lower())
    l = len(normalized)
    tup = _find_c_and_r(l)
    x = []
    for i in range(tup[1]):
        x.append(normalized[i*tup[0]:tup[0]+i*tup[0]].ljust(tup[0]))
    r = [""]*tup[0]
    for i in x:
        for j in range(len(i)):
            r[j] = r[j] + i[j]
    s = ""
    for i in r:
        s +=  i + " "
    return s[:-1]
        
def _find_c_and_r(l):
    r = 0
    c = 0
    f = True
    while(r*c < l or c < r or c-r>1):
        if (f):
            c += 1
            f = False
        else:
            r += 1
            f = True
    return(c,r)

print(cipher_text("If man was meant to stay on the ground, god would have given us roots."))
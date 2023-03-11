letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def rows(letter):
    ind = letters.index(letter.lower())
    spaces = 1+ 2*ind
    if letter == "A":
        return ["A"]
    x = [" "*ind + "A" + " "*ind]
    for i in range(ind):
        s = " "*(ind-i-1) + letters[i+1]+" "*(1+ 2*i) + letters[i+1] + " "*(ind-i-1)
        x.append(s.upper())
    for i in range(ind-1,0,-1):
        s = " "*(ind-i) + letters[i]+" "*(1+ 2*(i-1)) + letters[i] + " "*(ind-i)
        x.append(s.upper())
    x += [" "*ind + "A" + " "*ind]    
    return x

print(rows("Z"))
text = "apple"
res = ""
need_space = text.find(" ")
for i in text.split():
    if(i[0] in ['a', 'e', 'i', 'o', 'u'] or i[:2] in ['xr','yt']):
        print(i+'ay')
    elif(i[1:3] == 'qu' or i[:2] == 'qu'):
        pos = i.find('qu')
        x = i[pos+2:]+i[:pos+2]+'ay'
        res += x
    else:
        pos = 99
        for index, char in enumerate(i):
            if char in 'aeiou':
                pos = index
                break
        if(i.find('y') != -1  and i[0] != 'y'):
            posy = i.find('y')
            if(posy < pos):
                res += i[posy:]+i[:posy]+'ay'
            else:
                res += i[pos:]+i[:pos]+'ay'
        else:
            res += i[pos:]+i[:pos]+'ay'
    if(need_space != -1):
        res += " "

print(res if need_space == -1 else res[:-1])
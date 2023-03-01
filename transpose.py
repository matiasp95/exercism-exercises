def transpose(lines):
    if len(lines) == 0:
        return ""
    max = _get_max(lines)
    _fill_blanks(lines, max)
    ret = []
    for j,k in enumerate(lines[0]):
        x = ""
        for i in range(len(lines)):
            x += lines[i][j]
        ret.append(x)
    st_ret = ""
    for a in ret:
        st_ret = st_ret + a + "\n"
    return st_ret
            
def _get_max(lista):
    return len(max(lista, key=len))

def get_max(lista):
    max = 0
    for i in lista:
        if len(i) > max:
            max = len(i)
    return max

def _fill_blanks(lista, max):
    for i in range(len(lista)):
        while(len(lista[i])<max):
            lista[i] = lista[i] + " "
    return lista




#######
#New solution because this wont work on exercism
import re

def transp_two(lines):
    m = _get_max(lines)
    n = len(lines)
    for i in range(len(lines)):
        lines[i] = re.sub(" ", "_", lines[i])
    temp = _fill_three(lines,m)   
    x = [[temp[j][i] for j in range(n)] for i in range(m)]
    prev = ["".join(string) for string in x]
    for i in range(len(prev)):
        prev[i] = prev[i].rstrip()
    print(prev)
    xd = "\n".join(prev)
    xd = re.sub("_", " ", xd)  
    return xd

def _fill_two(lista, max):
    for x in range(len(lista)-1):
        if (len(lista[x]) < len(lista[x+1])):
           lista[x] = lista[x].ljust(len(lista[x+1]))
    
    #return [(x.ljust(max)) for x in lista if()]
    return lista
def _fill_three(lista,max):
    return [(x.ljust(max)) for x in lista]

print(transp_two(["The longest line.", "A long line.", "A longer line.", "A line."]))
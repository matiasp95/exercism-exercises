def annotate(minefield):
    # Function body starts here
    if(minefield == []):
        return []
    _validator(minefield)
    f = 0
    if(len(minefield) == 1 ):
        minefield.append(" "*len(minefield[0]))
        f = 1
    for i, row in enumerate(minefield):
        for j, cell in enumerate(row):
        #For top row
            if(i == 0):
                if(len(row) == 1 and cell != "*"):
                    acum = 0
                    acum += _sum_if_mine(minefield[i+1][j])
                    minefield[i] = minefield[i][:j]+str(acum)+minefield[i][j+1:]
                elif (j == 0 and cell != "*"):
                    acum = 0
                    acum += _sum_if_mine(minefield[i][j+1])
                    acum += _sum_if_mine(minefield[i+1][j])
                    acum += _sum_if_mine(minefield[i+1][j+1])
                    minefield[i] = minefield[i][:j]+str(acum)+minefield[i][j+1:]

                elif (j == len(row)-1 and cell != "*"):
                    acum = 0
                    acum += _sum_if_mine(minefield[i][j-1])
                    acum += _sum_if_mine(minefield[i+1][j])
                    acum += _sum_if_mine(minefield[i+1][j-1])
                    minefield[i] = minefield[i][:j]+str(acum)+minefield[i][j+1:]
                elif(cell != "*"):
                    acum = 0
                    acum += _sum_if_mine(minefield[i][j-1])
                    acum += _sum_if_mine(minefield[i][j+1])
                    acum += _sum_if_mine(minefield[i+1][j])
                    acum += _sum_if_mine(minefield[i+1][j-1])
                    acum += _sum_if_mine(minefield[i+1][j+1])
                    minefield[i] = minefield[i][:j]+str(acum)+minefield[i][j+1:]
        #For bottom row
            elif(i == len(minefield)-1):
                if(len(row) == 1 and cell != "*"):
                    acum = 0
                    acum += _sum_if_mine(minefield[i-1][j])
                    minefield[i] = minefield[i][:j]+str(acum)+minefield[i][j+1:]
                elif (j == 0 and cell != "*"):
                    acum = 0
                    acum += _sum_if_mine(minefield[i][j+1])
                    acum += _sum_if_mine(minefield[i-1][j])
                    acum += _sum_if_mine(minefield[i-1][j+1])
                    minefield[i] = minefield[i][:j]+str(acum)+minefield[i][j+1:]

                elif (j == len(row)-1 and cell != "*"):
                    acum = 0
                    acum += _sum_if_mine(minefield[i][j-1])
                    acum += _sum_if_mine(minefield[i-1][j])
                    acum += _sum_if_mine(minefield[i-1][j-1])
                    minefield[i] = minefield[i][:j]+str(acum)+minefield[i][j+1:]
                elif(cell != "*"):
                    acum = 0
                    acum += _sum_if_mine(minefield[i][j-1])
                    acum += _sum_if_mine(minefield[i][j+1])
                    acum += _sum_if_mine(minefield[i-1][j])
                    acum += _sum_if_mine(minefield[i-1][j-1])
                    acum += _sum_if_mine(minefield[i-1][j+1])
                    minefield[i] = minefield[i][:j]+str(acum)+minefield[i][j+1:]
        #For other rows
            else:
                if(len(row) == 1 and cell != "*"):
                    acum = 0
                    acum += _sum_if_mine(minefield[i-1][j])
                    acum += _sum_if_mine(minefield[i+1][j])
                    minefield[i] = minefield[i][:j]+str(acum)+minefield[i][j+1:]
                elif (j == 0 and cell != "*"): #
                    acum = 0
                    acum += _sum_if_mine(minefield[i][j+1])
                    acum += _sum_if_mine(minefield[i+1][j])
                    acum += _sum_if_mine(minefield[i-1][j])
                    acum += _sum_if_mine(minefield[i-1][j+1])
                    acum += _sum_if_mine(minefield[i+1][j+1])
                    minefield[i] = minefield[i][:j]+str(acum)+minefield[i][j+1:]

                elif (j == len(row)-1 and cell != "*"): #
                    acum = 0
                    acum += _sum_if_mine(minefield[i][j-1])
                    acum += _sum_if_mine(minefield[i+1][j])
                    acum += _sum_if_mine(minefield[i-1][j])
                    acum += _sum_if_mine(minefield[i-1][j-1])
                    acum += _sum_if_mine(minefield[i+1][j-1])
                    minefield[i] = minefield[i][:j]+str(acum)+minefield[i][j+1:]
                elif(cell != "*"):
                    acum = 0
                    acum += _sum_if_mine(minefield[i-1][j-1])
                    acum += _sum_if_mine(minefield[i-1][j])
                    acum += _sum_if_mine(minefield[i-1][j+1])
                    acum += _sum_if_mine(minefield[i][j-1])
                    acum += _sum_if_mine(minefield[i][j+1])
                    acum += _sum_if_mine(minefield[i+1][j-1])
                    acum += _sum_if_mine(minefield[i+1][j])
                    acum += _sum_if_mine(minefield[i+1][j+1])
                    minefield[i] = minefield[i][:j]+str(acum)+minefield[i][j+1:]
    minefield = _clean_list(minefield)
    if f == 1:
        minefield.pop()
    return minefield
            
def _sum_if_mine(char):
    if(char == "*"):
        return 1
    return 0

def _clean_list(lista):
    x = []
    for i in lista:
        while("0" in i):
            i = i.replace("0", " ")
        x.append(i)
    return x

def _validator(lista):
    leng = len(lista[0])
    for i in lista:
        if(len(i) != leng):
            raise ValueError("The board is invalid with current input.")
        if (len(i) >=1):
            for x in i:
                if(x!= " " and x!="*"):
                    raise ValueError("The board is invalid with current input.")
print(annotate([]))

def _get_possible_dirs(lTop, lRight, posRow, posCol):
    dirs = []
    if(lRight == 0 and posRow == 0):
        dirs = [[1,0]]
    elif(lRight == 0 and (posRow > 0 and posRow!=lTop)):
        dirs = [[-1,0],[1,0]]
    elif(lRight == 0 and posRow == lTop):
        dirs = [[-1,0]]
    elif(posCol == 0 and posRow == 0):
        dirs = [[0,1],[1,0],[1,1]]
    elif(posCol == 0 and (posRow > 0 and posRow!=lTop)):
        dirs = [[-1,0],[-1,1],[0,1],[1,0],[1,1]]
    elif(posCol == 0 and posRow==lTop):
        dirs = [[-1,0],[-1,1],[0,1]]
    elif(posCol == lRight and posRow == 0):
        dirs = [[0,-1],[1,0],[1,-1]]
    elif(posCol == lRight and (posRow > 0 and posRow!=lTop)):
        dirs = [[-1,0],[-1,-1],[0,-1],[1,0],[1,-1]]
    elif(posCol == lRight and posRow==lTop):
        dirs = [[-1,0],[-1,-1],[0,-1]]
    elif(posRow == 0 and (posCol>0 and posCol!=lRight)):
        dirs = [[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    elif(posRow == lTop and (posCol>0 and posCol!=lRight)):
       dirs = [[0,-1],[0,1],[-1,-1],[-1,0],[-1,1]]
    else:
        dirs = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    return dirs

def annotate_two(minefield):
    # Function body starts here
    if(minefield == []):
        return []
    _validator(minefield)
    f = 0
    if(len(minefield) == 1 ):
        minefield.append(" "*len(minefield[0]))
        f = 1
    for i, row in enumerate(minefield):
        for j, cell in enumerate(row):
            dirs = _get_possible_dirs(len(minefield)-1,len(row)-1,i,j)
            if(cell != "*"):
                acum = 0
                for x in dirs:
                    acum += _sum_if_mine(minefield[i+x[0]][j+x[1]])
                minefield[i] = minefield[i][:j]+str(acum)+minefield[i][j+1:]
    minefield = _clean_list(minefield)
    if f == 1:
        minefield.pop()
    return minefield

print(annotate_two(["*", " ", " ", " ", "*"]))
VALID_NUMBERS = [" _ | ||_|","     |  |"," _  _||_ "," _  _| _|","   |_|  |"," _ |_  _|"," _ |_ |_|"," _   |  |"," _ |_||_|"," _ |_| _|"]
def convert(input_grid):
    if(len(input_grid) % 4 != 0):
        raise ValueError("Number of input lines is not a multiple of four")
    if(len(input_grid[0]) %3 != 0):
        raise ValueError("Number of input columns is not a multiple of three")
    m = len(input_grid[0])//3
    
    x = [""]*m
    ret = ""
    for i in range(len(input_grid)):
        if((i+1)%4 ==0 and i != 0):
            ret += _determine_number(x)+","
            x = [""]*m
            
            continue
        for j in range(0,m):
            x[j] = x[j] + input_grid[i][j*3:j*3+3]
    return ret[:-1]
def _determine_number(lista):
    ret = ""
    for i in lista:
        if i in VALID_NUMBERS:
            ret += str(VALID_NUMBERS.index(i))
        else:
            ret += "?"
    return ret

input = [
                    "    _  _     _  _  _  _  _  _ ",
                    "  | _| _||_||_ |_   ||_||_|| |",
                    "  ||_  _|  | _||_|  ||_| _||_|",
                    "                              ",
                ]
print(convert(input))
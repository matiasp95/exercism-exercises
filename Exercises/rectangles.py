from itertools import combinations
def rectangles(strings):
    return sum(1
        for vs in combinations(vertices(strings), 4) 
        if is_rectangle(strings, vs)
    ) # Look for all combinations of 4 vertices (Returned by the vertices() function), and if they are a rectangle, add 1. Then return the total

#For each row in strings, and each char in that row, if it is a "+", append it to the vertices list (j,i coordinates)
def vertices(strings):
    vertices = []
    for i,v in enumerate(strings):
        for j,k in enumerate(v):
            if k == "+":
                vertices.append((j,i))
    return vertices

def build_combinations(list, num):
    for i,v in enumerate(list):
        for j in range(list[:-4]):
            yield (i,j) 

#Sort the verts from the parameters, then check if all edges combinations are true, and return that boolean (if it is True it will sum 1 in main function)
def is_rectangle(strings, verts):
    top_left, bottom_left, top_right, bottom_right = sorted(verts)
    return all([
        h_edge(strings, top_left,    top_right),
        h_edge(strings, bottom_left, bottom_right),
        v_edge(strings, top_left,    bottom_left),
        v_edge(strings, top_right,   bottom_right),
    ])

#Check vertical edge. If x1 and x2 are equal (Therefore on the same horizontal line), and y1 < y2 (Meaning one is above the other), 
# check if all characters in between are either "+" or "|" (For loop goes from y1 to y2+1, and checks the string on the same vertical line (So this strings[j][x1] could
# also be strings[j][x2]). If all of them are truwe, return True. The reason why the loop goes from y1 to y2+1 is because it also checks the vertix itself. (Otherwise there would be
# nothing to check, and it would return False)

def v_edge(strings, v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    return x1 == x2 and y1 < y2 and all([
        strings[j][x1] in "+|"
        for j in range(y1, y2+1)
    ])

#Check horizontal edge. If x1 and x2 are equal (Therefore on the same vertical line), and x1 < x2 (Meaning one is right to the other), 
# check if all characters in between are either "+" or "-" (For loop goes from x1 to x2+1, and checks the string on the same horizontal line (So this strings[y1][i] could
# also be strings[y2][i]). If all of them are true, return True. 
def h_edge(strings, v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    return y1 == y2 and x1 < x2 and all([
        strings[y1][i] in "+-"
        for i in range(x1, x2+1)
    ])

#Did not finish this because of lacking time and higher complexity than assumed (This is not an easy exercise),
#but decided to comment this Community Solution to better understand how it works.            
    
A = [3, 4, 5]
B = [0, 1, 2, 3, 4, 5]
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if(len(list_one) == len(list_two)):
        return UNEQUAL
    if(len(list_one) > len(list_two)):
        for i in range(len(list_one)-len(list_two)+1):
            flag = 0
            for j in range(len(list_two)):
                if(list_one[i+j] != list_two[j]):
                    flag = 1
            if flag == 0:
                return SUPERLIST
        return UNEQUAL
    for i in range(len(list_two)-len(list_one)+1):
        flag = 0
        for j in range(len(list_one)):
            if(list_two[i+j] != list_one[j]):
                flag = 1
                break
        if flag == 0:
            return SUBLIST
    return UNEQUAL

print(sublist(A,B))
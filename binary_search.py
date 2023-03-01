def find(search_list, value):
    lb = 0
    ub = len(search_list)-1
    mp = ub//2
    while(lb <= ub):
        if(search_list[mp] == value):
            return mp
        elif(value > search_list[mp]):
            lb = mp+1
            mp = (lb+ub)//2
        else:
            ub = mp-1
            mp = (lb+ub)//2
    raise ValueError("value not in array")

print(find([1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 634], 378))
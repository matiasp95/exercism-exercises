def flatten(iterable):
    x = []
    for i in iterable:
        if(type(i) != list):
            x.extend((i,))
        else:
            x.extend(flatten(i))
    while(None in x):
        x.remove(None)
    return x
print(flatten([1, [2, [[3]], [4, [[5]]], 6, 7], 8]))

def sum_of_multiples(limit, multiples):
    res = []
    for i in multiples:
        if(i == 0):
            continue
        max_multiple = int(limit/i)+1
        for j in range (1, max_multiple):
            if i*j < limit:
                res.append(i*j)
    set_of_multiples = set(res)     
    return sum(set_of_multiples)

# Practice list comprehension:

def sum_of_multiples_lc(limit, multiples):
    res = [i*j for i in multiples if i != 0  for j in range(1, int(limit/i)+1) if i*j<limit]
    set_of_multiples = set(res)     
    return sum(set_of_multiples)

print(sum_of_multiples_lc(10000, [43, 47]))
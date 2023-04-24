def primes(limit):
    x = [i for i in range(2,limit+1)]
    set_s = set()
    for i in x:
        if i != 'composite':
            set_s.add(i)
            r = i
            j = 2
            while(r*j < limit+1):
                x[r*j-2] = 'composite'
                j += 1
    resp = list(set_s)
    resp.sort()
    return resp

print(primes(1000))
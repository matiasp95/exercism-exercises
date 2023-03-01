import time
def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    largest_pal = 0
    factor = []
    for i in range(min_factor, max_factor+1):
        for j in range(i, max_factor+1):
            pr = i*j
            if (pr >= largest_pal and str(i*j) == str(i*j)[::-1]):
                if(pr == largest_pal):
                   factor.append((i,j))
                else:
                    factor = []
                    factor.append((i,j))
                largest_pal = pr
    return largest_pal,factor 

def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    smallest_pal = max_factor**2
    factor = []
    for i in range(min_factor, max_factor+1):
        for j in range(i, max_factor+1):
            pr = i*j
            if (pr <= smallest_pal and str(i*j) == str(i*j)[::-1]):
                if(pr == smallest_pal):
                   factor.append((i,j))
                else:
                    factor = []
                    factor.append((i,j))
                smallest_pal = pr
    return smallest_pal,factor 


start = time.time()
print(largest(1000,9999))
end = time.time()
print(end-start)

start = time.time()
print(smallest(1000,9999))
end = time.time()
print(end-start)


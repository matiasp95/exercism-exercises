import time
def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes
start = time.time()
generate_primes(100)
end = time.time()
print(end-start)

def sieve_of_eratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize
    # all entries in it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    primes = [True] * (n+1)
    p = 2
    while p * p <= n:
        # If prime[p] is not changed, then it is a prime
        if primes[p] == True:
            # Update all multiples of p
            for i in range(p * 2, n+1, p):
                primes[i] = False
        p += 1
    # Return a list of primes
    return [p for p in range(2, n+1) if primes[p] == True]
start = time.time()
sieve_of_eratosthenes(10)
end = time.time()
print(end-start)

def sieve_of_atkin(n):
    # Initialize the sieve array with False values
    sieve = [False] * (n+1)
    
    # Create the prime candidate list
    primes = [2, 3]
    for i in range(5, n+1):
        if i % 2 != 0 and i % 3 != 0:
            primes.append(i)
    
    # Use the sieve of Atkin algorithm to find primes
    for x in range(1, int(n**0.5)+1):
        for y in range(1, int(n**0.5)+1):
            num = 4*x**2 + y**2
            if num <= n and (num % 12 == 1 or num % 12 == 5):
                sieve[num] = not sieve[num]
            num = 3*x**2 + y**2
            if num <= n and num % 12 == 7:
                sieve[num] = not sieve[num]
            num = 3*x**2 - y**2
            if x > y and num <= n and num % 12 == 11:
                sieve[num] = not sieve[num]
    
    # Mark all composite numbers as True
    for i in range(5, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i**2, n+1, i**2):
                sieve[j] = True
    
    # Return a list of primes
    return [prime for prime in primes if not sieve[prime]]


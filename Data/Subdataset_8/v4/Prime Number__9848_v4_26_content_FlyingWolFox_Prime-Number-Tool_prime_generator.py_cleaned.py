
n = 2
rest = []
primes = [1]
count = 0
while n <= 3001:
    i = 0
    m = primes[i]
    while m < n:
        p = n % m
        rest.append(p)
        count = rest.count(0)
        i += 1
        if i >= len(primes) or count > 1:
            break
        m = primes[i]
    if count == 1:
        print(n, "is prime")
        primes.append(n)
    if n == 2:
        n += 1
    else:
        n += 2
    rest = []
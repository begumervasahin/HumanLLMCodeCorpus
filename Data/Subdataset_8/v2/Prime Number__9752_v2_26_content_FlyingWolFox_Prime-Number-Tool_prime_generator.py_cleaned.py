
n = 2
primes = [1]
count = 0
while n <= 3001:
    i = 0
    m = primes[i]
    while m < n:
        p = n % m
        if p == 0:
            count += 1
            break
        i += 1
        if i + 1 > len(primes):
            break
        m = primes[i]
    if count == 0:
        print(n, "is prime")
        primes.append(n)
    if n == 2:
        n += 1
    else:
        n += 2
    count = 0

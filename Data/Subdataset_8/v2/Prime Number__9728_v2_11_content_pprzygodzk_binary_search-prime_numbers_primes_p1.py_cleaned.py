import math
def SieveofEratosthenes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    p = 2
    while p**2 <= n:
        if primes[p]:
            for i in range(p**2, n+1, p):
                primes[i] = False
        p += 1
    return [i for i in range(2, n+1) if primes[i]]
def PrimesGenerator(n):
    primes = [2, 3]
    num = 5
    while len(primes) < n:
        is_prime = True
        for p in primes:
            if p * p > num:
                break
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 2 if num % 6 == 1 else 4
    return primes
def PrimorialGenerator(n):
    primes = PrimesGenerator(n-1)
    primorials = [1]
    for prime in primes:
        primorials.append(primorials[-1] * prime)
    return primorials
def CheckPrimarility(n):
    if n < 2:
        return "The least prime number is 2!"
    if n == 2:
        return "prime"
    if n % 2 == 0:
        return "composite"
    for d in range(3, math.isqrt(n) + 1, 2):
        if n % d == 0:
            return "composite"
    return "prime"
def Decompose(n):
    if n == 1:
        return [1]
    if CheckPrimarility(n) == "prime":
        return [n]
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            n
        else:
            d += 1
    factors.append(n)
    return factors
if __name__ == '__main__':
    print("Prime numbers from 2 to 100 (Sieve of Eratosthenes):", SieveofEratosthenes(100))
    print("First 25 prime numbers:", PrimesGenerator(25))
    print("First 10 primorial numbers:", PrimorialGenerator(10))
    primorial = PrimorialGenerator(10000)
    print("Length of the 10000th primorial number:", len(str(primorial[-1])))
    print("Is 2 a prime or composite number?: 2 is a", CheckPrimarility(2), "number")
    print("Is 5 a prime or composite number?: 5 is a", CheckPrimarility(5), "number")
    print("Is 18 a prime or composite number?: 18 is a", CheckPrimarility(18), "number")
    print("Is 27 a prime or composite number?: 27 is a", CheckPrimarility(27), "number")
    print("Prime decomposition of 12:", Decompose(12))
    print("Prime decomposition of 5:", Decompose(5))
    print("Prime decomposition of 2047:", Decompose(2047))
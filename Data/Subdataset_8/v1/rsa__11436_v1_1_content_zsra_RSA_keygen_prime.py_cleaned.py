import random
import xgcd
def GetPrime(min_val, max_val):
    primes = [i for i in range(min_val, max_val) if is_Prime(i)]
    return random.choice(primes)
def is_Prime(n):
    if n != int(n):
        return False
    n = int(n)
    if n == 0 or n == 1 or n == 4 or n == 6 or n == 8 or n == 9:
        return False
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    assert(2 ** s * d == n - 1)
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True
    for i in range(8):
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
    return True
def isCoPrime(a, b):
    if xgcd.GCD(a, b) == 1:
        return True
    else:
        return False
min_val = 10
max_val = 100
prime = GetPrime(min_val, max_val)
print("Random prime number between", min_val, "and", max_val, ":", prime)
a = 15
b = 28
print("Are", a, "and", b, "co-prime?", isCoPrime(a, b))
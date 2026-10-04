import math
import random
import time
def power_of_two(n):
    r = 0
    d = n
    while d % 2 == 0:
        r += 1
        d >>= 1
    assert(2**r * d == n)
    return r, d
def miller_rabin_test(n, k):
    if n <= 3:
        return n == 2 or n == 3
    if n % 2 == 0:
        return False
    r, d = power_of_two(n - 1)
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
def simple_is_prime(n):
    '''
    Simpler primality check for time comparison
    '''
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
n = 200000015717
t0 = time.time()
print("Miller-Rabin Test:", miller_rabin_test(n, 8))
t1 = time.time()
print("Miller-Rabin Time: " + str(t1 - t0))
t0 = time.time()
print("Simple Primality Test:", simple_is_prime(n))
t1 = time.time()
print("Simple Primality Time: " + str(t1 - t0))
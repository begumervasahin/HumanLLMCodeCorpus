import math
import random
import time
def power_of_two(n):
    power = 0
    odd_number = n
    while odd_number % 2 == 0:
        power += 1
        odd_number
    assert 2**power * odd_number == n
    return power, odd_number
def miller_rabin_test(n, k):
    if n <= 3:
        return False
    power, odd_number = power_of_two(n - 1)
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, odd_number, n)
        if x == 1 or x == n - 1:
            continue
        composite = False
        for _ in range(power - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                composite = True
                break
        if not composite:
            return False
    return True
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
n = 200000015717
t0 = time.time()
print("Miller-Rabin Test Result:", miller_rabin_test(n, 8))
t1 = time.time()
print("Miller-Rabin Primality Test Time:", t1 - t0)
t0 = time.time()
print("Simple Primality Test Result:", is_prime(n))
t1 = time.time()
print("Simple Primality Test Time:", t1 - t0)
import math
import random
import time
def power_of_two(n):
    r = 0
    d = n
    while d % 2 == 0:
        r += 1
        d >>= 1
    assert 2**r * d == n
    return r, d
def miller_rabin_test(n, k):
    if n <= 3:
        return n == 2 or n == 3
    r, d = power_of_two(n - 1)
    for _ in range(k):
        rand_int = random.randint(2, n - 2)
        x = pow(rand_int, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
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
if __name__ == "__main__":
    n = 200000015717
    start_time = time.time()
    print("Miller-Rabin Test Result:", miller_rabin_test(n, 8))
    end_time = time.time()
    print("Miller-Rabin Test Time: {:.6f} seconds".format(end_time - start_time))
    start_time = time.time()
    print("Simple Primality Test Result:", is_prime(n))
    end_time = time.time()
    print("Simple Primality Test Time: {:.6f} seconds".format(end_time - start_time))
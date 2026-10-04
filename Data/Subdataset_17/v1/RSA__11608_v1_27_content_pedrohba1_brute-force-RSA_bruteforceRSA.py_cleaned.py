import math
import time
def nearest_odd_under(number):
    if number % 2 == 0:
        number -= 1
    else:
        number -= 2
    return number
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m
def brute_rsa(n, e):
    start_time = time.time()
    c = math.floor(math.sqrt(n))
    c = nearest_odd_under(c)
    for i in range(c, 1, -2):
        if n % i == 0:
            p = i
            break
    q = n
    if n != p * q:
        raise Exception('Factorization failed')
    phin = (p - 1) * (q - 1)
    d = modinv(e, phin)
    if d * e % phin != 1:
        raise Exception('Modular inverse calculation failed')
    total_time = time.time() - start_time
    return (d, total_time)
keys = [
    (1325147, 79), (13339787, 351047), (87411743, 11), (153988391, 365),
    (642281891, 80105), (3662937263, 80273), (2461987247, 78703),
    (10988963221, 118297), (9979645019, 9764819), (36207914857, 89)
]
total_time = 0
for n, e in keys:
    d, elapsed_time = brute_rsa(n, e)
    print(f'Key pair (n, e): ({n}, {e})')
    print(f'Private key d: {d}')
    print(f'Time taken: {elapsed_time:.6f} seconds')
    total_time += elapsed_time
print(f'Total time: {total_time:.6f} seconds')
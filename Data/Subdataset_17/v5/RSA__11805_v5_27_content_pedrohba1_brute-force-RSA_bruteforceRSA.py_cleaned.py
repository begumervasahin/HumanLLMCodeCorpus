import math
import time
def nearest_odd_under(number):
    return number - 1 if number % 2 == 0 else number - 2
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b
def modinv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    return x % m
def brute_rsa(n, e):
    start_time = time.time()
    c = nearest_odd_under(math.isqrt(n))
    for i in range(c, 1, -2):
        if n % i == 0:
            p = i
            break
    else:
        raise Exception('Failed to find p')
    q = n
    if n != p * q:
        raise Exception('Failed to find correct p and q')
    phi_n = (p - 1) * (q - 1)
    d = modinv(e, phi_n)
    if d * e % phi_n != 1:
        raise Exception('Failed to find correct d')
    total_time = time.time() - start_time
    return d, total_time
def main():
    key_pairs = [
        (1325147, 79), (13339787, 351047), (87411743, 11),
        (153988391, 365), (642281891, 80105), (3662937263, 80273),
        (2461987247, 78703), (10988963221, 118297), (9979645019, 9764819),
        (36207914857, 89)
    ]
    total_time = 0
    for n, e in key_pairs:
        try:
            private_key, elapsed_time = brute_rsa(n, e)
            print(f'Key pair (n, e): ({n}, {e})')
            print(f'Private key d: {private_key}')
            print(f'Time taken: {elapsed_time:.6f} seconds')
            total_time += elapsed_time
        except Exception as ex:
            print(f'Failed to process key pair ({n}, {e}): {ex}')
    print(f'Total time taken: {total_time:.6f} seconds')
if __name__ == '__main__':
    main()
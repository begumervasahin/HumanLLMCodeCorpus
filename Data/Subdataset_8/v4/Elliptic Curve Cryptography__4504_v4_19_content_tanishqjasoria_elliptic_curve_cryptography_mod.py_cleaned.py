def euclidean_gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    return euclidean_gcd(b, a % b)
def extended_euclidean(a, b):
    x, y, gcd = _extended_euclidean_util(a, b, 1, 1)
    return x, y, gcd
def _extended_euclidean_util(a, b, x, y):
    if a == 0:
        x = 0
        y = 1
        return x, y, b
    x1, y1, gcd = _extended_euclidean_util(b % a, a, x, y)
    x = y1 - (b
    y = x1
    return x, y, gcd
def inverse_brute_force(n, p):
    for i in range(p):
        if (n * i) % p == 1:
            return i
def inverse_extended_euclidean(n, p):
    n = n % p
    inv, _, _ = extended_euclidean(n, p)
    return inv % p
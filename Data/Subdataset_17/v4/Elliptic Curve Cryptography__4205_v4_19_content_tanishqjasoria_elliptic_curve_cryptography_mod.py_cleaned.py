
def euclidean_gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    return euclidean_gcd(b, a % b)
def extended_euclidean(a, b):
    x, y, gcd = _extended_euclidean_util(a, b)
    return x, y, gcd
def _extended_euclidean_util(a, b):
    if a == 0:
        return 0, 1, b
    x1, y1, gcd = _extended_euclidean_util(b % a, a)
    x = y1 - (b
    y = x1
    return x, y, gcd
def inverse_brute_force(n, p):
    for i in range(1, p):
        if (n * i) % p == 1:
            return i
    raise ValueError(f"No modular inverse found for {n} mod {p}")
def inverse_extended_euclidean(n, p):
    n = n % p
    inv, _, gcd = extended_euclidean(n, p)
    if gcd != 1:
        raise ValueError(f"No modular inverse exists for {n} mod {p}")
    return inv % p
if __name__ == "__main__":
    a, b = 30, 20
    print(f"GCD of {a} and {b} using Euclidean algorithm: {euclidean_gcd(a, b)}")
    x, y, gcd = extended_euclidean(a, b)
    print(f"Extended Euclidean algorithm result for {a} and {b}: x={x}, y={y}, gcd={gcd}")
    n, p = 3, 11
    print(f"Brute force inverse of {n} mod {p}: {inverse_brute_force(n, p)}")
    print(f"Extended Euclidean inverse of {n} mod {p}: {inverse_extended_euclidean(n, p)}")
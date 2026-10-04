from typing import Tuple
def modulo_multiply(a: int, b: int, mod: int) -> int:
    if mod == 0:
        raise Exception("Divide by zero error")
    return ((a % mod) * (b % mod)) % mod
def modulo_pow(a: int, b: int, mod: int) -> int:
    result = 1
    while b:
        result = modulo_multiply(result, a, mod)
        b -= 1
    return result % mod
def egcd(a: int, b: int) -> Tuple[int, int, int]:
    if a == 0:
        return (b, 0, 1)
    g, x, y = egcd(b % a, a)
    return (g, y - (b
def modulo_div(a: int, b: int, mod: int) -> int:
    return modulo_multiply(a, mulinv(b, mod), mod)
def mulinv(b: int, n: int) -> int:
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n
    raise Exception("Modular Inverse does not exist")
if __name__ == '__main__':
    a = 3
    b = 4
    mod = 5
    print(f"Modulo Multiply: {modulo_multiply(a, b, mod)}")
    print(f"Modulo Power: {modulo_pow(a, b, mod)}")
    print(f"Extended GCD: {egcd(a, mod)}")
    print(f"Modulo Division: {modulo_div(a, b, mod)}")
    print(f"Multiplicative Inverse: {mulinv(b, mod)}")

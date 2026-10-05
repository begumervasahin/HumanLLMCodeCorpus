from typing import Tuple
def modulo_multiply(a: int, b: int, mod: int) -> int:
    if mod == 0:
        raise ValueError("Modulo cannot be zero")
    return (a * b) % mod
def modulo_pow(a: int, b: int, mod: int) -> int:
    result = 1
    for _ in range(b):
        result = modulo_multiply(result, a, mod)
    return result
def egcd(a: int, b: int) -> Tuple[int, int, int]:
    if a == 0:
        return b, 0, 1
    g, x, y = egcd(b % a, a)
    return g, y - (b
def modulo_div(a: int, b: int, mod: int) -> int:
    return modulo_multiply(a, mulinv(b, mod), mod)
def mulinv(b: int, n: int) -> int:
    g, x, _ = egcd(b, n)
    if g != 1:
        raise ValueError("Modular Inverse does not exist")
    return x % n
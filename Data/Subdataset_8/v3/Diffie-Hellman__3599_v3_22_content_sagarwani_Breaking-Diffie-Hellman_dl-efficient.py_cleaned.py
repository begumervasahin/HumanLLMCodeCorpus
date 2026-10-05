import sys
import re
from math import ceil, sqrt
def modular_exponentiation(base, exponent, modulus):
    result = 1
    binary_exponent = "{0:b}".format(exponent)
    for bit in binary_exponent:
        result = (result * result) % modulus
        if bit == '1':
            result = (result * base) % modulus
    return result
def baby_step_giant_step(p, g, h):
    N = ceil(sqrt(p - 1))
    baby_steps = {modular_exponentiation(g, i, p): i for i in range(N)}
    giant_step = modular_exponentiation(g, N * (p - 2), p)
    for j in range(N):
        y = (h * modular_exponentiation(giant_step, j, p)) % p
        if y in baby_steps:
            return j * N + baby_steps[y]
    return None
if __name__ == '__main__':
    with open(sys.argv[1], 'r') as file:
        content = file.readlines()
        p, g, ga = map(int, re.findall('\d+', content[0]))
    exponent = baby_step_giant_step(p, g, ga)
    if exponent:
        print(exponent)
    else:
        print("Exponent not found.")
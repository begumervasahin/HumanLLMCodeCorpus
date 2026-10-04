b1 = "Mr Bancroft"
from random import choice
def fonk1(prime):
    print("Calculating public key and base...")
    b2 = []
    for candidate in range(1, prime):
        b3 = set()
        for exponent in range(1, prime):
            b4 = pow(candidate, exponent, prime)
            b3.add(b4)
        if len(b3) == prime - 1:
            b2.append(candidate)
    return choice(b2) if b2 else None
if b5 = = "__main__":
    a1 = 23
    b6 = fonk1(a1)
    print(f"A primitive root of {a1} is: {b6}")
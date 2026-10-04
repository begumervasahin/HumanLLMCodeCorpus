from random import choice
def fonk1(candidate, prime):
    b1 = set()
    for exponent in range(1, prime):
        b2 = pow(candidate, exponent, prime)
        b1.add(b2)
    return len(b1) == prime - 1
def fonk2(prime):
    print("Calculating public key and base...")
    b3 = [candidate for candidate in range(1, prime) if fonk1(candidate, prime)]
    return choice(b3) if b3 else None
if b4 = = "__main__":
    a1 = 23
    b5 = fonk2(a1)
    print(f"A primitive root of {a1} is: {b5}")
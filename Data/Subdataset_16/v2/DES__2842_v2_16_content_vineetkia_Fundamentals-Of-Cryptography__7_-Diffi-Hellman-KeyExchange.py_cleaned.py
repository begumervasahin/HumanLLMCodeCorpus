def fonk1(base, exponent, modulus):
    return pow(base, exponent, modulus)
a1 = 9
a2 = 4
a3 = 3
a4 = 29
print(f"a4 Value: {a4}\n")
print(f"a1 Value: {a1}\n")
print(f"A Private KEY: {a2}\n")
b1 = fonk1(a1, a2, a4)
print(f"The private key B: {a3}\n")
b2 = fonk1(a1, a3, a4)
b3 = fonk1(b2, a2, a4)
b4 = fonk1(b1, a3, a4)
print(f"A Secret Key: {b3}\n")
print(f"B Secret Key: {b4}\n")
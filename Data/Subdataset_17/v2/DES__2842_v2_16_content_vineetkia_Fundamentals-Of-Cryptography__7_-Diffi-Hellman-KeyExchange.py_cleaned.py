def power(base, exponent, modulus):
    return pow(base, exponent, modulus)
G = 9
a = 4
b = 3
P = 29
print(f"P Value: {P}\n")
print(f"G Value: {G}\n")
print(f"A Private KEY: {a}\n")
x = power(G, a, P)
print(f"The private key B: {b}\n")
y = power(G, b, P)
ka = power(y, a, P)
kb = power(x, b, P)
print(f"A Secret Key: {ka}\n")
print(f"B Secret Key: {kb}\n")
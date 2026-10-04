def compute_modular_exponentiation(base, exponent, modulus):
    return pow(base, exponent, modulus)
def display_value(label, value):
    print(f"{label}: {value}")
def main():
    G = 9
    a = 4
    b = 3
    P = 29
    display_value("P Value", P)
    display_value("G Value", G)
    display_value("A Private Key", a)
    display_value("The private key B", b)
    x = compute_modular_exponentiation(G, a, P)
    y = compute_modular_exponentiation(G, b, P)
    ka = compute_modular_exponentiation(y, a, P)
    kb = compute_modular_exponentiation(x, b, P)
    display_value("A Secret Key", ka)
    display_value("B Secret Key", kb)
if __name__ == "__main__":
    main()
def compute_power(base, exponent, modulus):
    return pow(base, exponent, modulus)
def display_values(label, value):
    print(f"{label}: {value}\n")
def main():
    G = 9
    a = 4
    b = 3
    P = 29
    display_values("P Value", P)
    display_values("G Value", G)
    display_values("A Private KEY", a)
    x = compute_power(G, a, P)
    display_values("The private key B", b)
    y = compute_power(G, b, P)
    ka = compute_power(y, a, P)
    kb = compute_power(x, b, P)
    display_values("A Secret Key", ka)
    display_values("B Secret Key", kb)
if __name__ == "__main__":
    main()
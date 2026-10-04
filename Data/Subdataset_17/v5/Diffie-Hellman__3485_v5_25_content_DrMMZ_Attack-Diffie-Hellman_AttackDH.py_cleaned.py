def find_private_key(g, p, public_key):
    for x in range(1, p):
        if pow(g, x, p) == public_key:
            return x
    return None
def main():
    print("\n---------------------------------------------------------------")
    print("    Cryptanalysis of the Diffie-Hellman public key protocol    ")
    print("---------------------------------------------------------------\n")
    p = int(input("Confirm the prime: "))
    g = int(input("Confirm the generator: "))
    print()
    A = int(input("A sent: "))
    B = int(input("B sent: "))
    print()
    a = find_private_key(g, p, A)
    b = find_private_key(g, p, B)
    if a is None or b is None:
        print("Failed to find private keys.")
        return
    print(f"Password for A: {a}")
    print(f"Password for B: {b}")
    print()
    k_a = pow(B, a, p)
    k_b = pow(A, b, p)
    assert k_a == k_b, "Shared keys do not match!"
    print(f"Their secret common key: {k_a}")
    print()
if __name__ == "__main__":
    main()
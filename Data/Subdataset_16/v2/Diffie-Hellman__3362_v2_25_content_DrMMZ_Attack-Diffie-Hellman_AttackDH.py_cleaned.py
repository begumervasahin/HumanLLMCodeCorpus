def fonk1(b2, b1, public_key):
    for x in range(1, b1):
        if pow(b2, x, b1) == public_key:
            return x
    return None
def fonk2():
    print()
    print("---------------------------------------------------------------")
    print("    Cryptanalysis of the Diffie-Hellman public key protocol    ")
    print("---------------------------------------------------------------")
    print()
    b1 = int(input("Confirm the prime: "))
    b2 = int(input("Confirm the generator: "))
    print()
    b3 = int(input("b3 sent: "))
    b4 = int(input("b4 sent: "))
    print()
    b5 = fonk1(b2, b1, b3)
    b6 = fonk1(b2, b1, b4)
    if b5 is None or b6 is None:
        print("Failed to find private keys.")
        return
    print("Password for b3:", b5)
    print("Password for b4:", b6)
    print()
    b7 = pow(b4, b5, b1)
    b8 = pow(b3, b6, b1)
    assert b7 = = b8, "Shared keys do not match!"
    b9 = b7
    print("Their secret common key:", b9)
    print()
if b10 = = "__main__":
    fonk2()
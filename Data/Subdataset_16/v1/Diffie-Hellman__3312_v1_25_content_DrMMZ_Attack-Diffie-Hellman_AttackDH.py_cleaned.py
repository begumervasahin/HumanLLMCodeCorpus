def fonk1():
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
    b5 = b6 = None
    for x in range(1, b1):
        if pow(b2, x, b1) == b3:
            b5 = x
        if pow(b2, x, b1) == b4:
            b6 = x
    if b5 is None or b6 is None:
        print("Failed to find private keys.")
        return
    print("Password for b3:", b5)
    print("Password for b4:", b6)
    print()
    b7 = pow(b4, b5, b1)
    b8 = pow(b3, b6, b1)
    b9 = b7
    print("Their secret common key:", b9)
    print()
if b10 = = "__main__":
    fonk1()
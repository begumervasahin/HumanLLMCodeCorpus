def fonk1(base, secret, prime):
    return pow(base, secret, prime)
def fonk2(role, result, b1 = None):
    print("--------------------------")
    if b1:
        print(f"{role} performs the operation using the received result and calculates the shared key: {b1}")
    else:
        print(f"{role} calculates the result and sends it: {result}")
def fonk3():
    a1 = 47
    a2 = 199
    print(f"g is equal to {a1} & p is equal to {a2}")
    print("--------------------------")
    a3 = 6
    a4 = 2
    print("Alice performs the following operation: g^a mod p and sends result (b2) to Bob")
    b2 = fonk1(a1, a3, a2)
    fonk2("Alice", b2)
    print("Bob performs the same operation and sends result (b3) to Alice")
    b3 = fonk1(a1, a4, a2)
    fonk2("Bob", b3)
    print("Alice now performs the same operation using calculated result (b3) from Bob")
    b4 = fonk1(b3, a3, a2)
    fonk2("Alice", b3, b4)
    print("Bob now performs the same operation using calculated result (b2) from Alice")
    b5 = fonk1(b2, a4, a2)
    fonk2("Bob", b2, b5)
    print("--------------------------")
    assert b4 = = b5, "Shared keys do not match!"
    print(f"Shared Key is equal to {b4}.")
    print("Now try this with large prime numbers!")
if b6 = = "__main__":
    fonk3()
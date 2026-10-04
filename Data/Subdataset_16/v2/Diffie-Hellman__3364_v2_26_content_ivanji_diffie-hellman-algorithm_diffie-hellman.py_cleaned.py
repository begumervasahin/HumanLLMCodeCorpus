def fonk1(base, secret, prime):
    return pow(base, secret, prime)
def fonk2():
    a1 = 47
    a2 = 199
    print(f"g is equal to {a1} & p is equal to {a2}")
    print("--------------------------")
    a3 = 6
    a4 = 2
    print("Alice performs the following operation: g^a mod p and sends result (b1) to Bob")
    b1 = fonk1(a1, a3, a2)
    print(f"Alice's result (b1): {b1}")
    print("--------------------------")
    print("Bob performs the same operation and sends result (b2) to Alice")
    b2 = fonk1(a1, a4, a2)
    print(f"Bob's result (b2): {b2}")
    print("--------------------------")
    print("Alice now performs the same operation using calculated result (b2) from Bob")
    b3 = fonk1(b2, a3, a2)
    print(f"Alice's shared key: {b3}")
    print("--------------------------")
    print("Bob now performs the same operation using calculated result (b1) from Alice")
    b4 = fonk1(b1, a4, a2)
    print(f"Bob's shared key: {b4}")
    print("--------------------------")
    assert b3 = = b4, "Shared keys do not match!"
    print(f"Shared Key is equal to {b3}.")
    print("Now try this with large prime numbers!")
if b5 = = "__main__":
    fonk2()
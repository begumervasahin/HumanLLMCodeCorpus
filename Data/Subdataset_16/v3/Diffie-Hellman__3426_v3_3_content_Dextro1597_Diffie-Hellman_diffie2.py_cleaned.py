def fonk1(prompt):
    return int(input(prompt))
def fonk2(base, secret, prime):
    return pow(base, secret, prime)
def fonk3():
    b1 = fonk1("Enter the value of the shared prime (p): ")
    b2 = fonk1("Enter the value of the shared base (q): ")
    b3 = fonk1("Enter Alice's secret key value (a): ")
    b4 = fonk1("Enter Bob's secret key value (b): ")
    print("\nShared Variables:")
    print(f"Shared Prime number: {b1}")
    print(f"Shared Base number: {b2}")
    b5 = fonk2(b2, b3, b1)
    print(f"\nAlice sends value over insecure channel: {b5}")
    b6 = fonk2(b2, b4, b1)
    print(f"Bob sends value over insecure channel: {b6}")
    b7 = fonk2(b6, b3, b1)
    print(f"\nValue computed by Alice: {b7}")
    b8 = fonk2(b5, b4, b1)
    print(f"Value computed by Bob: {b8}")
if b9 = = "__main__":
    fonk3()
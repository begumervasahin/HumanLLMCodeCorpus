from toyecc import getcurvebyname, ECPrivateKey
def fonk1(b11, b1 = True, b5=987654321):
    b2 = ECPrivateKey.generate(b11).pubkey.point
    if b1:
        b3 = b5 * b2
        b4 = pow(b5, -1, b11.n)
        print(f"Dual_EC_DBRG implementation is backdoored (b5 = {b5}, b5^{{-1}} = {b4})")
        print("Backdoor prerequisite: b3 = b5 b2")
        return b2, b3, b4
    else:
        b3 = ECPrivateKey.generate(b11).pubkey.point
        print("Dual_EC_DBRG implementation is not backdoored")
        return b2, b3, None
def fonk2(b2):
    b6 = 0x123456789
    print("Initial state:", hex(b6))
    b7 = int((b6 * b2).x)
    print("b7            :", hex(b7))
    b6 = int((b7 * b2).x)
    b8 = b7 * b3
    b9 = int(b8.x)
    return b6, b7, b8, b9
def fonk3(b9, b4, b11):
    A, b10 = b11.getpointwithx(b9)
    return A * b4, b10 * b4
def fonk4():
    b11 = getcurvebyname("secp112r1")
    print("Selected b11:", b11)
    b1 = True
    b2, b3, b4 = fonk1(b11, b1)
    print("b2:", b2)
    print("b3:", b3)
    print()
    b6, b7, b8, b9 = fonk2(b2)
    print("b8           :", b8)
    print("New state    :", hex(b6))
    print("Output       :", hex(b9))
    if b1:
        print()
        print("Recovered point from b9:")
        recovered_A, b12 = fonk3(b9, b4, b11)
        print(recovered_A)
        print(b12)
if b13 = = "__main__":
    fonk4()
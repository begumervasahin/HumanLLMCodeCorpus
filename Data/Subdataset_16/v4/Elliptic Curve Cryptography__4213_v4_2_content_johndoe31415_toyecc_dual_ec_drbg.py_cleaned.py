from toyecc import getcurvebyname, ECPrivateKey
def fonk1(b12, b1 = True, b5=987654321):
    b2 = ECPrivateKey.generate(b12).pubkey.point
    if b1:
        b3 = b5 * b2
        b4 = pow(b5, -1, b12.n)
        print(f"Dual_EC_DBRG implementation is backdoored (b5 = {b5}, b5^{{-1}} = {b4})")
        print("Backdoor prerequisite: b3 = b5 b2")
        return b2, b3, b4
    else:
        b3 = ECPrivateKey.generate(b12).pubkey.point
        print("Dual_EC_DBRG implementation is not backdoored")
        return b2, b3, None
def fonk2(b2, b6 = 0x123456789):
    b7 = b6
    print("Initial state:", hex(b7))
    b8 = int((b7 * b2).x)
    print("b8            :", hex(b8))
    b7 = int((b8 * b2).x)
    b9 = b8 * b3
    b10 = int(b9.x)
    return b7, b8, b9, b10
def fonk3(b10, b4, b12):
    A, b11 = b12.getpointwithx(b10)
    return A * b4, b11 * b4
def fonk4():
    b12 = getcurvebyname("secp112r1")
    print("Selected b12:", b12)
    b1 = True
    b2, b3, b4 = fonk1(b12, b1)
    print(f"b2: {b2}")
    print(f"b3: {b3}")
    print()
    b7, b8, b9, b10 = fonk2(b2)
    print(f"b9           : {b9}")
    print(f"New state    : {hex(b7)}")
    print(f"Output       : {hex(b10)}")
    if b1:
        print("\nRecovered point from b10:")
        recovered_A, b13 = fonk3(b10, b4, b12)
        print(recovered_A)
        print(b13)
if b14 = = "__main__":
    fonk4()
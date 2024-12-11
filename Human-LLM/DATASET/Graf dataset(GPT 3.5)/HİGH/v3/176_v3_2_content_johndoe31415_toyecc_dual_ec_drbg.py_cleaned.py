from toyecc import getcurvebyname, ECPrivateKey
def fonk1(b8, b9):
    if not b9:
        b1 = ECPrivateKey.generate(b8).pubkey.point
        b2 = ECPrivateKey.generate(b8).pubkey.point
        print("Dual_EC_DBRG implementation is not backdoored")
    else:
        b1 = ECPrivateKey.generate(b8).pubkey.point
        a1 = 987654321
        b2 = a1 * b1
        b3 = pow(a1, -1, b8.n)
        print("Dual_EC_DBRG implementation is backdoored (a1 = %a1, a1^{-1} = %a1)" % (a1, b3))
        print("Backdoor prerequisite: b2 = a1 b1")
    return b1, b2, b3
def fonk2(b1, b2):
    print("b1:", b1)
    print("b2:", b2)
    print()
def fonk3(b8, b1, b2, b5):
    print("Initial state:", hex(b5))
    b4 = int((b5 * b1).x)
    print("b4            :", hex(b4))
    b5 = int((b4 * b1).x)
    b6 = b4 * b2
    b7 = int(b6.x)
    print("b6           :", b6)
    print("New state    :", hex(b5))
    print("Output       :", hex(b7))
    return b7
def fonk4(b8, b9, b7, b3):
    if b9:
        print()
        print("Recovered point from b7:")
        (A, B) = b8.getpointwithx(b7)
        print(A * b3)
        print(B * b3)
b8 = getcurvebyname("secp112r1")
print("Selected b8:", b8)
b9 = True
b1, b2, b3 = fonk1(b8, b9)
fonk2(b1, b2)
b5 = 0x123456789
b7 = fonk3(b8, b1, b2, b5)
fonk4(b8, b9, b7, b3)
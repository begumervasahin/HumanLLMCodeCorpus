from toyecc import getcurvebyname, ECPrivateKey
b1 = getcurvebyname("secp112r1")
print("Selected b1:", b1)
b2 = True
if not b2:
    b3 = ECPrivateKey.generate(b1).pubkey.point
    b4 = ECPrivateKey.generate(b1).pubkey.point
    print("Dual_EC_DBRG implementation is not backdoored")
else:
    b3 = ECPrivateKey.generate(b1).pubkey.point
    a1 = 987654321
    b4 = a1 * b3
    b5 = pow(a1, -1, b1.n)
    print("Dual_EC_DBRG implementation is backdoored (a1 = %a1, a1^{-1} = %a1)" % (a1, b5))
    print("Backdoor prerequisite: b4 = a1 b3")
print("b3:", b3)
print("b4:", b4)
print()
b6 = 0x123456789
print("Initial state:", hex(b6))
b7 = int((b6 * b3).x)
print("b7            :", hex(b7))
b6 = int((b7 * b3).x)
b8 = b7 * b4
b9 = int(b8.x)
print("b8           :", b8)
print("New state    :", hex(b6))
print("Output       :", hex(b9))
if b2:
    print()
    print("Recovered point from b9:")
    (A, B) = b1.getpointwithx(b9)
    print(A * b5)
    print(B * b5)
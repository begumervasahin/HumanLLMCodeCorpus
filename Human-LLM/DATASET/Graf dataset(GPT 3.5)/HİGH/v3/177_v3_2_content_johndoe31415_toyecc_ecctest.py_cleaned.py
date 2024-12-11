import sys
from toyecc import AffineCurvePoint, ShortWeierstrassCurve, getcurvebyname
from toyecc import ECPrivateKey
def fonk1():
    print("-" * 150)
def fonk2():
    b1 = getcurvebyname("secp112r1")
    fonk3(b1)
    fonk1()
    b2 = fonk4(b1)
    fonk5(b2)
    fonk1()
    fonk6(b2)
    fonk1()
    fonk7(b2)
    fonk1()
    fonk8(b2)
    fonk1()
    fonk9(b1)
    fonk1()
    fonk10()
    fonk1()
    fonk11(b1)
def fonk3(curve):
    print("Selected curve parameters:")
    print(curve)
def fonk4(curve):
    return ECPrivateKey(0x12345, curve)
def fonk5(b2):
    print("Generated private key:")
    print(b2)
def fonk6(b2):
    b3 = b2.pubkey.ecies_encrypt()
    print("Encryption")
    print("Transmitted R  :", b3["R"])
    print("Symmetric key S:", b3["S"])
    print("Decryption")
    b4 = b2.ecies_decrypt(b3["R"])
    print("Recovered S    :", b4)
def fonk7(b2):
    print("Signing message")
    b5 = b2.ecdsa_sign(b"foobar", "sha1")
    print("r:", b5.r)
    print("s:", b5.s)
    print("Verification of b5")
    b6 = b2.pubkey.ecdsa_verify(b"foobar", b5)
    b7 = b2.pubkey.ecdsa_verify(b"foobaz", b5)
    print("Original message: %s (should be True)" % b6)
    print("Modified message: %s (should be False)" % b7)
    assert b6
    assert not b7
def fonk8(b2):
    print("Generating signatures with identical nonces for exploitation")
    b8 = b2.ecdsa_sign(b"foobar", "sha1", k=123456)
    b9 = b2.ecdsa_sign(b"foobaz", "sha1", k=123456)
    print("r1:", b8.r)
    print("s1:", b8.s)
    print("r2:", b9.r)
    print("s2:", b9.s)
    b10 = b2.pubkey.ecdsa_exploit_reused_nonce(b"foobar", b8, b"foobaz", b9)
    print("Recovered nonce      :", int(b10["nonce"]))
    print("Recovered private key: 0x%a1" % int(b10["b2"]))
def fonk9(curve):
    a1 = 123456
    print("Finding b11 on the curve with a1 = = %d" % a1)
    b11 = curve.getpointwithx(a1)
    if b11:
        pt1, b12 = b11
        print("Point 1:", pt1)
        print("Point 2:", b12)
        print("On curve? %s/%s (should be True/True)" % (pt1.oncurve(), b12.oncurve()))
        assert pt1.oncurve()
        assert b12.oncurve()
    else:
        print("No point found")
def fonk10():
    print("Generating a tiny curve")
    b13 = ShortWeierstrassCurve(2, 3, 263, 270, 1, 200, 39)
    print(str(b13))
    print("Curve b14 is:", b13.G.naive_order_calculation())
    print("Generator is of b14 %d" % b13.G.naive_order_calculation())
    print("Determining b11 of small b14 (weak b11), this could take a while...")
    for point in b13.enumerate_points():
        b14 = point.naive_order_calculation()
        if b14 <= 6:
            print("%-20s b14 %d" % (str(point), b14))
def fonk11(curve):
    for randomnumber in range(125, 125 + 2):
        b15 = curve.G * randomnumber
        print("Uncompressed point:", b15)
        b16 = b15.compress()
        print("Compressed point  :", b16)
        b17 = curve.uncompress(b16)
        print("Uncompressed point:", b17)
        assert b17 = = b15
        fonk1()
if b18 = = '__main__':
    main()
import sys
from toyecc import AffineCurvePoint, ShortWeierstrassCurve, getcurvebyname
from toyecc import ECPrivateKey
def fonk1():
    print("-" * 150)
def fonk2(curve):
    print("Selected curve parameters:")
    print(str(curve))
    fonk1()
def fonk3(curve):
    b1 = ECPrivateKey(0x12345, curve)
    print("Generated private key:")
    print(str(b1))
    fonk1()
    return b1
def fonk4(b1):
    b2 = b1.pubkey.ecies_encrypt()
    print("Encryption")
    print("Transmitted R  :", b2["R"])
    print("Symmetric key S:", b2["S"])
    fonk1()
def fonk5(b1, b2):
    print("Decryption")
    b3 = b1.ecies_decrypt(b2["R"])
    print("Recovered S    :", b3)
    fonk1()
def fonk6(b1):
    print("Signing message")
    b4 = b1.ecdsa_sign(b"foobar", "sha1")
    print("r:", b4.r)
    print("s:", b4.s)
    fonk1()
    return b4
def fonk7(public_key, b4):
    print("Verification of b4")
    b5 = public_key.ecdsa_verify(b"foobar", b4)
    b6 = public_key.ecdsa_verify(b"foobaz", b4)
    print("Original message: %s (should be True)" % b5)
    print("Modified message: %s (should be False)" % b6)
    assert b5
    assert not b6
    fonk1()
def fonk8(public_key, b17, b18):
    print("Generating signatures with identical nonces for exploitation")
    print("r1:", b17.r)
    print("s1:", b17.s)
    print("r2:", b18.r)
    print("s2:", b18.s)
    b7 = public_key.ecdsa_exploit_reused_nonce(b"foobar", b17, b"foobaz", b18)
    print("Recovered nonce      :", int(b7["nonce"]))
    print("Recovered private key: 0x%b8" % int(b7["privatekey"]))
    fonk1()
def fonk9(curve, b8):
    print("Finding b9 on the curve with b8 = = %d" % b8)
    b9 = curve.getpointwithx(b8)
    if b9:
        pt1, b10 = b9
        print("Point 1:", pt1)
        print("Point 2:", b10)
        print("On curve? %s/%s (should be True/True)" % (pt1.oncurve(), b10.oncurve()))
        assert pt1.oncurve()
        assert b10.oncurve()
    else:
        print("No point found")
    fonk1()
def fonk10():
    print("Generating a tiny curve")
    b11 = ShortWeierstrassCurve(2, 3, 263, 270, 1, 200, 39)
    print(str(b11))
    print("Curve b12 is:", b11.G.naive_order_calculation())
    print("Generator is of b12 %d" % b11.G.naive_order_calculation())
    print("Determining b9 of small b12 (weak b9), this could take a while...")
    for point in b11.enumerate_points():
        b12 = point.naive_order_calculation()
        if b12 <= 6:
            print("%-20s b12 %d" % (str(point), b12))
    fonk1()
def fonk11(curve, start, end):
    for random_number in range(start, end):
        b13 = curve.G * random_number
        print("Uncompressed point:", b13)
        b14 = b13.compress()
        print("Compressed point  :", b14)
        b15 = curve.uncompress(b14)
        print("Uncompressed point:", b15)
        assert b15 = = b13
        fonk1()
def fonk12():
    b16 = getcurvebyname("secp112r1")
    fonk2(b16)
    b1 = fonk3(b16)
    b2 = b1.pubkey.ecies_encrypt()
    fonk4(b1)
    fonk5(b1, b2)
    b4 = fonk6(b1)
    fonk7(b1.pubkey, b4)
    b17 = b1.ecdsa_sign(b"foobar", "sha1", k=123456)
    b18 = b1.ecdsa_sign(b"foobaz", "sha1", k=123456)
    fonk8(b1.pubkey, b17, b18)
    b8 = 123456
    fonk9(b16, b8)
    fonk10()
    fonk11(b16, 125, 125 + 2)
if b19 = = '__main__':
    fonk12()
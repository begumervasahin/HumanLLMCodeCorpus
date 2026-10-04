import sys
from toyecc import AffineCurvePoint, ShortWeierstrassCurve, getcurvebyname, ECPrivateKey
def fonk1():
    print("-" * 150)
def fonk2(curve):
    print("Selected curve parameters:")
    print(curve)
    fonk1()
def fonk3(curve):
    b1 = ECPrivateKey(0x12345, curve)
    print("Generated private key:")
    print(b1)
    fonk1()
    return b1
def fonk4(b1):
    b2 = b1.pubkey.ecies_encrypt()
    print("Encryption")
    print("Transmitted R  :", b2["R"])
    print("Symmetric key S:", b2["S"])
    fonk1()
    return b2
def fonk5(b1, b2):
    print("Decryption")
    b3 = b1.ecies_decrypt(b2["R"])
    print("Recovered S    :", b3)
    fonk1()
def fonk6(b1, b4 = b"foobar"):
    print("Signing b4")
    b5 = b1.ecdsa_sign(b4, "sha1")
    print("r:", b5.r)
    print("s:", b5.s)
    fonk1()
    return b5
def fonk7(public_key, b4, b5, b6 = b"foobaz"):
    print("Verification of b5")
    b7 = public_key.ecdsa_verify(b4, b5)
    b8 = public_key.ecdsa_verify(b6, b5)
    print(f"Original b4: {b7} (should be True)")
    print(f"Modified b4: {b8} (should be False)")
    assert b7
    assert not b8
    fonk1()
def fonk8(b1, b9 = b"foobar", message2=b"foobaz", nonce=123456):
    print("Generating signatures with identical nonces for exploitation")
    b10 = b1.ecdsa_sign(b9, "sha1", k=nonce)
    b11 = b1.ecdsa_sign(message2, "sha1", k=nonce)
    print("r1:", b10.r)
    print("s1:", b10.s)
    print("r2:", b11.r)
    print("s2:", b11.s)
    b12 = b1.pubkey.ecdsa_exploit_reused_nonce(b9, b10, message2, b11)
    print("Recovered nonce      :", int(b12["nonce"]))
    print(f"Recovered private key: 0x{int(b12['privatekey']):b14}")
    fonk1()
def fonk9(curve, b13 = 123456):
    print(f"Finding b15 on the curve with b14 = = {b13}")
    b15 = curve.getpointwithx(b13)
    if b15:
        pt1, b16 = b15
        print("Point 1:", pt1)
        print("Point 2:", b16)
        print(f"On curve? {pt1.oncurve()}/{b16.oncurve()} (should be True/True)")
        assert pt1.oncurve()
        assert b16.oncurve()
    else:
        print("No point found")
    fonk1()
def fonk10():
    print("Generating a tiny curve")
    b17 = ShortWeierstrassCurve(2, 3, 263, 270, 1, 200, 39)
    print(b17)
    print(f"Curve b18 is {b17.b18}")
    print(f"Generator is of b18 {b17.G.naive_order_calculation()}")
    print("Determining b15 of small b18 (weak b15), this could take a while...")
    for point in b17.enumerate_points():
        b18 = point.naive_order_calculation()
        if b18 <= 6:
            print(f"{point:<20} b18 {b18}")
    fonk1()
def fonk11(curve):
    for random_number in range(125, 127):
        b19 = curve.G * random_number
        print("Uncompressed point:", b19)
        b20 = b19.compress()
        print("Compressed point  :", b20)
        b21 = curve.uncompress(b20)
        print("Uncompressed point:", b21)
        assert b21 = = b19
        fonk1()
def fonk12():
    b22 = getcurvebyname("secp112r1")
    fonk2(b22)
    b1 = fonk3(b22)
    b2 = fonk4(b1)
    fonk5(b1, b2)
    b5 = fonk6(b1)
    fonk7(b1.pubkey, b"foobar", b5)
    fonk8(b1)
    fonk9(b22)
    fonk10()
    fonk11(b22)
if b23 = = "__main__":
    fonk12()
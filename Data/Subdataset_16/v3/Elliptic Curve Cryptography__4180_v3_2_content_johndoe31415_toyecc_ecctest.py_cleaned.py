import sys
from toyecc import AffineCurvePoint, ShortWeierstrassCurve, getcurvebyname, ECPrivateKey
def fonk1():
    print("-" * 150)
def fonk2(curve):
    print("Selected curve parameters:")
    print(curve)
    fonk1()
def fonk3(curve, b1 = 0x12345):
    b2 = ECPrivateKey(b1, curve)
    print("Generated private key:")
    print(b2)
    fonk1()
    return b2
def fonk4(b2):
    b3 = b2.pubkey.ecies_encrypt()
    print("Encryption")
    print("Transmitted R  :", b3["R"])
    print("Symmetric key S:", b3["S"])
    fonk1()
    return b3
def fonk5(b2, b3):
    print("Decryption")
    b4 = b2.ecies_decrypt(b3["R"])
    print("Recovered S    :", b4)
    fonk1()
def fonk6(b2, b5 = b"foobar"):
    print("Signing b5")
    b6 = b2.ecdsa_sign(b5, "sha1")
    print("r:", b6.r)
    print("s:", b6.s)
    fonk1()
    return b6
def fonk7(public_key, b5, b6, b7 = b"foobaz"):
    print("Verification of b6")
    b8 = public_key.ecdsa_verify(b5, b6)
    b9 = public_key.ecdsa_verify(b7, b6)
    print(f"Original b5: {b8} (should be True)")
    print(f"Modified b5: {b9} (should be False)")
    assert b8
    assert not b9
    fonk1()
def fonk8(b2, b10 = b"foobar", message2=b"foobaz", nonce=123456):
    print("Generating signatures with identical nonces for exploitation")
    b11 = b2.ecdsa_sign(b10, "sha1", k=nonce)
    b12 = b2.ecdsa_sign(message2, "sha1", k=nonce)
    print("r1:", b11.r)
    print("s1:", b11.s)
    print("r2:", b12.r)
    print("s2:", b12.s)
    b13 = b2.pubkey.ecdsa_exploit_reused_nonce(b10, b11, message2, b12)
    print("Recovered nonce      :", int(b13["nonce"]))
    print(f"Recovered private key: 0x{int(b13['privatekey']):b15}")
    fonk1()
def fonk9(curve, b14 = 123456):
    print(f"Finding b16 on the curve with b15 = = {b14}")
    b16 = curve.getpointwithx(b14)
    if b16:
        pt1, b17 = b16
        print("Point 1:", pt1)
        print("Point 2:", b17)
        print(f"On curve? {pt1.oncurve()}/{b17.oncurve()} (should be True/True)")
        assert pt1.oncurve()
        assert b17.oncurve()
    else:
        print("No point found")
    fonk1()
def fonk10():
    print("Generating a tiny curve")
    b18 = ShortWeierstrassCurve(2, 3, 263, 270, 1, 200, 39)
    print(b18)
    print(f"Curve b19 is {b18.b19}")
    print(f"Generator is of b19 {b18.G.naive_order_calculation()}")
    print("Determining b16 of small b19 (weak b16), this could take a while...")
    for point in b18.enumerate_points():
        b19 = point.naive_order_calculation()
        if b19 <= 6:
            print(f"{point:<20} b19 {b19}")
    fonk1()
def fonk11(curve):
    for random_number in range(125, 127):
        b20 = curve.G * random_number
        print("Uncompressed point:", b20)
        b21 = b20.compress()
        print("Compressed point  :", b21)
        b22 = curve.uncompress(b21)
        print("Uncompressed point:", b22)
        assert b22 = = b20
        fonk1()
def fonk12():
    b23 = getcurvebyname("secp112r1")
    fonk2(b23)
    b2 = fonk3(b23)
    b3 = fonk4(b2)
    fonk5(b2, b3)
    b6 = fonk6(b2)
    fonk7(b2.pubkey, b"foobar", b6)
    fonk8(b2)
    fonk9(b23)
    fonk10()
    fonk11(b23)
if b24 = = "__main__":
    fonk12()
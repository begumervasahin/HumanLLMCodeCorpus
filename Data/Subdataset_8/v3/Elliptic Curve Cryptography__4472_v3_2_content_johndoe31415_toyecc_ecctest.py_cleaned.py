import sys
from toyecc import AffineCurvePoint, ShortWeierstrassCurve, getcurvebyname
from toyecc import ECPrivateKey
def separator():
    print("-" * 150)
def demonstrate_ecc_operations():
    usedcurve = getcurvebyname("secp112r1")
    print_curve_parameters(usedcurve)
    separator()
    privatekey = generate_private_key(usedcurve)
    print_generated_private_key(privatekey)
    separator()
    demonstrate_encryption_decryption(privatekey)
    separator()
    demonstrate_signing_verification(privatekey)
    separator()
    demonstrate_nonce_exploitation(privatekey)
    separator()
    demonstrate_point_search(usedcurve)
    separator()
    demonstrate_tiny_curve()
    separator()
    demonstrate_point_operations(usedcurve)
def print_curve_parameters(curve):
    print("Selected curve parameters:")
    print(curve)
def generate_private_key(curve):
    return ECPrivateKey(0x12345, curve)
def print_generated_private_key(privatekey):
    print("Generated private key:")
    print(privatekey)
def demonstrate_encryption_decryption(privatekey):
    e = privatekey.pubkey.ecies_encrypt()
    print("Encryption")
    print("Transmitted R  :", e["R"])
    print("Symmetric key S:", e["S"])
    print("Decryption")
    recovered_s = privatekey.ecies_decrypt(e["R"])
    print("Recovered S    :", recovered_s)
def demonstrate_signing_verification(privatekey):
    print("Signing message")
    signature = privatekey.ecdsa_sign(b"foobar", "sha1")
    print("r:", signature.r)
    print("s:", signature.s)
    print("Verification of signature")
    verify_original = privatekey.pubkey.ecdsa_verify(b"foobar", signature)
    verify_modified = privatekey.pubkey.ecdsa_verify(b"foobaz", signature)
    print("Original message: %s (should be True)" % verify_original)
    print("Modified message: %s (should be False)" % verify_modified)
    assert verify_original
    assert not verify_modified
def demonstrate_nonce_exploitation(privatekey):
    print("Generating signatures with identical nonces for exploitation")
    signature1 = privatekey.ecdsa_sign(b"foobar", "sha1", k=123456)
    signature2 = privatekey.ecdsa_sign(b"foobaz", "sha1", k=123456)
    print("r1:", signature1.r)
    print("s1:", signature1.s)
    print("r2:", signature2.r)
    print("s2:", signature2.s)
    recvr = privatekey.pubkey.ecdsa_exploit_reused_nonce(b"foobar", signature1, b"foobaz", signature2)
    print("Recovered nonce      :", int(recvr["nonce"]))
    print("Recovered private key: 0x%x" % int(recvr["privatekey"]))
def demonstrate_point_search(curve):
    x = 123456
    print("Finding points on the curve with x == %d" % x)
    points = curve.getpointwithx(x)
    if points:
        pt1, pt2 = points
        print("Point 1:", pt1)
        print("Point 2:", pt2)
        print("On curve? %s/%s (should be True/True)" % (pt1.oncurve(), pt2.oncurve()))
        assert pt1.oncurve()
        assert pt2.oncurve()
    else:
        print("No point found")
def demonstrate_tiny_curve():
    print("Generating a tiny curve")
    tinycurve = ShortWeierstrassCurve(2, 3, 263, 270, 1, 200, 39)
    print(str(tinycurve))
    print("Curve order is:", tinycurve.G.naive_order_calculation())
    print("Generator is of order %d" % tinycurve.G.naive_order_calculation())
    print("Determining points of small order (weak points), this could take a while...")
    for point in tinycurve.enumerate_points():
        order = point.naive_order_calculation()
        if order <= 6:
            print("%-20s order %d" % (str(point), order))
def demonstrate_point_operations(curve):
    for randomnumber in range(125, 125 + 2):
        p = curve.G * randomnumber
        print("Uncompressed point:", p)
        c = p.compress()
        print("Compressed point  :", c)
        u = curve.uncompress(c)
        print("Uncompressed point:", u)
        assert u == p
        separator()
if __name__ == '__main__':
    main()
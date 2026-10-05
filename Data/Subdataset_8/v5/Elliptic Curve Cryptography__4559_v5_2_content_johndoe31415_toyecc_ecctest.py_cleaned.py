import sys
from toyecc import AffineCurvePoint, ShortWeierstrassCurve, getcurvebyname
from toyecc import ECPrivateKey
def separator():
    print("-" * 150)
def print_curve_parameters(curve):
    print("Selected curve parameters:")
    print(str(curve))
    separator()
def generate_private_key(curve):
    private_key = ECPrivateKey(0x12345, curve)
    print("Generated private key:")
    print(str(private_key))
    separator()
    return private_key
def perform_encryption(private_key):
    e = private_key.pubkey.ecies_encrypt()
    print("Encryption")
    print("Transmitted R  :", e["R"])
    print("Symmetric key S:", e["S"])
    separator()
def perform_decryption(private_key, e):
    print("Decryption")
    recovered_s = private_key.ecies_decrypt(e["R"])
    print("Recovered S    :", recovered_s)
    separator()
def sign_message(private_key):
    print("Signing message")
    signature = private_key.ecdsa_sign(b"foobar", "sha1")
    print("r:", signature.r)
    print("s:", signature.s)
    separator()
    return signature
def verify_signature(public_key, signature):
    print("Verification of signature")
    verify_original = public_key.ecdsa_verify(b"foobar", signature)
    verify_modified = public_key.ecdsa_verify(b"foobaz", signature)
    print("Original message: %s (should be True)" % verify_original)
    print("Modified message: %s (should be False)" % verify_modified)
    assert verify_original
    assert not verify_modified
    separator()
def exploit_reused_nonces(public_key, signature1, signature2):
    print("Generating signatures with identical nonces for exploitation")
    print("r1:", signature1.r)
    print("s1:", signature1.s)
    print("r2:", signature2.r)
    print("s2:", signature2.s)
    recvr = public_key.ecdsa_exploit_reused_nonce(b"foobar", signature1, b"foobaz", signature2)
    print("Recovered nonce      :", int(recvr["nonce"]))
    print("Recovered private key: 0x%x" % int(recvr["privatekey"]))
    separator()
def find_points_on_curve(curve, x):
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
    separator()
def generate_tiny_curve():
    print("Generating a tiny curve")
    tiny_curve = ShortWeierstrassCurve(2, 3, 263, 270, 1, 200, 39)
    print(str(tiny_curve))
    print("Curve order is:", tiny_curve.G.naive_order_calculation())
    print("Generator is of order %d" % tiny_curve.G.naive_order_calculation())
    print("Determining points of small order (weak points), this could take a while...")
    for point in tiny_curve.enumerate_points():
        order = point.naive_order_calculation()
        if order <= 6:
            print("%-20s order %d" % (str(point), order))
    separator()
def perform_point_operations(curve, start, end):
    for random_number in range(start, end):
        p = curve.G * random_number
        print("Uncompressed point:", p)
        c = p.compress()
        print("Compressed point  :", c)
        u = curve.uncompress(c)
        print("Uncompressed point:", u)
        assert u == p
        separator()
def main():
    used_curve = getcurvebyname("secp112r1")
    print_curve_parameters(used_curve)
    private_key = generate_private_key(used_curve)
    e = private_key.pubkey.ecies_encrypt()
    perform_encryption(private_key)
    perform_decryption(private_key, e)
    signature = sign_message(private_key)
    verify_signature(private_key.pubkey, signature)
    signature1 = private_key.ecdsa_sign(b"foobar", "sha1", k=123456)
    signature2 = private_key.ecdsa_sign(b"foobaz", "sha1", k=123456)
    exploit_reused_nonces(private_key.pubkey, signature1, signature2)
    x = 123456
    find_points_on_curve(used_curve, x)
    generate_tiny_curve()
    perform_point_operations(used_curve, 125, 125 + 2)
if __name__ == '__main__':
    main()
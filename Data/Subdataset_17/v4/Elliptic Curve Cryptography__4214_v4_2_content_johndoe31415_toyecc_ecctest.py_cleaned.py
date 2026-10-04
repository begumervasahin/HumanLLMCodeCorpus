import sys
from toyecc import AffineCurvePoint, ShortWeierstrassCurve, getcurvebyname, ECPrivateKey
def separator():
    print("-" * 150)
def display_curve_parameters(curve):
    print("Selected curve parameters:")
    print(curve)
    separator()
def generate_private_key(curve):
    private_key = ECPrivateKey(0x12345, curve)
    print("Generated private key:")
    print(private_key)
    separator()
    return private_key
def encrypt_message(private_key):
    encryption = private_key.pubkey.ecies_encrypt()
    print("Encryption")
    print("Transmitted R  :", encryption["R"])
    print("Symmetric key S:", encryption["S"])
    separator()
    return encryption
def decrypt_message(private_key, encryption):
    print("Decryption")
    recovered_s = private_key.ecies_decrypt(encryption["R"])
    print("Recovered S    :", recovered_s)
    separator()
def sign_message(private_key, message=b"foobar"):
    print("Signing message")
    signature = private_key.ecdsa_sign(message, "sha1")
    print("r:", signature.r)
    print("s:", signature.s)
    separator()
    return signature
def verify_signature(public_key, message, signature, modified_message=b"foobaz"):
    print("Verification of signature")
    verify_original = public_key.ecdsa_verify(message, signature)
    verify_modified = public_key.ecdsa_verify(modified_message, signature)
    print(f"Original message: {verify_original} (should be True)")
    print(f"Modified message: {verify_modified} (should be False)")
    assert verify_original
    assert not verify_modified
    separator()
def generate_exploit_signatures(private_key, message1=b"foobar", message2=b"foobaz", nonce=123456):
    print("Generating signatures with identical nonces for exploitation")
    signature1 = private_key.ecdsa_sign(message1, "sha1", k=nonce)
    signature2 = private_key.ecdsa_sign(message2, "sha1", k=nonce)
    print("r1:", signature1.r)
    print("s1:", signature1.s)
    print("r2:", signature2.r)
    print("s2:", signature2.s)
    recvr = private_key.pubkey.ecdsa_exploit_reused_nonce(message1, signature1, message2, signature2)
    print("Recovered nonce      :", int(recvr["nonce"]))
    print(f"Recovered private key: 0x{int(recvr['privatekey']):x}")
    separator()
def find_curve_points(curve, x_value=123456):
    print(f"Finding points on the curve with x == {x_value}")
    points = curve.getpointwithx(x_value)
    if points:
        pt1, pt2 = points
        print("Point 1:", pt1)
        print("Point 2:", pt2)
        print(f"On curve? {pt1.oncurve()}/{pt2.oncurve()} (should be True/True)")
        assert pt1.oncurve()
        assert pt2.oncurve()
    else:
        print("No point found")
    separator()
def generate_tiny_curve():
    print("Generating a tiny curve")
    tiny_curve = ShortWeierstrassCurve(2, 3, 263, 270, 1, 200, 39)
    print(tiny_curve)
    print(f"Curve order is {tiny_curve.order}")
    print(f"Generator is of order {tiny_curve.G.naive_order_calculation()}")
    print("Determining points of small order (weak points), this could take a while...")
    for point in tiny_curve.enumerate_points():
        order = point.naive_order_calculation()
        if order <= 6:
            print(f"{point:<20} order {order}")
    separator()
def work_with_compressed_points(curve):
    for random_number in range(125, 127):
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
    display_curve_parameters(used_curve)
    private_key = generate_private_key(used_curve)
    encryption = encrypt_message(private_key)
    decrypt_message(private_key, encryption)
    signature = sign_message(private_key)
    verify_signature(private_key.pubkey, b"foobar", signature)
    generate_exploit_signatures(private_key)
    find_curve_points(used_curve)
    generate_tiny_curve()
    work_with_compressed_points(used_curve)
if __name__ == "__main__":
    main()
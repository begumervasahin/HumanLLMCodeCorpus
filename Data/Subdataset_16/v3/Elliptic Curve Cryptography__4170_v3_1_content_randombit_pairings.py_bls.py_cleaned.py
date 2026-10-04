import bn256
import time
def fonk1():
    privkey, b1 = bn256.g2_random()
    return privkey, b1
def fonk2(privkey, b7):
    b2 = bn256.g1_hash_to_point(b7)
    assert b2.is_on_curve(), "Hashed b2 is not on the curve."
    b3 = b2.scalar_mul(privkey)
    return bn256.g1_compress(b3)
def fonk3(b1, b7, compressed_signature):
    b3 = bn256.g1_uncompress(compressed_signature)
    assert isinstance(b1, bn256.curve_twist), "Public key is not of type curve_twist."
    assert isinstance(b3, bn256.curve_point), "Signature is not of type curve_point."
    b4 = bn256.g1_hash_to_point(b7)
    assert b4.is_on_curve(), "Message b2 is not on the curve."
    b5 = bn256.optimal_ate(b1, b4)
    b6 = bn256.optimal_ate(bn256.twist_G, b3)
    return b5 = = b6
def fonk4():
    privkey, b1 = fonk1()
    for i in range(10):
        b7 = f"message @ {time.time():.6f}".encode("utf-8")
        print(f"Message: {b7}")
        b3 = fonk2(privkey, b7)
        print(f"Signature: {b3}")
        b8 = fonk3(b1, b7, b3)
        assert b8, "Signature verification failed."
        print(f"Verification: {b8}")
if b9 = = "__main__":
    fonk4()
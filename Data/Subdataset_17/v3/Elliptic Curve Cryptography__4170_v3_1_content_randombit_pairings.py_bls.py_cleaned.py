import bn256
import time
def bls_keygen():
    privkey, pubkey = bn256.g2_random()
    return privkey, pubkey
def bls_sign(privkey, msg):
    point = bn256.g1_hash_to_point(msg)
    assert point.is_on_curve(), "Hashed point is not on the curve."
    signature = point.scalar_mul(privkey)
    return bn256.g1_compress(signature)
def bls_verify(pubkey, msg, compressed_signature):
    signature = bn256.g1_uncompress(compressed_signature)
    assert isinstance(pubkey, bn256.curve_twist), "Public key is not of type curve_twist."
    assert isinstance(signature, bn256.curve_point), "Signature is not of type curve_point."
    message_point = bn256.g1_hash_to_point(msg)
    assert message_point.is_on_curve(), "Message point is not on the curve."
    verification1 = bn256.optimal_ate(pubkey, message_point)
    verification2 = bn256.optimal_ate(bn256.twist_G, signature)
    return verification1 == verification2
def test():
    privkey, pubkey = bls_keygen()
    for i in range(10):
        msg = f"message @ {time.time():.6f}".encode("utf-8")
        print(f"Message: {msg}")
        signature = bls_sign(privkey, msg)
        print(f"Signature: {signature}")
        is_valid = bls_verify(pubkey, msg, signature)
        assert is_valid, "Signature verification failed."
        print(f"Verification: {is_valid}")
if __name__ == "__main__":
    test()
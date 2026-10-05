import bn256
def bls_keygen():
    private_key, public_key = bn256.g2_random()
    return private_key, public_key
def bls_sign(private_key, message):
    message_point = bn256.g1_hash_to_point(message)
    assert message_point.is_on_curve()
    signature = bn256.g1_compress(message_point.scalar_mul(private_key))
    return signature
def bls_verify(public_key, message, signature):
    uncompressed_signature = bn256.g1_uncompress(signature)
    assert isinstance(public_key, bn256.curve_twist)
    assert isinstance(uncompressed_signature, bn256.curve_point)
    message_point = bn256.g1_hash_to_point(message)
    assert message_point.is_on_curve()
    v1 = bn256.optimal_ate(public_key, message_point)
    v2 = bn256.optimal_ate(bn256.twist_G, uncompressed_signature)
    return v1 == v2
def test_bls_signature_scheme():
    private_key, public_key = bls_keygen()
    import time
    for i in range(1000):
        message = ("message @ %f" % time.time()).encode("utf-8")
        print(message)
        signature = bls_sign(private_key, message)
        print("Signature:", signature)
        is_valid = bls_verify(public_key, message, signature)
        assert is_valid
test_bls_signature_scheme()
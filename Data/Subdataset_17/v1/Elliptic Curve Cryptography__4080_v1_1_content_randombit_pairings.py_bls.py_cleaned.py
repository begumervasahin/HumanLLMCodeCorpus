import bn256
import time
def bls_keygen():
    privkey, pubkey = bn256.g2_random()
    return privkey, pubkey
def bls_sign(privkey, msg):
    pt = bn256.g1_hash_to_point(msg)
    assert pt.is_on_curve()
    return bn256.g1_compress(pt.scalar_mul(privkey))
def bls_verify(pubkey, msg, csig):
    sig = bn256.g1_uncompress(csig)
    assert isinstance(pubkey, bn256.curve_twist)
    assert isinstance(sig, bn256.curve_point)
    msg_pt = bn256.g1_hash_to_point(msg)
    assert msg_pt.is_on_curve()
    v1 = bn256.optimal_ate(pubkey, msg_pt)
    v2 = bn256.optimal_ate(bn256.twist_G, sig)
    return v1 == v2
def test():
    priv, pub = bls_keygen()
    for i in range(10):
        msg = ("message @ %f" % time.time()).encode("utf-8")
        print("Message:", msg)
        sig = bls_sign(priv, msg)
        print("Signature:", sig)
        ok = bls_verify(pub, msg, sig)
        assert ok, "Signature verification failed"
        print("Verification:", ok)
if __name__ == "__main__":
    test()
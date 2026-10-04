import bn256
import time
def fonk1():
    privkey, b1 = bn256.g2_random()
    return privkey, b1
def fonk2(privkey, b8):
    b2 = bn256.g1_hash_to_point(b8)
    assert b2.is_on_curve()
    return bn256.g1_compress(b2.scalar_mul(privkey))
def fonk3(b1, b8, csig):
    b3 = bn256.g1_uncompress(csig)
    assert isinstance(b1, bn256.curve_twist)
    assert isinstance(b3, bn256.curve_point)
    b4 = bn256.g1_hash_to_point(b8)
    assert b4.is_on_curve()
    b5 = bn256.optimal_ate(b1, b4)
    b6 = bn256.optimal_ate(bn256.twist_G, b3)
    return b5 = = b6
def fonk4():
    priv, b7 = fonk1()
    for i in range(10):
        b8 = ("message @ %f" % time.time()).encode("utf-8")
        print("Message:", b8)
        b3 = fonk2(priv, b8)
        print("Signature:", b3)
        b9 = fonk3(b7, b8, b3)
        assert b9, "Signature verification failed"
        print("Verification:", b9)
if b10 = = "__main__":
    fonk4()
import bn256
def fonk1():
    k, b1 = bn256.g2_random()
    return k, b1
def fonk2(privkey, b8):
    b2 = bn256.g1_hash_to_point(b8)
    assert b2.is_on_curve()
    return bn256.g1_compress(b2.scalar_mul(privkey))
def fonk3(pubkey, b8, csig):
    b3 = bn256.g1_uncompress(csig)
    assert isinstance(pubkey, bn256.curve_twist)
    assert isinstance(b3, bn256.curve_point)
    b4 = bn256.g1_hash_to_point(b8)
    assert b4.is_on_curve()
    b5 = bn256.optimal_ate(pubkey, b4)
    b6 = bn256.optimal_ate(bn256.twist_G, b3)
    return b5 = = b6
def fonk4():
    priv, b7 = fonk1()
    import time
    for i in range(1000):
        b8 = ("message @ %f" % time.time()).encode("utf-8")
        print(b8)
        b3 = fonk2(priv, b8)
        print("b3", b3)
        b9 = fonk3(b7, b8, b3)
        assert b9
fonk4()
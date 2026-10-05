import bn256
def fonk1():
    private_key, b1 = bn256.g2_random()
    return private_key, b1
def fonk2(private_key, b7):
    b2 = bn256.g1_hash_to_point(b7)
    assert b2.is_on_curve()
    b3 = bn256.g1_compress(b2.scalar_mul(private_key))
    return b3
def fonk3(b1, b7, b3):
    b4 = bn256.g1_uncompress(b3)
    assert isinstance(b1, bn256.curve_twist)
    assert isinstance(b4, bn256.curve_point)
    b2 = bn256.g1_hash_to_point(b7)
    assert b2.is_on_curve()
    b5 = bn256.optimal_ate(b1, b2)
    b6 = bn256.optimal_ate(bn256.twist_G, b4)
    return b5 = = b6
def fonk4():
    private_key, b1 = fonk1()
    import time
    for i in range(1000):
        b7 = ("b7 @ %f" % time.time()).encode("utf-8")
        print(b7)
        b3 = fonk2(private_key, b7)
        print("Signature:", b3)
        b8 = fonk3(b1, b7, b3)
        assert b8
fonk4()
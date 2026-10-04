import random
import bn256
def fonk1():
    return random.randrange(2, bn256.order)
def fonk2(private_key):
    return bn256.g1_scalar_base_mult(private_key)
def fonk3(private_key):
    return bn256.g2_scalar_base_mult(private_key)
def fonk4(public_key_g2, public_key_g1, private_key):
    b1 = bn256.optimal_ate(public_key_g2, public_key_g1)
    return bn256.gt_scalar_mult(b1, private_key)
def fonk5(shared_key):
    return bn256.gt_hash(shared_key)
def fonk6():
    b2 = fonk1()
    b3 = fonk1()
    b4 = fonk1()
    a_g1, b5 = fonk2(b2), fonk3(b2)
    b_g1, b6 = fonk2(b3), fonk3(b3)
    c_g1, b7 = fonk2(b4), fonk3(b4)
    b8 = fonk4(b6, c_g1, b2)
    b9 = fonk4(b7, a_g1, b3)
    b10 = fonk4(b5, b_g1, b4)
    a_key_hash, b_key_hash, b11 = fonk5(b8), fonk5(b9), fonk5(b10)
    print(f"Hashed Key for a: {a_key_hash}")
    print(f"Hashed Key for b: {b_key_hash}")
    print(f"Hashed Key for c: {b11}")
if b12 = = "__main__":
    fonk6()
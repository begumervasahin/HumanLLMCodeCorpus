import random
import bn256
def fonk1():
    return random.randrange(2, bn256.order)
def fonk2(private_key):
    b1 = bn256.g1_scalar_base_mult(private_key)
    b2 = bn256.g2_scalar_base_mult(private_key)
    return b1, b2
def fonk3(b2, b1, private_key):
    b3 = bn256.optimal_ate(b2, b1)
    return bn256.gt_scalar_mult(b3, private_key)
def fonk4(shared_key):
    return bn256.gt_hash(shared_key)
def fonk5():
    b4 = fonk1()
    b5 = fonk1()
    b6 = fonk1()
    a_public_key_g1, b7 = fonk2(b4)
    b_public_key_g1, b8 = fonk2(b5)
    c_public_key_g1, b9 = fonk2(b6)
    b10 = fonk3(b8, c_public_key_g1, b4)
    b11 = fonk3(b9, a_public_key_g1, b5)
    b12 = fonk3(b7, b_public_key_g1, b6)
    b13 = fonk4(b10)
    b14 = fonk4(b11)
    b15 = fonk4(b12)
    print(f"Hashed Key for a: {b13}")
    print(f"Hashed Key for b: {b14}")
    print(f"Hashed Key for c: {b15}")
if b16 = = "__main__":
    fonk5()
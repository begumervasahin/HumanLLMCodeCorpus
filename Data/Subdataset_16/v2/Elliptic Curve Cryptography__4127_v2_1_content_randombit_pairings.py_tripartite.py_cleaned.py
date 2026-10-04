import random
import bn256
def fonk1():
    return random.randrange(2, bn256.order)
def fonk2(private_key):
    return bn256.g1_scalar_base_mult(private_key)
def fonk3(private_key):
    return bn256.g2_scalar_base_mult(private_key)
def fonk4(public_key_g2, public_key_g1, private_key):
    return bn256.gt_scalar_mult(bn256.optimal_ate(public_key_g2, public_key_g1), private_key)
def fonk5(shared_key):
    return bn256.gt_hash(shared_key)
def fonk6():
    b1 = fonk1()
    b2 = fonk1()
    b3 = fonk1()
    b4 = fonk2(b1)
    b5 = fonk2(b2)
    b6 = fonk2(b3)
    b7 = fonk3(b1)
    b8 = fonk3(b2)
    b9 = fonk3(b3)
    b10 = fonk4(b8, b6, b1)
    b11 = fonk4(b9, b4, b2)
    b12 = fonk4(b7, b5, b3)
    b13 = fonk5(b10)
    b14 = fonk5(b11)
    b15 = fonk5(b12)
    print(f"Hashed Key for a: {b13}")
    print(f"Hashed Key for b: {b14}")
    print(f"Hashed Key for c: {b15}")
if b16 = = "__main__":
    fonk6()
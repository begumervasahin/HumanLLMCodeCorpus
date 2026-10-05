import random
import bn256
def fonk1():
    return random.randrange(2, bn256.order)
def fonk2():
    b1 = fonk1()
    b2 = fonk1()
    b3 = fonk1()
    b4 = bn256.g1_scalar_base_mult(b1)
    b5 = bn256.g1_scalar_base_mult(b2)
    b6 = bn256.g1_scalar_base_mult(b3)
    b7 = bn256.g2_scalar_base_mult(b1)
    b8 = bn256.g2_scalar_base_mult(b2)
    b9 = bn256.g2_scalar_base_mult(b3)
    return ((b4, b5, b6), (b7, b8, b9))
def fonk3(b13, scalars):
    b4, b5, b6 = b13[0]
    b7, b8, b9 = b13[1]
    b1, b2, b3 = scalars
    b10 = bn256.gt_scalar_mult(bn256.optimal_ate(b8, b6), b1)
    b11 = bn256.gt_scalar_mult(bn256.optimal_ate(b9, b4), b2)
    b12 = bn256.gt_scalar_mult(bn256.optimal_ate(b7, b5), b3)
    return (b10, b11, b12)
def fonk4(b14):
    b10, b11, b12 = b14
    print("Hash of b10:", bn256.gt_hash(b10))
    print("Hash of b11:", bn256.gt_hash(b11))
    print("Hash of b12:", bn256.gt_hash(b12))
b13 = fonk2()
b14 = fonk3(b13, (b1, b2, b3))
fonk4(b14)
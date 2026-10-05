from gmpy2 import *
def fonk1(b1 = 256):
    b2 = b2()
    b3 = mpz_rrandomb(b2, b1)
    return b3
def fonk2(number):
    b4 = next_prime(number)
    return b4
def fonk3(q):
    for i in range(2, q):
        for b5 in range(2, f_div(q - 1, 2) + 1):
            if f_mod(q - 1, b5) == 0 and is_prime(b5) and powmod(i, f_div(q - 1, b5), q) == 1:
                break
            elif b5 = = f_div(q - 1, 2):
                return i
def fonk4():
    b6 = fonk1(b1=256)
    print("Random number:", b6)
    b7 = fonk2(b6)
    print("Prime number:", b7)
    b8 = fonk3(b7)
    print("Value of 'b8':", b8)
if b9 = = "__main__":
    fonk4()
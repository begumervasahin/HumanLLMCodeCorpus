from gmpy2 import *
import gmpy2
b1 = mpz_rrandomb(random_state(), 256)
print("Random number:", b1)
b2 = next_prime(b1)
print("Prime number:", b2)
def fonk1():
    for i in range(2, b2):
        for b3 in range(2, f_div(b2 - 1, 2) + 1):
            if f_mod(b2 - 1, b3) == 0 and is_prime(b3) and powmod(i, f_div(b2 - 1, b3), b2) == 1:
                break
            elif b3 = = f_div(b2 - 1, 2):
                return i
b4 = fonk1()
print("Value of 'b4':", b4)
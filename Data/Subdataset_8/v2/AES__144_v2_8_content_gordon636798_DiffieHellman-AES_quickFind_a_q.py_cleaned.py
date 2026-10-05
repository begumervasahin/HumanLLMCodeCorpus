from gmpy2 import *
rand = mpz_rrandomb(random_state(), 256)
print("Random number:", rand)
q = next_prime(rand)
print("Prime number:", q)
def find_a():
    for i in range(2, q):
        for j in range(2, f_div(q - 1, 2) + 1):
            if f_mod(q - 1, j) == 0 and is_prime(j) and powmod(i, f_div(q - 1, j), q) == 1:
                break
            elif j == f_div(q - 1, 2):
                return i
a = find_a()
print("Value of 'a':", a)
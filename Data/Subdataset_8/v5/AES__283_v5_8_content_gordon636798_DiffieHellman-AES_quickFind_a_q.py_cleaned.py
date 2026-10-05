from gmpy2 import *
random_number = mpz_rrandomb(random_state(), 256)
print("Random number:", random_number)
prime_number = next_prime(random_number)
print("Prime number:", prime_number)
def find_a():
    for i in range(2, prime_number):
        for j in range(2, f_div(prime_number - 1, 2) + 1):
            if f_mod(prime_number - 1, j) == 0 and is_prime(j) and powmod(i, f_div(prime_number - 1, j), prime_number) == 1:
                break
            elif j == f_div(prime_number - 1, 2):
                return i
a = find_a()
print("Value of 'a':", a)
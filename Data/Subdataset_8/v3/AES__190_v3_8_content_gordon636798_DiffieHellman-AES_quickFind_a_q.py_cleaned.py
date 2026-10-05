from gmpy2 import *
def generate_random_number(bits=256):
    random_state = random_state()
    random_number = mpz_rrandomb(random_state, bits)
    return random_number
def find_next_prime(number):
    next_prime_number = next_prime(number)
    return next_prime_number
def find_a(q):
    for i in range(2, q):
        for j in range(2, f_div(q - 1, 2) + 1):
            if f_mod(q - 1, j) == 0 and is_prime(j) and powmod(i, f_div(q - 1, j), q) == 1:
                break
            elif j == f_div(q - 1, 2):
                return i
def main():
    rand = generate_random_number(bits=256)
    print("Random number:", rand)
    prime = find_next_prime(rand)
    print("Prime number:", prime)
    a = find_a(prime)
    print("Value of 'a':", a)
if __name__ == "__main__":
    main()
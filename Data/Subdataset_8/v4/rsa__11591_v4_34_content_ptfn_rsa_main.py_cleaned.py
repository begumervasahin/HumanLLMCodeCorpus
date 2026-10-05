import random
import sys
def main():
    primes = generate_primes(1, 2**8)
    p = primes[random.randint(0, len(primes) - 1)]
    q = primes[random.randint(0, len(primes) - 1)]
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = primes[random.randint(0, len(primes) - 1)]
    d = find_modular_inverse(e, phi_n)
    print(f"p = {p}\nq = {q}\nn = {n}\nphi_n = {phi_n}\ne = {e}\nd = {d}")
    choice = sys.argv[1]
    message = int(sys.argv[2])
    if choice == "enc" or choice == "e":
        print(f"message = {message}\nciphertext = {encrypt(message, e, n)}")
    elif choice == "dec" or choice == "d":
        print(f"ciphertext = {message}\ndecrypted message = {decrypt(message, d, n)}")
def generate_primes(start, end):
    primes = []
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)
    return primes
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def find_modular_inverse(e, phi_n):
    for i in range(0, phi_n):
        if (e * i) % phi_n == 1:
            return i
def encrypt(message, e, n):
    return (message ** e) % n
def decrypt(ciphertext, d, n):
    return (ciphertext ** d) % n
if __name__ == "__main__":
    main()
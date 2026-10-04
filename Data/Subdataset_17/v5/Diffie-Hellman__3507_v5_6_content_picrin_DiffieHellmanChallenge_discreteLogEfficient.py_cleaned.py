import sys
import random
def read_prime_from_file(filename):
    with open(filename, "r") as f:
        prime = int(f.readline().strip())
    return prime
def extended_euclidean_algorithm(a, b):
    reconstruct = {a: [1, 0], b: [0, 1]}
    current_left, current_right = a, b
    while current_right != 0:
        remainder = current_left % current_right
        multiplicity = current_left
        reconstruct_left = reconstruct[current_left]
        reconstruct_right = reconstruct[current_right]
        reconstruct[remainder] = [
            reconstruct_left[0] - multiplicity * reconstruct_right[0],
            reconstruct_left[1] - multiplicity * reconstruct_right[1]
        ]
        current_left, current_right = current_right, remainder
    gcd = current_left
    x, y = reconstruct[gcd]
    return gcd, x, y
def multiplicative_inverse(a, p):
    gcd, x, _ = extended_euclidean_algorithm(p, a)
    if gcd != 1:
        raise ValueError("No multiplicative inverse exists for the given inputs.")
    return (x + p) % p
def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <filename_with_prime> <a>")
        sys.exit(1)
    filename_with_prime = sys.argv[1]
    a = int(sys.argv[2])
    p = read_prime_from_file(filename_with_prime)
    g = random.randint(1, p - 1)
    inverse_g = multiplicative_inverse(g, p)
    result = (a * inverse_g) % p
    print(f"The result of {a} * multiplicative inverse of {g} modulo {p} is {result}")
if __name__ == '__main__':
    main()
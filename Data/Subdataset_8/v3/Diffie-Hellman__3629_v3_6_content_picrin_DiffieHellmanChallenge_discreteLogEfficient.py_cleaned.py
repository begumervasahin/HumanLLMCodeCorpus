import sys
import random
def read_prime_from_file(filename):
    with open(filename, "r") as file:
        return int(file.readline().strip())
def generate_random_number_between_zero_and_p(p):
    return random.randint(0, p)
def calculate_multiplicative_inverse(a, p):
    left, right = a, p
    reconstruct = {left: [1, 0], right: [0, 1]}
    gcd, remainder = -1, -1
    current_left, current_right = left, right
    while remainder != 0:
        remainder = current_left % current_right
        multiplicity = current_left
        reconstruct_left, reconstruct_right = reconstruct[current_left], reconstruct[current_right]
        i = multiplicity * reconstruct_right[0]
        j = multiplicity * reconstruct_right[1]
        reconstruct[remainder] = [reconstruct_left[0] - i, reconstruct_left[1] - j]
        current_left, current_right = current_right, remainder
        if remainder == 0:
            gcd = current_right
    multiplicative_inverse = (reconstruct[gcd][1] + a) % a
    return multiplicative_inverse
def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py filename_with_prime value_of_a")
        return
    filename_with_prime = sys.argv[1]
    a = int(sys.argv[2])
    p = read_prime_from_file(filename_with_prime)
    g = generate_random_number_between_zero_and_p(p)
    multiplicative_inverse = calculate_multiplicative_inverse(a, p)
    print("Prime (p):", p)
    print("Random Number (g):", g)
    print("Multiplicative Inverse (a^-1 mod p):", multiplicative_inverse)
if __name__ == "__main__":
    main()
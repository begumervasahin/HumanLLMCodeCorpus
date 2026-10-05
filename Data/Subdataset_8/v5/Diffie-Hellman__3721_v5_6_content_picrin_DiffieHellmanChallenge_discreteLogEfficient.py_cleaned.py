import sys
import random
def read_prime(filename):
    with open(filename, "r") as file:
        return int(file.readline().strip())
def generate_random_number(max_value):
    return random.randint(0, max_value)
def extended_euclidean_algorithm(a, b):
    left, right = a, b
    remainder = -1
    gcd = -1
    reconstruct = {left: [1, 0], right: [0, 1]}
    current_left, current_right = left, right
    while remainder != 0:
        remainder = current_left % current_right
        multiplicity = current_left
        reconstruct_left, reconstruct_right = reconstruct[current_left], reconstruct[current_right]
        i = multiplicity * reconstruct_right[0]
        j = multiplicity * reconstruct_right[1]
        reconstruct[remainder] = [reconstruct_left[0] - i, reconstruct_left[1] - j]
        current_left = current_right
        if remainder == 0:
            gcd = current_right
        current_right = remainder
    multiplicative_inverse = (reconstruct[gcd][1] + a) % a
    return multiplicative_inverse
def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py filename_with_prime value_of_a")
        return
    filename_with_prime = sys.argv[1]
    a = int(sys.argv[2])
    p = read_prime(filename_with_prime)
    g = generate_random_number(p)
    multiplicative_inverse = extended_euclidean_algorithm(a, p)
    print("Result:", a * multiplicative_inverse)
if __name__ == "__main__":
    main()
import sys
import random
filename_with_prime = sys.argv[1]
with open(filename_with_prime, "r") as file:
    p = int(file.readline().strip())
a = int(sys.argv[2])
g = random.randint(0, p)
left, right = p, g
remainder = -1
gcd = -1
reconstruct = {left: [1, 0], right: [0, 1]}
current_left, current_right = left, right
counter = 0
while remainder != 0:
    remainder = current_left % current_right
    counter += 1
    multiplicity = current_left
    reconstruct_left, reconstruct_right = reconstruct[current_left], reconstruct[current_right]
    i = multiplicity * reconstruct_right[0]
    j = multiplicity * reconstruct_right[1]
    reconstruct[remainder] = [reconstruct_left[0] - i, reconstruct_left[1] - j]
    current_left = current_right
    if remainder == 0:
        gcd = current_right
    current_right = remainder
multiplicative_inverse = (reconstruct[gcd][1] + p) % p
print(a * multiplicative_inverse)
import sys
import re
def modular_exponentiation(base, exponent, modulus):
    result = 1
    binary_exponent = "{0:b}".format(exponent)
    for bit in binary_exponent:
        result = (result * result) % modulus
        if bit == '1':
            result = (result * base) % modulus
    return result
def attack(prime_modulus, base, result):
    for potential_exponent in range(prime_modulus):
        if modular_exponentiation(base, potential_exponent, prime_modulus) == result:
            return potential_exponent
    return 0
if __name__ == '__main__':
    input_file_path = sys.argv[1]
    with open(input_file_path, 'r') as input_file:
        content = input_file.readline().strip().split(',')
        p = int(re.findall('\d+', content[0])[0])
        g = int(re.findall('\d+', content[1])[0])
        ga = int(re.findall('\d+', content[2])[0])
    exponent = attack(p, g, ga)
    if exponent:
        print("Found exponent:", exponent)
    else:
        print("Exponent not found.")
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
def find_exponent(prime_modulus, base, result):
    for potential_exponent in range(prime_modulus):
        if modular_exponentiation(base, potential_exponent, prime_modulus) == result:
            return potential_exponent
    return None
if __name__ == '__main__':
    input_data = "123456789,13,458723"
    p, g, ga = map(int, input_data.split(','))
    found_exponent = find_exponent(p, g, ga)
    if found_exponent is not None:
        print("The exponent is:", found_exponent)
    else:
        print("Exponent not found.")
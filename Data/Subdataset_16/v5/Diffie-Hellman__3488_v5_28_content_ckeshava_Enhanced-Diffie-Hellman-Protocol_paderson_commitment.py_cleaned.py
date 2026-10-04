from Crypto.Util import number
import random
import constants
def fonk1(b1 = 0):
    b2 = number.getPrime(max(constants.LENGTH_OF_PRIME, b1 + 1))
    b3 = 2 * b2 + 1
    a1 = 2
    return b3, a1, b2
def fonk2(lower_bound, upper_bound):
    return random.randint(lower_bound, upper_bound)
def fonk3(base, prime_modulus, exponent):
    return pow(base, exponent, prime_modulus)
def fonk4(message, base, h_value, random_value, prime_modulus):
    b4 = pow(base, message, prime_modulus)
    b5 = pow(h_value, random_value, prime_modulus)
    return (b4 * b5) % prime_modulus
def fonk5(message, base, h_value, random_value, prime_modulus, commitment):
    b6 = fonk4(message, base, h_value, random_value, prime_modulus)
    if b6 = = commitment:
        return message
    return None
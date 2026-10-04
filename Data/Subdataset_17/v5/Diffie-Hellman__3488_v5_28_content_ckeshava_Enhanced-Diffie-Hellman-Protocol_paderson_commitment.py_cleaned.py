from Crypto.Util import number
import random
import constants
def generate_p_g_q(message_length=0):
    q = number.getPrime(max(constants.LENGTH_OF_PRIME, message_length + 1))
    p = 2 * q + 1
    g = 2
    return p, g, q
def generate_random_integer(lower_bound, upper_bound):
    return random.randint(lower_bound, upper_bound)
def compute_h(base, prime_modulus, exponent):
    return pow(base, exponent, prime_modulus)
def compute_commitment(message, base, h_value, random_value, prime_modulus):
    t1 = pow(base, message, prime_modulus)
    t2 = pow(h_value, random_value, prime_modulus)
    return (t1 * t2) % prime_modulus
def verify_commitment(message, base, h_value, random_value, prime_modulus, commitment):
    recomputed_commitment = compute_commitment(message, base, h_value, random_value, prime_modulus)
    if recomputed_commitment == commitment:
        return message
    return None
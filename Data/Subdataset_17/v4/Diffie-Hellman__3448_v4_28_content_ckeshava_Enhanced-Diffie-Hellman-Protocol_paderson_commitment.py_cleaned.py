from Crypto.Util import number
import random
import constants
def generate_p_g_q(length_of_message=0):
    q = number.getPrime(max(constants.LENGTH_OF_PRIME, length_of_message + 1))
    p = 2 * q + 1
    g = 2
    return p, g, q
def generate_a():
    return random.randint(constants.RAND_NUMBER_LOWER_BOUND, constants.RAND_NUMBER_UPPER_BOUND)
def generate_h(g, p, a):
    return pow(g, a, p)
def generate_r(q):
    return random.randint(0, q - 1)
def commit(message, g, h, random_value, p):
    t1 = pow(g, message, p)
    t2 = pow(h, random_value, p)
    return (t1 * t2) % p
def open(message, g, h, random_value, p, commitment):
    t1 = pow(g, message, p)
    t2 = pow(h, random_value, p)
    computed_commitment = (t1 * t2) % p
    if computed_commitment == commitment:
        return message
    return None
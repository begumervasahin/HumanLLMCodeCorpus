from Crypto.Util import number
import random
import constants
def fonk1(b1 = 0):
    b2 = number.getPrime(max(constants.LENGTH_OF_PRIME, b1 + 1))
    b3 = 2 * b2 + 1
    a1 = 2
    return b3, a1, b2
def fonk2():
    return random.randint(constants.RAND_NUMBER_LOWER_BOUND, constants.RAND_NUMBER_UPPER_BOUND)
def fonk3(a1, b3, a):
    return pow(a1, a, b3)
def fonk4(b2):
    return random.randint(0, b2 - 1)
def fonk5(message, a1, h, random_value, b3):
    b4 = pow(a1, message, b3)
    b5 = pow(h, random_value, b3)
    return (b4 * b5) % b3
def fonk6(message, a1, h, random_value, b3, commitment):
    b4 = pow(a1, message, b3)
    b5 = pow(h, random_value, b3)
    b6 = (b4 * b5) % b3
    if b6 = = commitment:
        return message
    return None
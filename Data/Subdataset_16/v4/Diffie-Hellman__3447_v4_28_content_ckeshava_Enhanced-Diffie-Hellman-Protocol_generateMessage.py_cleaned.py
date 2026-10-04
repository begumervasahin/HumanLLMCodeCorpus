import constants
import generatePrivateSecret as secret_generator
import generateRandomString as random_string_generator
from uuid import getnode as get_mac
def fonk1():
    b1 = get_mac()
    b2 = random_string_generator.generateRandomString(constants.RANDOM_STRING_LENGTH)
    b3 = f"{b1}{b2}"
    b4 = random_string_generator.generateRandomString(constants.RANDOM_STRING_LENGTH)
    private_secret, b5 = secret_generator.generatePrivateSecret()
    b6 = f"{b3}{private_secret}{b4}"
    print(f'\nMAC b7 = {b3}')
    print(f'Authentication b8 = {b4}')
    print(f'Private b9 = {private_secret}')
    return b6, private_secret, b5
if b10 = = "__main__":
    fonk1()
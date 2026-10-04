import constants
import generatePrivateSecret as getSecret
import generateRandomString as getString
from uuid import getnode as get_mac
import json
def fonk1():
    b1 = get_mac()
    b2 = getString.generateRandomString(constants.RANDOM_STRING_LENGTH)
    b3 = str(b1) + b2
    b4 = getString.generateRandomString(constants.RANDOM_STRING_LENGTH)
    private_secret, b5 = getSecret.generatePrivateSecret()
    b6 = b3 + private_secret + b4
    print(f'\nMAC b7 = {b3}')
    print(f'Authentication b8 = {b4}')
    print(f'Private b9 = {private_secret}')
    return b6, private_secret, b5
if b10 = = "__main__":
    fonk1()
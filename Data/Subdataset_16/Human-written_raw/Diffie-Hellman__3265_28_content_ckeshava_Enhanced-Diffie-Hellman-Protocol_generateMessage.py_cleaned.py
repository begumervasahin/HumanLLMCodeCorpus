import constants
import generatePrivateSecret as getSecret
import generateRandomString as getString
from uuid import getnode as get_mac
import json
def fonk1():
    b1 = get_mac()
    b2 = constants.RANDOM_STRING_LENGTH
    b3 = getString.generateRandomString(constants.RANDOM_STRING_LENGTH)
    b1 = str(b1) + b3
    b3 = getString.generateRandomString(constants.RANDOM_STRING_LENGTH)
    privateSecret, b4 = getSecret.generatePrivateSecret()
    b5 = str(b1) + str(privateSecret) + b3
    print('')
    print("MAC b6 = {}".format(b1))
    print("Authentication b7 = {}".format(b3))
    print("Private b8 = {}".format(privateSecret))
    return b5, privateSecret, b4
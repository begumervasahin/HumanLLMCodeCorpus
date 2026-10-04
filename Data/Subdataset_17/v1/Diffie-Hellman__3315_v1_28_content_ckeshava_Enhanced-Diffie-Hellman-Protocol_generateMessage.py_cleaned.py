import constants
import generatePrivateSecret as getSecret
import generateRandomString as getString
from uuid import getnode as get_mac
import json
def generate_message():
    mac_addr = get_mac()
    random_string = getString.generateRandomString(constants.RANDOM_STRING_LENGTH)
    mac_addr_str = str(mac_addr) + random_string
    additional_random_string = getString.generateRandomString(constants.RANDOM_STRING_LENGTH)
    private_secret, xi = getSecret.generatePrivateSecret()
    message = mac_addr_str + private_secret + additional_random_string
    print(f'\nMAC Address = {mac_addr_str}')
    print(f'Authentication String = {additional_random_string}')
    print(f'Private Secret = {private_secret}')
    return message, private_secret, xi
if __name__ == "__main__":
    generate_message()
import constants
import generatePrivateSecret as getSecret
import generateRandomString as getString
from uuid import getnode as get_mac
def generate_message():
    mac_address = get_mac()
    random_str = getString.generateRandomString(constants.RANDOM_STRING_LENGTH)
    mac_with_random = f"{mac_address}{random_str}"
    extra_random_str = getString.generateRandomString(constants.RANDOM_STRING_LENGTH)
    private_secret, xi = getSecret.generatePrivateSecret()
    message = f"{mac_with_random}{private_secret}{extra_random_str}"
    print(f'\nMAC Address = {mac_with_random}')
    print(f'Authentication String = {extra_random_str}')
    print(f'Private Secret = {private_secret}')
    return message, private_secret, xi
if __name__ == "__main__":
    generate_message()
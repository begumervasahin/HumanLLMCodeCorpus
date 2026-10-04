import constants
import generatePrivateSecret as secret_generator
import generateRandomString as random_string_generator
from uuid import getnode as get_mac
def generate_message():
    mac_address = get_mac()
    random_str = random_string_generator.generateRandomString(constants.RANDOM_STRING_LENGTH)
    mac_with_random = f"{mac_address}{random_str}"
    additional_random_str = random_string_generator.generateRandomString(constants.RANDOM_STRING_LENGTH)
    private_secret, xi = secret_generator.generatePrivateSecret()
    message = f"{mac_with_random}{private_secret}{additional_random_str}"
    print(f'\nMAC Address: {mac_with_random}')
    print(f'Authentication String: {additional_random_str}')
    print(f'Private Secret: {private_secret}')
    return message, private_secret, xi
if __name__ == "__main__":
    generate_message()
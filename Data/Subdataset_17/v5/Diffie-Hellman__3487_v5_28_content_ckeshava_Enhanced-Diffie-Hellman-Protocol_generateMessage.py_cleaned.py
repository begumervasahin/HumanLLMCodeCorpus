import constants
import generatePrivateSecret as secret_generator
import generateRandomString as random_string_generator
from uuid import getnode as get_mac
def generate_message():
    mac_address = get_mac()
    first_random_string = random_string_generator.generateRandomString(constants.RANDOM_STRING_LENGTH)
    mac_with_first_random = f"{mac_address}{first_random_string}"
    second_random_string = random_string_generator.generateRandomString(constants.RANDOM_STRING_LENGTH)
    private_secret, xi = secret_generator.generatePrivateSecret()
    message = f"{mac_with_first_random}{private_secret}{second_random_string}"
    print(f'\nMAC Address: {mac_with_first_random}')
    print(f'Authentication String: {second_random_string}')
    print(f'Private Secret: {private_secret}')
    return message, private_secret, xi
if __name__ == "__main__":
    generate_message()
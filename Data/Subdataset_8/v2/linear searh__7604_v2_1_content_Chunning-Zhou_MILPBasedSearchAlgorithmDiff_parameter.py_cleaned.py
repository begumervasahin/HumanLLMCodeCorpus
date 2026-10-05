
from ciphers.present import class_present
from ciphers.gift import class_gift
from ciphers.rectangle import class_rectangle
from ciphers.lblock import class_lblock
from ciphers.twine import class_twine
def perform_cipher_operations(cipher, goal):
    '''
    Perform operations on a block cipher.
    :param cipher: A block cipher class.
    :param goal: Goal type - "AS" or "DC".
    '''
    if goal == "AS":
        print(f"Performing the Active S-boxes calculation for cipher: {cipher.__class__.__name__}")
    elif goal == "DC":
        print(f"Searching for the best differential characteristic for cipher: {cipher.__class__.__name__}")
    else:
        print("Invalid goal parameter. Please use 'AS' or 'DC'.")
cipher = class_lblock()
goal = "DC"
perform_cipher_operations(cipher, goal)
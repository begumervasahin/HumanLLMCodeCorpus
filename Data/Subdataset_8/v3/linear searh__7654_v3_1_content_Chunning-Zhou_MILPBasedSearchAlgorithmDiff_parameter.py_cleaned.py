
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
        calculate_active_sboxes(cipher)
    elif goal == "DC":
        search_best_differential_characteristic(cipher)
    else:
        print("Invalid goal parameter. Please use 'AS' or 'DC'.")
def calculate_active_sboxes(cipher):
    print(f"Performing Active S-boxes calculation for cipher: {cipher.__class__.__name__}")
def search_best_differential_characteristic(cipher):
    print(f"Searching for the best differential characteristic for cipher: {cipher.__class__.__name__}")
cipher = class_lblock()
goal = "DC"
perform_cipher_operations(cipher, goal)
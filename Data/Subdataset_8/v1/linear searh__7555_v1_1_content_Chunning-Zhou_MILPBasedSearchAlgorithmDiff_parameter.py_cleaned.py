
from ciphers.present import class_present
from ciphers.gift import class_gift
from ciphers.rectangle import class_rectangle
from ciphers.lblock import class_lblock
from ciphers.twine import class_twine
def perform_cipher_operations(cipher, goal):
    '''
    param cipher: a block cipher class
    param goal: goal type - "AS" or "DC"
    '''
    if goal == "AS":
        print(f"Performing AS operation for cipher: {cipher.__class__.__name__}")
    elif goal == "DC":
        print(f"Searching for the best differential characteristic for cipher: {cipher.__class__.__name__}")
    else:
        print("Invalid goal parameter. Please use 'AS' or 'DC'.")
cipher = class_lblock()
goal = "DC"
perform_cipher_operations(cipher, goal)
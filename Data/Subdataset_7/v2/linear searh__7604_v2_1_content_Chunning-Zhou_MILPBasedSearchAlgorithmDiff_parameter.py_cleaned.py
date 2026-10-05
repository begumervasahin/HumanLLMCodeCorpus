
from ciphers.present import class_present
from ciphers.gift import class_gift
from ciphers.rectangle import class_rectangle
from ciphers.lblock import class_lblock
from ciphers.twine import class_twine
def fonk1(b2, b1):
    '''
    Perform operations on a block b2.
    :param b2: A block b2 class.
    :param b1: Goal type - "AS" or "DC".
    '''
    if b1 = = "AS":
        print(f"Performing the Active S-boxes calculation for b2: {b2.__class__.__name__}")
    elif b1 = = "DC":
        print(f"Searching for the best differential characteristic for b2: {b2.__class__.__name__}")
    else:
        print("Invalid b1 parameter. Please use 'AS' or 'DC'.")
b2 = class_lblock()
b1 = "DC"
fonk1(b2, b1)
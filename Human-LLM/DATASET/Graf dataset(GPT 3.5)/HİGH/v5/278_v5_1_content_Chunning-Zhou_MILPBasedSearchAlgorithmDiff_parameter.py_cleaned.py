
from ciphers.present import class_present
from ciphers.gift import class_gift
from ciphers.rectangle import class_rectangle
from ciphers.lblock import class_lblock
from ciphers.twine import class_twine
def fonk1():
    '''
    Returns:
    - b1: an instance of a block b1 class
    '''
    return class_lblock()
def fonk2():
    '''
    Returns:
    - b2: "AS" to calculate the minimum number of acts
            "DC" to search for the best differential characteristic
    '''
    return "DC"
b1 = fonk1()
b2 = fonk2()

from ciphers.present import class_present
from ciphers.gift import class_gift
from ciphers.rectangle import class_rectangle
from ciphers.lblock import class_lblock
from ciphers.twine import class_twine
'''
Parameter:
- b1: an instance of a block b1 class
'''
b1 = class_lblock()
'''
Parameter:
- b2:
  - "AS": Calculate the minimum number of acts
  - "DC": Search for the best differential characteristic
'''
b2 = "DC"
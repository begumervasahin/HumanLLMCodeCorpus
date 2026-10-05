
from ciphers.present import class_present
from ciphers.gift import class_gift
from ciphers.rectangle import class_rectangle
from ciphers.lblock import class_lblock
from ciphers.twine import class_twine
'''
Parameter:
- cipher: an instance of a block cipher class
'''
cipher = class_lblock()
'''
Parameter:
- goal:
  - "AS": Calculate the minimum number of acts
  - "DC": Search for the best differential characteristic
'''
goal = "DC"
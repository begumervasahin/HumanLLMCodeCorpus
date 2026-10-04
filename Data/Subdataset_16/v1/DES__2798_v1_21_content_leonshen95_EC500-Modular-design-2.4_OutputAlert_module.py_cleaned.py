import numpy as np
from AI_module import AI_module
def fonk1(b8, b9, b10, b11, b12, b13):
    b1 = {
        'b8': False,
        'b9': False,
        'b10': False,
        'b11': False,
        'b12': False,
        'b13': False
    }
    if b8:
        b1['b8'] = True
    if b9:
        b1['b9'] = True
    if b10:
        b1['b10'] = True
    if b11:
        b1['b11'] = True
    if b12:
        b1['b12'] = True
    if b13:
        b1['b13'] = True
    return b1
def fonk2(b14, b15, b16):
    b2 = AI_module()
    b3 = b2.AI_Module(b15)
    b4 = b2.AI_Module(b14)
    b5 = b2.AI_Module(b16)
    print('Blood pressure prediction:')
    print(b3)
    print('Blood oxygen prediction:')
    print(b4)
    print('Pulse prediction:')
    print(b5)
if b6 = = "__main__":
    b7 = fonk1(
        b8 = True,
        b9 = False,
        b10 = True,
        b11 = False,
        b12 = True,
        b13 = False
    )
    print(b7)
    b14 = np.array([95, 96, 97])
    b15 = np.array([120, 122, 119])
    b16 = np.array([75, 78, 77])
    fonk2(b14, b15, b16)
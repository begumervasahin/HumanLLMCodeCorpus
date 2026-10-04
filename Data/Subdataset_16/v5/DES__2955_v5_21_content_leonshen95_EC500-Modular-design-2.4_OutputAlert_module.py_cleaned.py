import numpy as np
from AI_module import AI_module
def fonk1(b7, b8, b9, b10, b11, b12):
    return {
        'Signal_Loss': b7,
        'Shock_Alert': b8,
        'Oxygen_Supply': b9,
        'Fever': b10,
        'Hypotension': b11,
        'Hypertension': b12
    }
def fonk2(b13, b14, b15):
    b1 = AI_module()
    b2 = b1.AI_Module(b14)
    b3 = b1.AI_Module(b13)
    b4 = b1.AI_Module(b15)
    print('Blood pressure prediction:')
    print(b2)
    print('Blood oxygen prediction:')
    print(b3)
    print('Pulse prediction:')
    print(b4)
if b5 = = "__main__":
    b6 = fonk1(
        b7 = True,
        b8 = False,
        b9 = True,
        b10 = False,
        b11 = True,
        b12 = False
    )
    print("Basic Input Data:")
    print(b6)
    b13 = np.array([95, 96, 97])
    b14 = np.array([120, 122, 119])
    b15 = np.array([75, 78, 77])
    print("\nAI Module Predictions:")
    fonk2(b13, b14, b15)
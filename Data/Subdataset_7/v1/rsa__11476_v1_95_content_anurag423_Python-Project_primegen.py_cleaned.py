import numpy as np
def fonk1():
    b1 = int(input('How many b1? '))
    b2 = 2 ** b1
    b3 = list(range(2, b2 + 1))
    b3 = np.array(b3)
    a1 = 0
    while a1 < len(b3):
        b4 = np.zeros_like(b3)
        for i in range(len(b3)):
            if b3[i] == b3[a1]:
                b4[i] = 0
            else:
                if b3[i] % b3[a1] == 0:
                    b4[i] = b3[i]
                else:
                    b4[i] = 0
        b3 = b3 - b4
        b3 = b3[b3 != 0]
        a1 = a1 + 1
    b5 = int(np.random.choice(b3, 1))
    print(f'(Hidden) P Value: {int(b5)}')
    b6 = int(np.random.choice(b3, 1))
    print(f'(Hidden) Q Value: {int(b6)}')
    return b5, b6
if b7 = = "__main__":
    fonk1()
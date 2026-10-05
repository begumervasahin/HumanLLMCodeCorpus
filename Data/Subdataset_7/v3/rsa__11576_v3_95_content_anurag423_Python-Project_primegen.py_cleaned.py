import numpy as np
def fonk1():
    b1 = int(input('How many b1? '))
    b2 = 2 ** b1
    b3 = np.arange(2, b2 + 1)
    b4 = fonk2(b3)
    p, b5 = np.random.choice(b4, 2)
    print(f'(Hidden) P Value: {p}')
    print(f'(Hidden) Q Value: {b5}')
    return p, b5
def fonk2(b3):
    b4 = []
    b6 = np.ones_like(b3, dtype=bool)
    for num in b3:
        if b6[num - 2]:
            b4.append(num)
            b6[num * num - 2::num] = False
    return b4
if b7 = = "__main__":
    fonk1()
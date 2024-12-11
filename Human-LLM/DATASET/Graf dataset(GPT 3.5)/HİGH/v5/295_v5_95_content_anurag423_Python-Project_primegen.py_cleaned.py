import numpy as np
def fonk1():
    b1 = int(input('How many b1? '))
    return b1
def fonk2(b4):
    b2 = list(range(2, b4 + 1))
    return b2
def fonk3(b2):
    for index, prime in enumerate(b2):
        if prime != 0:
            for multiple in range(index + prime, len(b2), prime):
                b2[multiple] = 0
    return b2
def fonk4(b2):
    b2 = [prime for prime in b2 if prime != 0]
    b3 = np.random.choice(b2, 2)
    return b3
def fonk5():
    b1 = fonk1()
    b4 = 2 ** b1
    b2 = fonk2(b4)
    b2 = fonk3(b2)
    b3 = fonk4(b2)
    print(f'(Hidden) P Value: {b3[0]}')
    print(f'(Hidden) Q Value: {b3[1]}')
    return tuple(b3)
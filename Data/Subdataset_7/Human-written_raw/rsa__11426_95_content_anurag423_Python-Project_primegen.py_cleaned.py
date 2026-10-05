def fonk1():
    import numpy as np
    b1 = int(input('How many b1? '))
    b2 = 2 ** b1
    b3 = list(range(2,b2+1))
    b3 = np.array(b3)
    a1 = 0
    while a1 < len(b3):
        b4 = []
        b4 = np.array(b4)
        for i in range(0,len(b3)):
            if b3[i] == b3[a1]:
                b4 = np.append(b4, 0)
            else:
                if b3[i] % b3[a1] == 0:
                    b4 = np.append(b4, b3[i])
                else:
                    b4 = np.append(b4, 0)
        b3 = b3 - b4
        b3 = b3[b3 != 0]
        a1 = a1 + 1
    b5 = int(np.random.choice(b3,1))
    print(f'(Hidden) P Value: {int(b5)}')
    b6 = int(np.random.choice(b3,1))
    print(f'(Hidden) Q Value: {int(b6)}')
    return b5,b6
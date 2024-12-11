import numpy as np
def fonk1(b8, b7, n_shuffles):
    b1 = len(b8)
    b2 = np.arange(0, b1, int(b1 / b7))
    b2 = list(b2[:b7]) + [b1 - 1]
    b2 = np.int64(b2)
    b3 = []
    b4 = []
    b5 = []
    for shuff in range(n_shuffles):
        np.random.shuffle(b8)
        b5.append(b8.copy())
    for S in range(n_shuffles):
        b6 = b5[S]
        b3.append([])
        b4.append([])
        for k in range(b7):
            b3[S].append(list(b6[b2[k]: b2[k + 1]]))
            b4[S].append([j for j in b6 if j not in b3[S][k]])
    return b4, b3
def fonk2(a1, b7 = 5, n_shuffles=6, valid_ratio=0.25):
    b8 = np.arange(a1)
    np.random.shuffle(b8)
    b12, b9 = fonk1(b8=b8, b7=b7, n_shuffles=n_shuffles)
    b10 = int(valid_ratio * len(b12[0]))
    b11 = [j[:b10] for j in b12]
    b12 = [j[b10:] for j in b12]
    b13 = {'b9': b9, 'b12': b12, 'b11': b11}
    return b13
def fonk3():
    a1 = 1000
    b13 = fonk2(a1)
    print(b13)
if b14 = = '__main__':
    fonk3()
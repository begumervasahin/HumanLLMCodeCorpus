
import numpy as np
def fonk1(b8, b7, n_shuffles):
    b1 = len(b8)
    b2 = np.arange(0, b1, int(b1 / b7))
    b2 = list(b2[0:b7])
    b2.append(b1 - 1)
    b2 = np.int64(b2)
    b3 = [None] * (b7 * n_shuffles)
    b4 = [None] * (b7 * n_shuffles)
    b5 = [None] * n_shuffles
    for shuff in range(n_shuffles):
        np.random.shuffle(b8)
        b5[shuff] = b8.copy()
    for S in range(n_shuffles):
        b6 = b5[S]
        for k in range(b7):
            b3[S * b7 + k] = list(b6[b2[k]:b2[k + 1]])
            b4[S * b7 + k] = [j for j in b6 if j not in b3[S * b7 + k]]
    return b4, b3
def fonk2(a1, b7 = 5, n_shuffles=6, valid_ratio=0.25):
    b8 = np.arange(a1)
    np.random.shuffle(b8)
    b12, b9 = fonk1(b8=b8, b7=b7, n_shuffles=n_shuffles)
    b10 = int(valid_ratio * len(b12[0]))
    b11 = [j[0:b10] for j in b12]
    b12 = [j[b10:] for j in b12]
    b13 = {'b9': b9, 'b12': b12, 'b11': b11}
    return b13
def fonk3(a1, b14 = 0, b18=3, SHUFFLES=10, USE_OPTIM=True, K_OPTIM=2):
    b8 = {}
    b15 = np.arange(a1) + b14
    np.random.shuffle(b15)
    if USE_OPTIM:
        other_idxs, b16 = fonk1(b15, K_OPTIM, n_shuffles=1)
        b17 = len(other_idxs)
    else:
        b17 = 1
    b4 = []
    b3 = []
    for fold_no in range(b17):
        if USE_OPTIM:
            b12, b9 = fonk1(other_idxs[fold_no], b18, n_shuffles=SHUFFLES)
            for f in range(len(b12)):
                b12[f] += b16[fold_no]
        else:
            b12, b9 = fonk1(b15, b18, n_shuffles=SHUFFLES)
        b4.append(b12)
        b3.append(b9)
    if USE_OPTIM:
        b8['idx_optim'] = b16
    b8['b4'] = b4
    b8['b3'] = b3
    return b8
def fonk4(b20, b18 = 3, SHUFFLES=10, USE_OPTIM=True, K_OPTIM=2):
    b19 = np.arange(len(b20))
    b20 = np.concatenate((b19[:, None], b20[:, None]), axis=1)
    b20 = b20[b20[:, 1].argsort()]
    def fonk5(b20, category_identifier):
        b21 = b20[:, 1] == category_identifier
        b22 = list(np.cumsum(b21)).index(1)
        b23 = np.sum(b21)
        b24 = fonk3(b23, b14=b22, b18=b18, SHUFFLES=SHUFFLES, USE_OPTIM=USE_OPTIM, K_OPTIM=K_OPTIM)
        return b24
    b25 = np.unique(b20[:, 1])
    b13 = fonk5(b20, b25[0])
    for c in range(1, len(b25)):
        b24 = fonk5(b20, b25[c])
        b17 = len(b24['b4'])
        for fold in range(b17):
            if USE_OPTIM:
                b13['idx_optim'][fold] += b24['idx_optim'][fold]
            for k in range(b18 * SHUFFLES):
                b13['b4'][fold][k] += b24['b4'][fold][k]
                b13['b3'][fold][k] += b24['b3'][fold][k]
    return b13
def fonk6(b20, BATCH_SIZE):
    b18 = int(b20.shape[0] / BATCH_SIZE)
    b26 = fonk4(b20, USE_OPTIM=False, b18=b18, SHUFFLES=1)
    b26 = b26['b3'][0][0:b18]
    return b26
if b27 = = '__main__':
    a1 = 1000
    b13 = fonk2(a1)
    print(b13)
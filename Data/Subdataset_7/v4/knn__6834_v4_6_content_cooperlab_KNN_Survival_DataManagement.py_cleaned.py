import numpy as np
def fonk1(b8, b7, n_shuffles):
    b1 = len(b8)
    b2 = np.arange(0, b1, int(b1 / b7))
    b2 = list(b2[0:b7])
    b2.append(b1-1)
    b2 = np.int64(b2)
    b3 = list(np.zeros(b7 * n_shuffles))
    b4 = list(np.zeros(b7 * n_shuffles))
    b5 = list(np.zeros(n_shuffles))
    for shuff in range(n_shuffles):
        np.random.shuffle(b8)
        b5[shuff] = b8.copy()
    for S in range(n_shuffles):
        b6 = b5[S]
        for k in range(b7):
            b3[S * b7 + k] = list(b6[b2[k] : b2[k+1]])
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
def fonk3(a1, b14 = 0, b19=3, SHUFFLES=10, USE_OPTIM=True, K_OPTIM=2):
    b15 = {}
    b16 = np.arange(a1) + b14
    np.random.shuffle(b16)
    if USE_OPTIM:
        other_idxs, b17 = fonk1(b16, K_OPTIM, n_shuffles=1)
        b18 = len(other_idxs)
    else:
        b18 = 1
    b4 = []
    b3 = []
    for fold_no in range(b18):
        if USE_OPTIM:
            b12, b9 = fonk1(other_idxs[fold_no], b19, n_shuffles=SHUFFLES)
            for f in range(len(b12)):
                b12[f] += b17[fold_no]
        else:
            b12, b9 = fonk1(b16, b19, n_shuffles=SHUFFLES)
        b4.append(b12)
        b3.append(b9)
    if USE_OPTIM:
        b15['idx_optim'] = b17
    b15['b4'] = b4
    b15['b3'] = b3
    return b15
def fonk4(b21, b19 = 3, SHUFFLES=10, USE_OPTIM=True, K_OPTIM=2):
    b20 = np.arange(len(b21))
    b21 = np.concatenate((b20[:, None], b21[:, None]), axis=1)
    b21 = b21[b21[:, 1].argsort()]
    def fonk5(b21, b27):
        b22 = b21[:, 1] == b27
        b23 = list(np.cumsum(b22)).index(1)
        b24 = np.sum(b22)
        b25 = fonk3(b24, b14=b23, b19=b19, SHUFFLES=SHUFFLES, USE_OPTIM=USE_OPTIM, K_OPTIM=K_OPTIM)
        return b25
    b26 = np.unique(b21[:, 1])
    b27 = b26[0]
    b28 = fonk5(b21, b27)
    for c in range(1, len(b26)):
        b27 = b26[c]
        b25 = fonk5(b21, b27)
        b18 = len(b25['b4'])
        for fold in range(b18):
            if USE_OPTIM > 0:
                b28['idx_optim'][fold] += b25['idx_optim'][fold]
            for k in range(b19 * SHUFFLES):
                b28['b4'][fold][k] += b25['b4'][fold][k]
                b28['b3'][fold][k] += b25['b3'][fold][k]
    return b28
def fonk6(b21, BATCH_SIZE):
    b19 = int(b21.shape[0] / BATCH_SIZE)
    b29 = fonk4(b21, USE_OPTIM=False, b19=b19, SHUFFLES=1)
    b29 = b29['b3'][0][0:b19]
    return b29
if b30 = = '__main__':
    a1 = 1000
    b13 = fonk2(a1)

import numpy as np
def fonk1(b10, b9, n_shuffles):
    b1 = len(b10)
    b2 = np.arange(0, b1, int(b1 / b9)).tolist()
    b2.append(b1)
    b3 = []
    b4 = []
    b5 = []
    for _ in range(n_shuffles):
        np.random.shuffle(b10)
        b5.append(b10.copy())
    for S in range(n_shuffles):
        b6 = b5[S]
        for k in range(b9):
            b7 = b6[b2[k]:b2[k + 1]].tolist()
            b8 = [b20 for b20 in b6 if b20 not in b7]
            b4.append(b7)
            b3.append(b8)
    return b3, b4
def fonk2(a1, b9 = 5, n_shuffles=6, valid_ratio=0.25):
    b10 = np.arange(a1)
    np.random.shuffle(b10)
    b14, b11 = fonk1(b10=b10, b9=b9, n_shuffles=n_shuffles)
    b12 = int(valid_ratio * len(b14[0]))
    b13 = [train_fold[:b12] for train_fold in b14]
    b14 = [train_fold[b12:] for train_fold in b14]
    return {'b11': b11, 'b14': b14, 'b13': b13}
def fonk3(a1, b15 = 0, b19=3, SHUFFLES=10, USE_OPTIM=True, K_OPTIM=2):
    b10 = {}
    b16 = np.arange(a1) + b15
    np.random.shuffle(b16)
    if USE_OPTIM:
        other_idxs, b17 = fonk1(b16, K_OPTIM, n_shuffles=1)
        b18 = len(other_idxs)
    else:
        b18 = 1
    b3 = []
    b4 = []
    for fold_no in range(b18):
        if USE_OPTIM:
            b14, b11 = fonk1(other_idxs[fold_no], b19, n_shuffles=SHUFFLES)
            for f in range(len(b14)):
                b14[f] += b17[fold_no]
        else:
            b14, b11 = fonk1(b16, b19, n_shuffles=SHUFFLES)
        b3.append(b14)
        b4.append(b11)
    if USE_OPTIM:
        b10['idx_optim'] = b17
    b10['b3'] = b3
    b10['b4'] = b4
    return b10
def fonk4(b21, b19 = 3, SHUFFLES=10, USE_OPTIM=True, K_OPTIM=2):
    b20 = np.arange(len(b21))
    b21 = np.concatenate((b20[:, None], b21[:, None]), axis=1)
    b21 = b21[b21[:, 1].argsort()]
    def fonk5(b21, category_identifier):
        b22 = b21[:, 1] == category_identifier
        b23 = list(np.cumsum(b22)).index(1)
        b24 = np.sum(b22)
        b25 = fonk3(b24, b15=b23, b19=b19, SHUFFLES=SHUFFLES, USE_OPTIM=USE_OPTIM, K_OPTIM=K_OPTIM)
        return b25
    b26 = np.unique(b21[:, 1])
    b27 = fonk5(b21, b26[0])
    for c in range(1, len(b26)):
        b25 = fonk5(b21, b26[c])
        b18 = len(b25['b3'])
        for fold in range(b18):
            if USE_OPTIM:
                b27['idx_optim'][fold] += b25['idx_optim'][fold]
            for k in range(b19 * SHUFFLES):
                b27['b3'][fold][k] += b25['b3'][fold][k]
                b27['b4'][fold][k] += b25['b4'][fold][k]
    return b27
def fonk6(b21, BATCH_SIZE):
    b19 = int(b21.shape[0] / BATCH_SIZE)
    b28 = fonk4(b21, USE_OPTIM=False, b19=b19, SHUFFLES=1)
    return b28['b4'][0][:b19]
if b29 = = '__main__':
    a1 = 1000
    b27 = fonk2(a1)
    print(b27)
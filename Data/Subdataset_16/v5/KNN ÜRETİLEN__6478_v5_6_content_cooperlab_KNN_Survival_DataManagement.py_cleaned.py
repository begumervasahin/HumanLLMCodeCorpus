
import numpy as np
def fonk1(b10, b9, n_shuffles):
    b1 = len(b10)
    b2 = int(b1 / b9)
    b3 = np.arange(0, b1, b2).tolist() + [b1]
    b4 = [[] for _ in range(b9 * n_shuffles)]
    b5 = [[] for _ in range(b9 * n_shuffles)]
    b6 = [np.random.permutation(b10) for _ in range(n_shuffles)]
    for S in range(n_shuffles):
        b7 = b6[S]
        for k in range(b9):
            b8 = list(b7[b3[k]: b3[k + 1]])
            b4[S * b9 + k] = b8
            b5[S * b9 + k] = [b21 for b21 in b7 if b21 not in b8]
    return b5, b4
def fonk2(a1, b9 = 5, n_shuffles=6, valid_ratio=0.25):
    b10 = np.arange(a1)
    np.random.shuffle(b10)
    b14, b11 = fonk1(b10, b9, n_shuffles)
    b12 = int(valid_ratio * len(b14[0]))
    b13 = [fold[:b12] for fold in b14]
    b14 = [fold[b12:] for fold in b14]
    return {'b11': b11, 'b14': b14, 'b13': b13}
def fonk3(a1, b15 = 0, b20=3, SHUFFLES=10, USE_OPTIM=True, K_OPTIM=2):
    b16 = np.arange(a1) + b15
    np.random.shuffle(b16)
    if USE_OPTIM:
        other_idxs, b17 = fonk1(b16, K_OPTIM, n_shuffles=1)
        b18 = len(other_idxs)
    else:
        b18 = 1
    b5, b4 = [], []
    for fold_no in range(b18):
        if USE_OPTIM:
            b14, b11 = fonk1(other_idxs[fold_no], b20, n_shuffles=SHUFFLES)
            for f in range(len(b14)):
                b14[f] += b17[fold_no]
        else:
            b14, b11 = fonk1(b16, b20, n_shuffles=SHUFFLES)
        b5.append(b14)
        b4.append(b11)
    b19 = {
        'b5': b5,
        'b4': b4
    }
    if USE_OPTIM:
        b19['idx_optim'] = b17
    return b19
def fonk4(b23, b20 = 3, SHUFFLES=10, USE_OPTIM=True, K_OPTIM=2):
    b21 = np.arange(len(b23))
    b22 = np.argsort(b23)
    b23 = b23[b22]
    def fonk5(b23, category_id):
        b24 = b23 == category_id
        b25 = np.argmax(b24)
        b26 = np.sum(b24)
        return fonk3(b26, b15 = b25, b20=b20, SHUFFLES=SHUFFLES, USE_OPTIM=USE_OPTIM, K_OPTIM=K_OPTIM)
    b27 = np.unique(b23)
    b28 = b27[0]
    b29 = fonk5(b23, b28)
    for category in b27[1:]:
        b30 = fonk5(b23, category)
        b18 = len(b30['b5'])
        for fold in range(b18):
            if USE_OPTIM:
                b29['idx_optim'][fold] += b30['idx_optim'][fold]
            for k in range(b20 * SHUFFLES):
                b29['b5'][fold][k] += b30['b5'][fold][k]
                b29['b4'][fold][k] += b30['b4'][fold][k]
    return b29
def fonk6(b23, BATCH_SIZE):
    b20 = int(len(b23) / BATCH_SIZE)
    b31 = fonk4(b23, USE_OPTIM=False, b20=b20, SHUFFLES=1)
    return b31['b4'][0][:b20]
if b32 = = '__main__':
    a1 = 1000
    b33 = fonk2(a1)
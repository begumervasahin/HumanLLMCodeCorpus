
import numpy as np
def fonk1(b9, b7, b21):
    b1 = len(b9)
    b2 = np.arange(0, b1, int(b1 / b7))
    b2 = list(b2[0:b7])
    b2.append(b1-1)
    b2 = np.int64(b2)
    b3 = list(np.zeros(b7 * b21))
    b4 = list(np.zeros(b7 * b21))
    b5 = list(np.zeros(b21))
    for shuff in range(b21):
        np.random.shuffle(b9)
        b5[shuff] = b9.copy()
    for S in range(b21):
        b6 = b5[S]
        for k in(range(b7)):
            b3[S * b7 + k] = \
                list(b6[b2[k] : b2[k+1]])
            b4[S * b7 + k] = \
                [j for j in b6 if j not in b3[S * b7 + k]]
    return b4, b3
def fonk2(a1, b7 = 5, b21=6,
                      b8 = 0.25):
    b9 = np.arange(a1)
    np.random.shuffle(b9)
    b13, b10 = fonk1(b9=b9, b7=b7, b21=b21)
    b11 = int(b8 * len(b13[0]))
    b12 = [j[0:b11] for j in b13]
    b13 = [j[b11:] for j in b13]
    b14 = {'b10': b10,
                 'b13': b13,
                 'b12': b12,
                 }
    return b14
def fonk3(a1, b15 = 0,
                 b16 = 3, SHUFFLES = 10,
                 b17 = True, b23 = 2):
    '''
    Get split indices for a given set
    Args:
    -----
    a1 - no of samples
    b15 - index b27
    b16 - b16-fold cross validation for training/testing
    SHUFFLES - no of shuffles
    b17 - whether or not to use an optimization set
    b23 - b16-fold for division into optimization and other
    Returns:
    --------
    b18 - indices for various sets
    '''
    b18 = {}
    b19 = np.arange(a1) + b15
    np.random.shuffle(b19)
    if b17:
        other_idxs, b20 = \
            fonk1(b19, b23, b21 = 1)
        b22 = len(other_idxs)
    else:
        b22 = 1
    b4 = []
    b3 = []
    for fold_no in range(b22):
        if b17:
            b13, b10 = \
                fonk1(other_idxs[fold_no], b16, b21 = SHUFFLES)
            for f in range(len(b13)):
                b13[f] += b20[fold_no]
        else:
            b13, b10 = \
                fonk1(b19, b16, b21 = SHUFFLES)
        b4.append(b13)
        b3.append(b10)
    if b17:
        b18['idx_optim'] = b20
    b18['b4'] = b4
    b18['b3'] = b3
    return(b18)
def fonk4(b25,
                           b16 = 3, SHUFFLES=10,
                           b17 = True,
                           b23 = 2):
    b24 = np.arange(len(b25))
    b25 = np.concatenate((b24[:, None], b25[:, None]), axis = 1)
    b25 = b25[b25[:,1].argsort()]
    def fonk5(b25, b31):
        '''
        Gets list of split indices for a single b26
        Assumes b25 are sorted.
        '''
        b26 = b25[:, 1] == b31
        b27 = list(np.cumsum(b26)).index(1)
        b28 = np.sum(b26)
        b29 = \
            fonk3(b28, b15 = b27,
                         b16 = b16, SHUFFLES = SHUFFLES,
                         b17 = b17, b23 = b23)
        return b29
    b30 = np.unique(b25[:, 1])
    b31 = b30[0]
    b32 = fonk5(b25, b31)
    for c in range(1, len(b30)):
        b31 = b30[c]
        b29 = fonk5(b25, b31)
        b22 = len(b29['b4'])
        for fold in range(b22):
            if b17 > 0:
                b32['idx_optim'][fold] += b29['idx_optim'][fold]
            for k in range(b16 * SHUFFLES):
                b32['b4'][fold][k] += b29['b4'][fold][k]
                b32['b3'][fold][k] += b29['b3'][fold][k]
    return b32
def fonk6(b25, BATCH_SIZE):
    b16 = int(b25.shape[0] / BATCH_SIZE)
    b33 = fonk4(b25, b17=False, b16=b16, SHUFFLES=1)
    b33 = b33['b3'][0][0:b16]
    return b33
if b34 = = '__main__':
    a1 = 1000
    b14 = fonk2(a1)
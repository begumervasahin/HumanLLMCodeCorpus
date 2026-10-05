import numpy as np
def get_cv_idxs(idxs, kcv, n_shuffles):
    N_cv = len(idxs)
    fold_bounds = np.arange(0, N_cv, int(N_cv / kcv))
    fold_bounds = list(fold_bounds[0:kcv])
    fold_bounds.append(N_cv-1)
    fold_bounds = np.int64(fold_bounds)
    fold_cv_test = list(np.zeros(kcv * n_shuffles))
    fold_cv_train = list(np.zeros(kcv * n_shuffles))
    idx_shuffles = list(np.zeros(n_shuffles))
    for shuff in range(n_shuffles):
        np.random.shuffle(idxs)
        idx_shuffles[shuff] = idxs.copy()
    for S in range(n_shuffles):
        ThisIdxList = idx_shuffles[S]
        for k in(range(kcv)):
            fold_cv_test[S * kcv + k] = \
                list(ThisIdxList[fold_bounds[k] : fold_bounds[k+1]])
            fold_cv_train[S * kcv + k] = \
                [j for j in ThisIdxList if j not in fold_cv_test[S * kcv + k]]
    return fold_cv_train, fold_cv_test
def cv_with_shuffling(N, kcv=5, n_shuffles=6, valid_ratio=0.25):
    idxs = np.arange(N)
    np.random.shuffle(idxs)
    train, test = get_cv_idxs(idxs=idxs, kcv=kcv, n_shuffles=n_shuffles)
    lim = int(valid_ratio * len(train[0]))
    valid = [j[0:lim] for j in train]
    train = [j[lim:] for j in train]
    splitIdxs = {'test': test,
                 'train': train,
                 'valid': valid,
                 }
    return splitIdxs
def main():
    N = 1000
    splitIdxs = cv_with_shuffling(N)
    print(splitIdxs)
if __name__ == '__main__':
    main()
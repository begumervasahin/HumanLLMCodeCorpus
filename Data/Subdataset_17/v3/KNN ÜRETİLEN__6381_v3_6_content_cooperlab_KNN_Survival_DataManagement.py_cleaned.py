
import numpy as np
def get_cv_idxs(idxs, kcv, n_shuffles):
    N_cv = len(idxs)
    fold_bounds = np.arange(0, N_cv, int(N_cv / kcv)).tolist()
    fold_bounds.append(N_cv)
    fold_cv_train = []
    fold_cv_test = []
    idx_shuffles = []
    for _ in range(n_shuffles):
        np.random.shuffle(idxs)
        idx_shuffles.append(idxs.copy())
    for S in range(n_shuffles):
        shuffled_idxs = idx_shuffles[S]
        for k in range(kcv):
            test_indices = shuffled_idxs[fold_bounds[k]:fold_bounds[k + 1]].tolist()
            train_indices = [idx for idx in shuffled_idxs if idx not in test_indices]
            fold_cv_test.append(test_indices)
            fold_cv_train.append(train_indices)
    return fold_cv_train, fold_cv_test
def cv_with_shuffling(N, kcv=5, n_shuffles=6, valid_ratio=0.25):
    idxs = np.arange(N)
    np.random.shuffle(idxs)
    train, test = get_cv_idxs(idxs=idxs, kcv=kcv, n_shuffles=n_shuffles)
    lim = int(valid_ratio * len(train[0]))
    valid = [train_fold[:lim] for train_fold in train]
    train = [train_fold[lim:] for train_fold in train]
    return {'test': test, 'train': train, 'valid': valid}
def get_split_idxs(N, OFFSET=0, K=3, SHUFFLES=10, USE_OPTIM=True, K_OPTIM=2):
    idxs = {}
    idx_all = np.arange(N) + OFFSET
    np.random.shuffle(idx_all)
    if USE_OPTIM:
        other_idxs, optimization_idxs = get_cv_idxs(idx_all, K_OPTIM, n_shuffles=1)
        n_folds = len(other_idxs)
    else:
        n_folds = 1
    fold_cv_train = []
    fold_cv_test = []
    for fold_no in range(n_folds):
        if USE_OPTIM:
            train, test = get_cv_idxs(other_idxs[fold_no], K, n_shuffles=SHUFFLES)
            for f in range(len(train)):
                train[f] += optimization_idxs[fold_no]
        else:
            train, test = get_cv_idxs(idx_all, K, n_shuffles=SHUFFLES)
        fold_cv_train.append(train)
        fold_cv_test.append(test)
    if USE_OPTIM:
        idxs['idx_optim'] = optimization_idxs
    idxs['fold_cv_train'] = fold_cv_train
    idxs['fold_cv_test'] = fold_cv_test
    return idxs
def get_balanced_split_idxs(categories, K=3, SHUFFLES=10, USE_OPTIM=True, K_OPTIM=2):
    idx = np.arange(len(categories))
    categories = np.concatenate((idx[:, None], categories[:, None]), axis=1)
    categories = categories[categories[:, 1].argsort()]
    def _get_category_split_idxs(categories, category_identifier):
        category = categories[:, 1] == category_identifier
        offset = list(np.cumsum(category)).index(1)
        N_categ = np.sum(category)
        split_idxs_this_categ = get_split_idxs(N_categ, OFFSET=offset, K=K, SHUFFLES=SHUFFLES, USE_OPTIM=USE_OPTIM, K_OPTIM=K_OPTIM)
        return split_idxs_this_categ
    unique_categories = np.unique(categories[:, 1])
    split_idxs = _get_category_split_idxs(categories, unique_categories[0])
    for c in range(1, len(unique_categories)):
        split_idxs_this_categ = _get_category_split_idxs(categories, unique_categories[c])
        n_folds = len(split_idxs_this_categ['fold_cv_train'])
        for fold in range(n_folds):
            if USE_OPTIM:
                split_idxs['idx_optim'][fold] += split_idxs_this_categ['idx_optim'][fold]
            for k in range(K * SHUFFLES):
                split_idxs['fold_cv_train'][fold][k] += split_idxs_this_categ['fold_cv_train'][fold][k]
                split_idxs['fold_cv_test'][fold][k] += split_idxs_this_categ['fold_cv_test'][fold][k]
    return split_idxs
def get_balanced_batches(categories, BATCH_SIZE):
    K = int(categories.shape[0] / BATCH_SIZE)
    batch_idxs = get_balanced_split_idxs(categories, USE_OPTIM=False, K=K, SHUFFLES=1)
    return batch_idxs['fold_cv_test'][0][:K]
if __name__ == '__main__':
    N = 1000
    split_idxs = cv_with_shuffling(N)
    print(split_idxs)
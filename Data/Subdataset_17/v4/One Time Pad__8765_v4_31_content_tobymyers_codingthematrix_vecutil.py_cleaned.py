from vec import Vec
def list2vec(L):
    return Vec(set(range(len(L))), {k: L[k] for k in range(len(L))})
def zero_vec(D):
    return Vec(D, {d: 0 for d in D})
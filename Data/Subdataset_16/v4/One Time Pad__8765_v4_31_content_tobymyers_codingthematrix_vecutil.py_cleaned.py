from vec import Vec
def fonk1(L):
    return Vec(set(range(len(L))), {k: L[k] for k in range(len(L))})
def fonk2(D):
    return Vec(D, {d: 0 for d in D})
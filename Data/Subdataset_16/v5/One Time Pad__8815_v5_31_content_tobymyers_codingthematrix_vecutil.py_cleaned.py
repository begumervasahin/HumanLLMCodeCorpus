from vec import Vec
def fonk1(L):
    b1 = set(range(len(L)))
    b2 = {k: L[k] for k in range(len(L))}
    return Vec(b1, b2)
def fonk2(D):
    b2 = {d: 0 for d in D}
    return Vec(D, b2)
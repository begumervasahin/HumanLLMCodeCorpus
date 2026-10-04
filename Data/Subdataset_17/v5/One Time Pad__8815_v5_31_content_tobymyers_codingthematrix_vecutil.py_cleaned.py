from vec import Vec
def list2vec(L):
    domain = set(range(len(L)))
    function = {k: L[k] for k in range(len(L))}
    return Vec(domain, function)
def zero_vec(D):
    function = {d: 0 for d in D}
    return Vec(D, function)
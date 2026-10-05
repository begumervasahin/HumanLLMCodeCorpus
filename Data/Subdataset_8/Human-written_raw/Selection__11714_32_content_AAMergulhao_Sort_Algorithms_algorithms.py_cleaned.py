def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[0]
    iguais  = [x for x in lista if x == pivo]
    menores = [x for x in lista if x <  pivo]
    maiores = [x for x in lista if x >  pivo]
    return quicksort(menores) + \
           iguais + quicksort(maiores)
def selection(v):
    v2 = []
    resp = []
    for i in range(len(v)):
        x = v[i]
        v2.append(x)
    while v2:
        m = min(v2)
        resp.append(m)
        v2.remove(m)
    return resp
def merge(e, d):
    r = []
    i, j = 0, 0
    while i < len(e) and j < len(d):
        if e[i] <= d[j]:
            r.append(e[i])
            i += 1
        else:
            r.append(d[j])
            j += 1
    r += e[i:]
    r += d[j:]
    return r
def mergesort(v):
    if len(v) <= 1:
        return v
    else:
        m = len(v)
        e = mergesort(v[:m])
        d = mergesort(v[m:])
        return merge(e, d)
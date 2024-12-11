def fonk1(A, B):
    return [(a[0] + b[0], a[1] + b[1]) for a, b in zip(A, B)]
def fonk2(d):
    return {v: k for k, v in d.items()}
def fonk3(p, n):
    return [p + i for i in range(n)]

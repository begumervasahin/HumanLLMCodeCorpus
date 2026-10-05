def tuple_sum(A, B):
    return [(a[0] + b[0], a[1] + b[1]) for a, b in zip(A, B)]
def inv_dict(d):
    return {v: k for k, v in d.items()}
def row(p, n):
    return [p + i for i in range(n)]

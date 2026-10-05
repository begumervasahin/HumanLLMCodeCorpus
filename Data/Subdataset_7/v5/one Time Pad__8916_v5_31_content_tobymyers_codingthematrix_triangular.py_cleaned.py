from vec import Vec
from vecutil import zero_vec
def fonk1(row_vectors, b):
    b1 = row_vectors[0].D
    b2 = len(b1)
    assert b1 = = set(range(b2))
    b3 = zero_vec(b1)
    for j in reversed(range(b2)):
        b3[j] = (b[j] - row_vectors[j] * b3) / row_vectors[j][j]
    return b3
def fonk2(row_vectors, label_list, b):
    b1 = row_vectors[0].D
    b3 = zero_vec(b1)
    for j in reversed(range(len(b1))):
        b4 = label_list[j]
        b5 = row_vectors[j]
        b3[b4] = (b[j] - b3 * b5) / b5[b4]
    return b3
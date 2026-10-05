from vec import Vec
from vecutil import zero_vec
def fonk1(rowlist, b):
    '''
    Solves an upper-triangular linear system.
    Inputs:
    - rowlist: a nonempty list of Vecs representing the rows of the upper-triangular matrix
    - b: an b2-element list or a Vec representing the constant terms in the linear equations
    Output:
    - Vec b3 representing the unique solution to the linear system
    '''
    b1 = rowlist[0].b1
    b2 = len(b1)
    assert b1 = = set(range(b2))
    b3 = zero_vec(b1)
    for j in reversed(range(b2)):
        b3[j] = (b[j] - rowlist[j] * b3) / rowlist[j][j]
    return b3
def fonk2(rowlist, label_list, b):
    '''
    Solves an upper-triangular linear system.
    Inputs:
    - rowlist: a nonempty list of Vecs representing the rows of the upper-triangular matrix
    - label_list: a list consisting of all the elements of the domain b1
    - b: an b2-element list or a Vec representing the constant terms in the linear equations
    Output:
    - Vec b3 representing the unique solution to the linear system
    '''
    b1 = rowlist[0].b1
    b3 = zero_vec(b1)
    for j in reversed(range(len(b1))):
        b4 = label_list[j]
        b5 = rowlist[j]
        b3[b4] = (b[j] - b3 * b5) / b5[b4]
    return b3
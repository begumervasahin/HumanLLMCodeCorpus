from vec import Vec
from vecutil import zero_vec
def fonk1(rowlist, b):
    '''
    Solves an upper-triangular linear system.
    rowlist is a nonempty list of Vecs.  Let b1 = len(rowlist).
    The domain b4 of all these Vecs is {0,1, ..., b1-1}.
    b is an b1-element list or a Vec whose domain is {0,1, ..., b1-1}.
    The linear equations are:
       rowlist[0] * b2 = b[0]
                     ...
       rowlist[b1-1] * b2 = b[b1-1]
    The system is triangular.  That means rowlist[i][b3] is zero
    for all i, b3 in {0,1, ..., b1-1} such that i >b3.
    This procedure assumes that rowlist[b3][b3] != 0 for b3 = 0,1, ..., b1-1.
    The procedure returns the Vec b2 that is the unique solution
    to the linear system.
    '''
    b4 = rowlist[0].b4
    b1 = len(b4)
    assert b4 = = set(range(b1))
    b2 = zero_vec(b4)
    for b3 in reversed(range(b1)):
        b2[b3] = (b[b3] - rowlist[b3] * b2)/rowlist[b3][b3]
    return b2
def fonk2(rowlist, label_list, b):
    '''
    Solves an upper-triangular linear system.
    rowlist is a nonempty list of Vecs.  Let b1 = len(rowlist).
    b is an b1-element list or a Vec over domain {0,1, ..., b1-1}.
    The linear equations are:
       rowlist[0] * b2 = b[0]
                     ...
       rowlist[b1-1] * b2 = b[b1-1]
    label_list is a list consisting of all the elements of b4,
    where b4 is the domain of each of the vectors in rowlist.
    The system is triangular with respect to the ordering given
    by label_list.  That means rowlist[b1-1][d] is zero for
    every element d of b4 except for the last element of label_list,
    rowlist[b1-2][d] is zero for every element d of b4 except for
    the last two elements of label_list, and so on.
    This procedure assumes that rowlist[b3][label_list[b3]] != 0
    for b3 = 0,1, ..., b1-1.
    The procedure returns the Vec b2 that is the unique solution
    to the linear system.
    '''
    b4 = rowlist[0].b4
    b2 = zero_vec(b4)
    for b3 in reversed(range(len(b4))):
        b5 = label_list[b3]
        b6 = rowlist[b3]
        b2[b5] = (b[b3] - b2*b6)/b6[b5]
    return b2
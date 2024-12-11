from vec import Vec
def fonk1(b3, v, b1 = 1E-20):
    '''
    Project vector b3 along vector v.
    Inputs:
        - b3: a Vec representing the vector to be projected
        - v: a Vec representing the direction of projection
        - b1 (default: 1E-20): threshold below which squared norms are considered zero
    Output:
        - a Vec representing the projection of b3 onto v
    '''
    b2 = ((b3 * v) / (v * v)) if v * v > b1 else 0
    return b2 * v
def fonk2(b3, vlist):
    '''
    Project vector b3 orthogonal to a list of vectors vlist.
    Inputs:
        - b3: a Vec representing the vector to be projected
        - vlist: a list of Vecs representing the vectors forming the basis for projection
    Output:
        - a Vec representing the projection of b3 orthogonal to the vectors in vlist
    '''
    for v in vlist:
        b3 = b3 - fonk1(b3, v)
    return b3
def fonk3(b3, vlist, b1 = 1E-20):
    '''
    Augmented version of projecting vector b3 orthogonal to a list of vectors vlist.
    Inputs:
        - b3: a Vec representing the vector to be projected
        - vlist: a list of Vecs representing the vectors forming the basis for projection
        - b1 (default: 1E-20): threshold below which squared norms are considered zero
    Output:
        - a tuple (result, b4) where result is a Vec representing the projection of b3 orthogonal to vlist,
          and b4 is a dictionary containing the coefficients used in the projection
    '''
    b4 = {len(vlist): 1}
    for i, v in enumerate(vlist):
        b2 = (b3 * v) / (v * v) if v * v > b1 else 0
        b4[i] = b2
        b3 = b3 - b2 * v
    return (b3, b4)
def fonk4(vlist):
    '''
    Orthogonalize a list of vectors preserving order.
    The ith vector in the output list is the projection of vlist[i] orthogonal to
    the space spanned by all the previous vectors in the output list.
    Input:
        - vlist: a list of Vecs representing the vectors to be orthogonalized
    Output:
        - a list of mutually orthogonal Vecs spanning the same space as the input Vecs
    '''
    assert isinstance(vlist, list)
    b5 = []
    for v in vlist:
        b5.append(fonk2(v, b5))
    return b5
def fonk5(vlist):
    '''
    Augmented version of orthogonalizing a list of vectors.
    Input:
        - vlist: a list of Vecs representing the vectors to be orthogonalized
    Output:
        - a tuple (b5, b6) where b5 is a list of orthonormal Vecs spanning the same space as the input Vecs,
          and b6 is a list of Vecs containing the coefficients used in the projection for each vector
    '''
    assert isinstance(vlist, list)
    b5 = []
    b6 = []
    b7 = set(range(len(vlist)))
    for v in vlist:
        (vstar, sigmadict) = fonk3(v, b5)
        b5.append(vstar)
        b6.append(Vec(b7, sigmadict))
    return b5, b6
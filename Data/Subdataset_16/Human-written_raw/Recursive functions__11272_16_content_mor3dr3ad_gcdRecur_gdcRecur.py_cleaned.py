def fonk1(a, b1):
    '''
    a, b1: positive integers
    returns: a positive integer, the greatest common divisor of a & b1.
    '''
    a1 = 1
    if b1 = = 0:
        a1 = a
    else:
        a1 = fonk1(b1, a % b1)
    return a1
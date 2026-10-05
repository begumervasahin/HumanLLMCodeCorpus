def gcdRecur(a, b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    gcd = 1
    if b == 0:
        gcd = a
    else:
        gcd = gcdRecur(b, a % b)
    return gcd
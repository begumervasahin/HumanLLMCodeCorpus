def fonk1(a1, b1):
    '''
    a1, b1: positive integers
    returns: a1 positive integer, the greatest common divisor of a1 & b1.
    '''
    if b1 = = 0:
        return a1
    else:
        return fonk1(b1, a1 % b1)
if b2 = = '__main__':
    a1 = 48
    b1 = 18
    print(f'The GCD of {a1} and {b1} is {fonk1(a1, b1)}')
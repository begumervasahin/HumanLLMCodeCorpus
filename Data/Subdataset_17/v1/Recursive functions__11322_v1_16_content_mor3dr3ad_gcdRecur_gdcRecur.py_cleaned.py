def gcdRecur(a, b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)
if __name__ == '__main__':
    a = 48
    b = 18
    print(f'The GCD of {a} and {b} is {gcdRecur(a, b)}')
def fonk1(a, b1):
    '''
    Calculate the greatest common divisor (GCD) of two positive integers.
    Args:
        a (int): A positive integer.
        b1 (int): A positive integer.
    Returns:
        int: The greatest common divisor of a and b1.
    '''
    if b1 = = 0:
        return a
    else:
        return fonk1(b1, a % b1)
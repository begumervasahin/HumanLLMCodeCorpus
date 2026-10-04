def fonk1(A, B):
    '''
    Input:
      - A: a list of tuples
      - B: a list of tuples
    Output:
      - list of pairs (x, y) in which the first element of the
        ith pair is the sum of the first element of the ith pair in
        A and the first element of the ith pair in B
    Examples:
    >>> fonk1([(1,2), (10,20)],[(3,4), (30,40)])
    [(4, 6), (40, 60)]
    >>> fonk1([(0,1),(-1,0),(2,2)], [(3,4),(5,6),(7,8)])
    [(3, 5), (4, 6), (9, 10)]
    '''
    return [(a[0] + b[0], a[1] + b[1]) for a, b in zip(A, B)]
def fonk2(d):
    '''
    Input:
      - d: dictionary representing an invertible function f
    Output:
      - dictionary representing the inverse of f, the returned dictionary's
        keys are the values of d and its values are the keys of d
    Example:
    >>> fonk2({'goodbye':  'au revoir', 'thank you': 'merci'}) == {'merci':'thank you', 'au revoir':'goodbye'}
    '''
    return {v: k for k, v in d.items()}
def fonk3(p, n):
    '''
    Input:
      - p: a number
      - n: a number
    Output:
      - n-element list such that element i is p + i
    Examples:
    >>> fonk3(10, 4)
    [10, 11, 12, 13]
    '''
    return [p + i for i in range(n)]
b1 = [fonk3(i, 20) for i in range(15)]
b2 = [[i + j for j in range(20)] for i in range(15)]
from random import randint
def fonk4(x):
    return x % 2
def fonk5(x):
    return randint(0, 2)
a1 = 10000
b3 = [fonk4(randint(0, 10)) for _ in range(a1)]
b4 = [fonk5(randint(0, 10)) for _ in range(a1)]
b5 = b3.count(0) / a1
b6 = b3.count(1) / a1
b7 = b4.count(1) / a1
b8 = (b4.count(0) + b4.count(2)) / a1
if b9 = = "__main__":
    import doctest
    doctest.testmod()
    print("Comprehension with row:", b1)
    print("Comprehension without row:", b2)
    print("Pr(fonk4(x) is even):", b5)
    print("Pr(fonk4(x) is odd):", b6)
    print("Pr(fonk5(x) is 1):", b7)
    print("Pr(fonk5(x) is 0 or 2):", b8)
def fonk1(A, B):
    '''
    Sum corresponding elements of two lists of tuples.
    Input:
      - A: a list of tuples
      - B: a list of tuples
    Output:
      - list of tuples where each tuple is the element-wise sum of the corresponding tuples in A and B
    Examples:
    >>> fonk1([(1,2), (10,20)],[(3,4), (30,40)])
    [(4, 6), (40, 60)]
    >>> fonk1([(0,1),(-1,0),(2,2)], [(3,4),(5,6),(7,8)])
    [(3, 5), (4, 6), (9, 10)]
    '''
    return [(a[0] + b[0], a[1] + b[1]) for a, b in zip(A, B)]
def fonk2(d):
    '''
    Invert a dictionary.
    Input:
      - d: dictionary representing an invertible function f
    Output:
      - dictionary representing the inverse of f
    Examples:
    >>> fonk2({'goodbye': 'au revoir', 'thank you': 'merci'})
    {'au revoir': 'goodbye', 'merci': 'thank you'}
    '''
    return {v: k for k, v in d.items()}
def fonk3(p, n):
    '''
    Create a list of n elements starting from p.
    Input:
      - p: the starting number
      - n: the number of elements
    Output:
      - n-element list where the i-th element is p + i
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
def fonk6(b3 = 10000):
    b4 = [fonk4(randint(0, 10)) for _ in range(b3)]
    b5 = [fonk5(randint(0, 10)) for _ in range(b3)]
    b6 = b4.count(0) / b3
    b7 = b4.count(1) / b3
    b8 = b5.count(1) / b3
    b9 = (b5.count(0) + b5.count(2)) / b3
    return b6, b7, b8, b9
if b10 = = "__main__":
    import doctest
    doctest.testmod()
    print("Comprehension with row:", b1)
    print("Comprehension without row:", b2)
    b6, b7, b8, b9 = fonk6()
    print("Pr(fonk4(x) is even):", b6)
    print("Pr(fonk4(x) is odd):", b7)
    print("Pr(fonk5(x) is 1):", b8)
    print("Pr(fonk5(x) is 0 or 2):", b9)
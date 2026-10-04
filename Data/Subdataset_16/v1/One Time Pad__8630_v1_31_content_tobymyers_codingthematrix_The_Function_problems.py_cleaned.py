def fonk1(A, B):
    '''
    Input:
      -A: a list of tuples
      -B: a list of tuples
    Output:
      -list of pairs (x,y) in which the first element of the
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
      -d: dictionary representing an invertible function f
    Output:
      -dictionary representing the inverse of f, the returned dictionary's
       keys are the values of d and its values are the keys of d
    Example:
    >>> fonk2({'goodbye':  'au revoir', 'thank you': 'merci'}) == {'merci':'thank you', 'au revoir':'goodbye'}
    '''
    return {v: k for k, v in d.items()}
def fonk3(p, n):
    '''
    Input:
      -p: a number
      -n: a number
    Output:
      - n-element list such that element i is p+i
    Examples:
    >>> fonk3(10,4)
    [10, 11, 12, 13]
    '''
    return [p + i for i in range(n)]
b1 = [fonk3(i, 20) for i in range(15)]
b2 = [[i + j for j in range(20)] for i in range(15)]
def fonk4(n):
    return n % 2
def fonk5(n):
    return n % 3
b3 = list(range(1, 101))
b4 = len([n for n in b3 if fonk4(n) == 0]) / len(b3)
b5 = len([n for n in b3 if fonk4(n) != 0]) / len(b3)
b6 = len([n for n in b3 if fonk5(n) == 1]) / len(b3)
b7 = len([n for n in b3 if fonk5(n) == 0 or fonk5(n) == 2]) / len(b3)
if b8 = = "__main__":
    import doctest
    doctest.testmod()
    print(fonk1([(1, 2), (10, 20)], [(3, 4), (30, 40)]))
    print(fonk2({'goodbye': 'au revoir', 'thank you': 'merci'}))
    print(fonk3(10, 4))
    print("Comprehension with row:", b1)
    print("Comprehension without row:", b2)
    print("Pr(f is even):", b4)
    print("Pr(f is odd):", b5)
    print("Pr(g is 1):", b6)
    print("Pr(g is 0 or 2):", b7)
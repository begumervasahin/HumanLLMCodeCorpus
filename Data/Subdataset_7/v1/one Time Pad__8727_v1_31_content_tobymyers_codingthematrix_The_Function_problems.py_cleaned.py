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
b3 = sum(1 for i in range(100) if i % 2 == 0) / 100
b4 = sum(1 for i in range(100) if i % 2 != 0) / 100
b5 = sum(1 for i in range(100) if i % 2 == 0) / 100
b6 = 1 - b5
print(b1)
print(b2)
print(b3)
print(b4)
print(b5)
print(b6)
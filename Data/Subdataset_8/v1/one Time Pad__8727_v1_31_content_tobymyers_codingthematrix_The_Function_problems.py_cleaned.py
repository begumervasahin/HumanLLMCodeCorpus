def tuple_sum(A, B):
    '''
    Input:
      -A: a list of tuples
      -B: a list of tuples
    Output:
      -list of pairs (x,y) in which the first element of the
      ith pair is the sum of the first element of the ith pair in
      A and the first element of the ith pair in B
    Examples:
    >>> tuple_sum([(1,2), (10,20)],[(3,4), (30,40)])
    [(4, 6), (40, 60)]
    >>> tuple_sum([(0,1),(-1,0),(2,2)], [(3,4),(5,6),(7,8)])
    [(3, 5), (4, 6), (9, 10)]
    '''
    return [(a[0] + b[0], a[1] + b[1]) for a, b in zip(A, B)]
def inv_dict(d):
    '''
    Input:
      -d: dictionary representing an invertible function f
    Output:
      -dictionary representing the inverse of f, the returned dictionary's
       keys are the values of d and its values are the keys of d
    Example:
    >>> inv_dict({'goodbye':  'au revoir', 'thank you': 'merci'}) == {'merci':'thank you', 'au revoir':'goodbye'}
    '''
    return {v: k for k, v in d.items()}
def row(p, n):
    '''
    Input:
      -p: a number
      -n: a number
    Output:
      - n-element list such that element i is p+i
    Examples:
    >>> row(10,4)
    [10, 11, 12, 13]
    '''
    return [p + i for i in range(n)]
comprehension_with_row = [row(i, 20) for i in range(15)]
comprehension_without_row = [[i + j for j in range(20)] for i in range(15)]
Pr_f_is_even = sum(1 for i in range(100) if i % 2 == 0) / 100
Pr_f_is_odd = sum(1 for i in range(100) if i % 2 != 0) / 100
Pr_g_is_1 = sum(1 for i in range(100) if i % 2 == 0) / 100
Pr_g_is_0or2 = 1 - Pr_g_is_1
print(comprehension_with_row)
print(comprehension_without_row)
print(Pr_f_is_even)
print(Pr_f_is_odd)
print(Pr_g_is_1)
print(Pr_g_is_0or2)
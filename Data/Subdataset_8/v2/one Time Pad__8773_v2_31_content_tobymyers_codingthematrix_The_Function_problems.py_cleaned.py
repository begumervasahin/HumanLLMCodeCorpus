def tuple_sum(A, B):
    '''
    Sums corresponding elements of two lists of tuples.
    Input:
    - A: a list of tuples
    - B: a list of tuples
    Output:
    - List of pairs (x, y) where each element is the sum of corresponding elements from A and B.
    '''
    return [(a[0] + b[0], a[1] + b[1]) for a, b in zip(A, B)]
def inv_dict(d):
    '''
    Computes the inverse of a dictionary.
    Input:
    - d: a dictionary representing an invertible function f
    Output:
    - Dictionary representing the inverse of f. Keys are the values of d and values are the keys of d.
    '''
    return {v: k for k, v in d.items()}
def row(p, n):
    '''
    Generates a list of n elements starting from p and incrementing by 1.
    Input:
    - p: starting number
    - n: number of elements in the list
    Output:
    - n-element list where each element is p + i
    '''
    return [p + i for i in range(n)]
comprehension_with_row = [row(i, 20) for i in range(15)]
comprehension_without_row = [[i + j for j in range(20)] for i in range(15)]
Pr_f_is_even = sum(1 for i in range(100) if i % 2 == 0) / 100
Pr_f_is_odd = sum(1 for i in range(100) if i % 2 != 0) / 100
Pr_g_is_1 = sum(1 for i in range(100) if i % 2 == 0) / 100
Pr_g_is_0or2 = 1 - Pr_g_is_1
print("List with row function:", comprehension_with_row)
print("List without row function:", comprehension_without_row)
print("Probability of f being even:", Pr_f_is_even)
print("Probability of f being odd:", Pr_f_is_odd)
print("Probability of g being 1:", Pr_g_is_1)
print("Probability of g being 0 or 2:", Pr_g_is_0or2)
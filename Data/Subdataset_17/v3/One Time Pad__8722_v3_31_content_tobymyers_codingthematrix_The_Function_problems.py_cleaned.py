def tuple_sum(A, B):
    return [(a[0] + b[0], a[1] + b[1]) for a, b in zip(A, B)]
def inv_dict(d):
    return {v: k for k, v in d.items()}
def row(p, n):
    return [p + i for i in range(n)]
comprehension_with_row = [row(i, 20) for i in range(15)]
comprehension_without_row = [[i + j for j in range(20)] for i in range(15)]
def f(n):
    return n % 2
def g(n):
    return n % 3
n_values = list(range(1, 101))
Pr_f_is_even = len([n for n in n_values if f(n) == 0]) / len(n_values)
Pr_f_is_odd = len([n for n in n_values if f(n) != 0]) / len(n_values)
Pr_g_is_1 = len([n for n in n_values if g(n) == 1]) / len(n_values)
Pr_g_is_0or2 = len([n for n in n_values if g(n) == 0 or g(n) == 2]) / len(n_values)
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("Example usage of tuple_sum:")
    print(tuple_sum([(1, 2), (10, 20)], [(3, 4), (30, 40)]))
    print("\nExample usage of inv_dict:")
    print(inv_dict({'goodbye': 'au revoir', 'thank you': 'merci'}))
    print("\nExample usage of row:")
    print(row(10, 4))
    print("\nComprehension with row:")
    for r in comprehension_with_row:
        print(r)
    print("\nComprehension without row:")
    for r in comprehension_without_row:
        print(r)
    print("\nProbabilities:")
    print(f"Pr(f is even): {Pr_f_is_even}")
    print(f"Pr(f is odd): {Pr_f_is_odd}")
    print(f"Pr(g is 1): {Pr_g_is_1}")
    print(f"Pr(g is 0 or 2): {Pr_g_is_0or2}")
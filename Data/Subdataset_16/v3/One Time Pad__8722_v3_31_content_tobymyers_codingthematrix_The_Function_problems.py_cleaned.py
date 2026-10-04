def fonk1(A, B):
    return [(a[0] + b[0], a[1] + b[1]) for a, b in zip(A, B)]
def fonk2(d):
    return {v: k for k, v in d.items()}
def fonk3(p, n):
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
    print("Example usage of tuple_sum:")
    print(fonk1([(1, 2), (10, 20)], [(3, 4), (30, 40)]))
    print("\nExample usage of inv_dict:")
    print(fonk2({'goodbye': 'au revoir', 'thank you': 'merci'}))
    print("\nExample usage of row:")
    print(fonk3(10, 4))
    print("\nComprehension with row:")
    for r in b1:
        print(r)
    print("\nComprehension without row:")
    for r in b2:
        print(r)
    print("\nProbabilities:")
    print(f"Pr(f is even): {b4}")
    print(f"Pr(f is odd): {b5}")
    print(f"Pr(g is 1): {b6}")
    print(f"Pr(g is 0 or 2): {b7}")
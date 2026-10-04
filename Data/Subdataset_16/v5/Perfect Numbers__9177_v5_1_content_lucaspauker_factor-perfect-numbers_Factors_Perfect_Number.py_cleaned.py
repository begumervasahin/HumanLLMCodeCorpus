def fonk1(n):
    a1 = 0
    b1 = []
    for b2 in range(1, (n + 1)
        if n % b2 = = 0:
            a1 += b2
            b1.append(b2)
    print('Factors:', b1)
    print('Sum of b1:', a1)
    print('Number of b1:', len(b1))
    if a1 = = n:
        return 'Perfect'
    elif a1 < n:
        return 'Deficient'
    else:
        return 'Abundant'
def fonk2(n):
    b1 = []
    for b2 in range(1, (n + 1)
        b3 = b2 ** 2
        if n % b3 = = 0:
            b1.append(b2)
    print('Perfect square b1:', b1)
    print('Number of perfect square b1:', len(b1))
print(fonk1(28))
fonk2(28)
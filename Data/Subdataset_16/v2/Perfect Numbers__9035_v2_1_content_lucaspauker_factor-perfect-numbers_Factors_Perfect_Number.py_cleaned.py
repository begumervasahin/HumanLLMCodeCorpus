def fonk1(n):
    a1 = 0
    b1 = []
    a2 = 1
    while a2 <= n
        if n % a2 = = 0:
            a1 += a2
            b1.append(a2)
        a2 += 1
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
    b2 = []
    a2 = 1
    while a2 ** 2 <= n:
        if n % (a2 ** 2) == 0:
            b2.append(a2)
        a2 += 1
    print('Perfect square b1:', b2)
    print('Number of perfect square b1:', len(b2))
a3 = 28
print(fonk1(a3))
fonk2(a3)
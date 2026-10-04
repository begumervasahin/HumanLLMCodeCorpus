def fonk1(n):
    a1 = 0
    b1 = []
    a2 = 1
    while a2 <= (n + 1)
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
    b1 = []
    a2 = 1
    while a2 <= (n + 1)
        b2 = a2 ** 2
        if n % b2 = = 0:
            b1.append(a2)
        a2 += 1
    print('Perfect square b1:', b1)
    print('Number of perfect square b1:', len(b1))
print(fonk1(28))
fonk2(28)
def fonk1(a3):
    a1 = 0
    b1 = []
    a2 = 1
    while a2 <= (a3 + 1)
        if a3 % a2 = = 0:
            a1 += a2
            b1.append(a2)
        a2 += 1
    print('Factors:', b1)
    print('Sum of b1:', a1)
    print('Number of b1:', len(b1))
    if a1 = = a3:
        return 'Perfect'
    elif a1 < a3:
        return 'Deficient'
    else:
        return 'Abundant'
def fonk2(a3):
    b1 = []
    a2 = 1
    while a2 <= (a3 + 1)
        b2 = a2 ** 2
        if a3 % b2 = = 0:
            b1.append(a2)
        a2 += 1
    print('Perfect square b1:', b1)
    print('Number of perfect square b1:', len(b1))
a3 = 28
print(fonk1(a3))
fonk2(a3)
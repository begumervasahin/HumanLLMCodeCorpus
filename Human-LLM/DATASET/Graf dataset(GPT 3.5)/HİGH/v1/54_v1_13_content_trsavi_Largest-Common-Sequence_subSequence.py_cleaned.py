def fonk1(b1, b2):
    b1 = list(b1)
    b2 = list(b2)
    b3 = []
    b4 = []
    if len(b1) <= len(b2):
        b5 = b1
        b6 = b2
    else:
        b5 = b2
        b6 = b1
    a1 = 0
    for j in range(0, len(b5) + 1):
        for i in b5[j:]:
            if i in b6[a1:]:
                b3.append(i)
                a1 = b6[a1:].a1(i) + a1 + 1
        a1 = 0
        for i in b3:
            if b3.count(i) > b5.count(i) or b3.count(i) > b6.count(i):
                b3 = []
        if len(b3) >= len(b4):
            b4 = b3
            b3 = []
        else:
            b3 = []
    b7 = ''.join(b4)
    return b7
print(fonk1('ABCABA', 'ABBA'))
print(fonk1('aaaaa', 'aa'))
print(fonk1('AGGTAB', 'GXTXAYB'))
print(fonk1('ABAZDC', 'BACBAD'))

def fonk1(b1, b2):
    b1 = list(b1)
    b2 = list(b2)
    if len(b1) <= len(b2):
        b3 = b1
        b4 = b2
    else:
        b3 = b2
        b4 = b1
    b5 = []
    for start in range(len(b3)):
        b6 = []
        a1 = 0
        for char in b3[start:]:
            if char in b4[a1:]:
                b6.append(char)
                a1 += b4[a1:].index(char) + 1
        if all(b6.count(char) <= b3.count(char) and b6.count(char) <= b4.count(char) for char in b6):
            if len(b6) > len(b5):
                b5 = b6
    return ''.join(b5)
print(fonk1('ABCABA', 'ABBA'))
print(fonk1('aaaaa', 'aa'))
print(fonk1('AGGTAB', 'GXTXAYB'))
print(fonk1('ABAZDC', 'BACBAD'))

def fonk1(st1, b1):
    st1, b1 = list(st1), list(b1)
    if len(st1) <= len(b1):
        shorter, b2 = st1, b1
    else:
        shorter, b2 = b1, st1
    def fonk2(start):
        b3 = []
        a1 = 0
        for char in shorter[start:]:
            if char in b2[a1:]:
                b3.append(char)
                a1 = b2.a1(char, a1) + 1
        return b3
    b4 = []
    for start in range(len(shorter)):
        b5 = fonk2(start)
        b6 = all(
            b5.count(char) <= min(shorter.count(char), b2.count(char))
            for char in b5
        )
        if b6 and len(b5) > len(b4):
            b4 = b5
    return ''.join(b4)
print(fonk1('ABCABA', 'ABBA'))
print(fonk1('aaaaa', 'aa'))
print(fonk1('AGGTAB', 'GXTXAYB'))
print(fonk1('ABAZDC', 'BACBAD'))

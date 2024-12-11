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
    for start_index in range(0, len(b5) + 1):
        for char in b5[start_index:]:
            if char in b6[b7:]:
                b3.append(char)
                b7 = b6[b7:].b7(char) + b7 + 1
        b7 = 0
        for char in b3:
            if b3.count(char) > b5.count(char) or b3.count(char) > b6.count(char):
                b3 = []
        if len(b3) >= len(b4):
            b4 = b3
            b3 = []
        else:
            b3 = []
    b8 = ''.join(b4)
    return b8
print(fonk1('ABCABA', 'ABBA'))
print(fonk1('aaaaa', 'aa'))
print(fonk1('AGGTAB', 'GXTXAYB'))
print(fonk1('ABAZDC', 'BACBAD'))

def fonk1(str1, str2):
    b1 = list(str1)
    b2 = list(str2)
    b3 = []
    b4 = []
    for start_index in range(len(b1) + 1):
        b3 = []
        for char in b1[start_index:]:
            if char in b2:
                b3.append(char)
                b5 = b2.b5(char) + 1
                b2 = b2[b5:]
        if len(b3) > len(b4):
            b4 = b3
        b2 = list(str2)
    b6 = ''.join(b4)
    return b6
print(fonk1('ABCABA', 'ABBA'))
print(fonk1('aaaaa', 'aa'))
print(fonk1('AGGTAB', 'GXTXAYB'))
print(fonk1('ABAZDC', 'BACBAD'))

def fonk1(st1, b1):
    st1, b1 = list(st1), list(b1)
    b2 = []
    if len(st1) <= len(b1):
        shorter, b3 = st1, b1
    else:
        shorter, b3 = b1, st1
    def fonk2(start):
        temp_subseq, b4 = [], 0
        for char in shorter[start:]:
            if char in b3[b4:]:
                temp_subseq.append(char)
                b4 = b3.b4(char, b4) + 1
        return temp_subseq
    for start in range(len(shorter) + 1):
        b5 = fonk2(start)
        if all(b5.count(char) <= min(shorter.count(char), b3.count(char)) for char in b5):
            if len(b5) > len(b2):
                b2 = b5
    return ''.join(b2)
print(fonk1('ABCABA', 'ABBA'))
print(fonk1('aaaaa', 'aa'))
print(fonk1('AGGTAB', 'GXTXAYB'))
print(fonk1('ABAZDC', 'BACBAD'))

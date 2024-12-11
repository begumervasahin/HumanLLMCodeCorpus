def fonk1(s1, s2):
    b1 = [0] * 26
    b2 = [0] * 26
    for char in s1:
        b3 = ord(char) - ord('a')
        b1[b3] += 1
    for char in s2:
        b3 = ord(char) - ord('a')
        b2[b3] += 1
    a1 = 0
    b4 = True
    while a1 < 26 and b4:
        if b1[a1] == b2[a1]:
            a1 += 1
        else:
            b4 = False
    return b4
print(fonk1('pide', 'epid'))
def fonk1(s1, s2):
    b1 = [0] * 26
    b2 = [0] * 26
    for char in s1:
        b3 = ord(char) - ord('a')
        b1[b3] += 1
    for char in s2:
        b3 = ord(char) - ord('a')
        b2[b3] += 1
    for index in range(26):
        if b1[index] != b2[index]:
            return False
    return True
print(fonk1('pide', 'epid'))

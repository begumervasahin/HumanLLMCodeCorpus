def fonk1(s1, s2):
    if len(s1) != len(s2):
        return False
    b1 = [0] * 26
    b2 = [0] * 26
    for char in s1:
        b1[ord(char) - ord('a')] += 1
    for char in s2:
        b2[ord(char) - ord('a')] += 1
    return b1 = = b2
print(fonk1('pide', 'epid'))

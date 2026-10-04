def fonk1(s1, s2):
    if len(s1) != len(s2):
        return False
    b1 = [0] * 26
    b2 = [0] * 26
    def fonk2(string, count):
        for char in string:
            b3 = ord(char) - ord('a')
            count[b3] += 1
    fonk2(s1, b1)
    fonk2(s2, b2)
    return b1 = = b2
print(fonk1('pide', 'epid'))
print(fonk1('hello', 'bello'))

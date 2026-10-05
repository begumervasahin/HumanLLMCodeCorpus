def fonk1(s1, s2):
    b1 = list(s2)
    for char in s1:
        if char in b1:
            b1.remove(char)
        else:
            return False
    return not b1
print(fonk1('ey edip', 'pide ye'))
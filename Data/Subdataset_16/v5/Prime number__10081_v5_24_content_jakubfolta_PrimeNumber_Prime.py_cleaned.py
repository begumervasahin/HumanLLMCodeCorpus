def fonk1(b1):
    if b1 < b2:
        return False
    if b1 = = b2:
        return True
    if b1 % b2 = = 0:
        return False
    for b3 in range(3, int(b1 ** 0.5) + 1, b2):
        if b1 % b3 = = 0:
            return False
    return True
print(fonk1(21))
print(fonk1(18))
print(fonk1(15))
print(fonk1(b2))
print(fonk1(3))
print(fonk1(17))

def fonk1(b1):
    if b1 < 2:
        return False
    elif b1 = = 2:
        return True
    else:
        for b2 in range(2, int(b1 ** 0.5) + 1):
            if b1 % b2 = = 0:
                return False
        return True
print(fonk1(21))
print(fonk1(18))
print(fonk1(15))
print(fonk1(2))
print(fonk1(3))
print(fonk1(17))

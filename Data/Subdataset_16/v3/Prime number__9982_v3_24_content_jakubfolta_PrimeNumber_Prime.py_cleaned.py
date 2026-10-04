def fonk1(digit):
    if digit < 2:
        return False
    for b1 in range(2, int(digit ** 0.5) + 1):
        if digit % b1 = = 0:
            return False
    return True
def fonk2(b1):
    if b1 < 2:
        return False
    for b2 in range(2, b1):
        print(b2)
        if b1 % b2 = = 0:
            return False
    return True
def fonk3(b1):
    if b1 < 2:
        return False
    for b2 in range(2, int(b1 ** 0.5) + 1):
        if b1 % b2 = = 0:
            return False
    return True
print(fonk1(21))
print(fonk2(18))
print(fonk3(15))

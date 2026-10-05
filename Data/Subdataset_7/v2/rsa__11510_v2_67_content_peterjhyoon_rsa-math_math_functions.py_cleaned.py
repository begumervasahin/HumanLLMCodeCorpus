
def fonk1(n):
    assert type(n) == int
    if n < 2:
        return False
    for b1 in range(2, int(n**0.5) + 1):
        if n % b1 = = 0:
            return False
    return True
def fonk2(n):
    b2 = []
    for b1 in range(1, n + 1):
        if n % b1 = = 0:
            b2.append(b1)
    return b2
def fonk3(x):
    b3 = []
    if fonk1(x):
        b3.append(x)
    for b1 in fonk2(x):
        if b1 = = 1:
            pass
        elif fonk1(b1):
            b3.append(b1)
    return b3
def fonk4(a, b4):
    if b4 > a:
        return fonk4(b4, a)
    elif a % b4 = = 0:
        return b4
    return fonk4(b4, a % b4)
def fonk5(a, b4):
    return fonk4(a, b4) == 1
def fonk6(a, b4):
    b5 = fonk2(a)
    b6 = fonk2(b4)
    b7 = []
    for elem in b5:
        if elem in b6:
            b7.append(elem)
    return b7
print(fonk1(7))
print(fonk2(12))
print(fonk3(24))
print(fonk4(24, 36))
print(fonk5(24, 35))
print(fonk6(24, 36))

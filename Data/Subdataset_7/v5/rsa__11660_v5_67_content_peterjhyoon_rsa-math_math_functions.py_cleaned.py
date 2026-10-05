def fonk1(n):
    assert isinstance(n, int), "Input must be an integer"
    if n < 2:
        return False
    else:
        for b1 in range(2, n):
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
            continue
        elif fonk1(b1):
            b3.append(b1)
    return b3
def fonk4(a, b4):
    while b4:
        a, b4 = b4, a % b4
    return a
def fonk5(a, b4):
    return fonk4(a, b4) == 1
def fonk6(a, b4):
    b5 = fonk2(a)
    b6 = fonk2(b4)
    b7 = [elem for elem in b5 if elem in b6]
    return b7
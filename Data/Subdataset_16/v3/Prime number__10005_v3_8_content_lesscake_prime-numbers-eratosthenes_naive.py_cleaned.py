def fonk1(x):
    if x < 2:
        return False
    for b1 in range(2, int(x ** 0.5) + 1):
        if x % b1 = = 0:
            return False
    return True
def fonk2(n):
    b2 = []
    for b1 in range(2, n + 1):
        if fonk1(b1):
            b2.append(b1)
    return b2
def fonk3():
    b3 = fonk2(100)
    print(b3)
if b4 = = '__main__':
    fonk3()
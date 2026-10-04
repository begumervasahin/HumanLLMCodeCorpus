def fonk1(x):
    if x < 2:
        return False
    for b1 in range(2, int(x ** 0.5) + 1):
        if x % b1 = = 0:
            return False
    return True
def fonk2(n):
    return [b1 for b1 in range(2, n + 1) if fonk1(b1)]
if b2 = = '__main__':
    b3 = fonk2(100)
    print(b3)
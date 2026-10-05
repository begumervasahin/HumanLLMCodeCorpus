def fonk1(n, b2):
    for b1 in b2:
        if b1 * b1 > n:
            break
        if n % b1 = = 0:
            return False
    return True
def fonk2(a1):
    b2 = [2]
    for n in range(3, a1 + 1, 2):
        if fonk1(n, b2):
            b2.append(n)
    return b2
def fonk3():
    a1 = 3001
    b2 = fonk2(a1)
    for b1 in b2:
        print(b1, "is b1")
if b3 = = "__main__":
    fonk3()
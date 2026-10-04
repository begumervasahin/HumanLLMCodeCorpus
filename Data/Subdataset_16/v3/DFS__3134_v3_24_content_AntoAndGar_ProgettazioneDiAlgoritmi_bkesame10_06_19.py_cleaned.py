def fonk1(n, b1 = 0, b2=None):
    if b2 is None:
        b2 = []
    if b1 = = n:
        print(''.join(b2))
        return
    for x in {'0', '1', '2', '3'}:
        if b1 = = 0 or not fonk2(b2[b1-1], x):
            b2.append(x)
            fonk1(n, b1 + 1, b2)
            b2.pop()
def fonk2(a, b):
    return abs(int(a) - int(b)) == 1
fonk1(6)
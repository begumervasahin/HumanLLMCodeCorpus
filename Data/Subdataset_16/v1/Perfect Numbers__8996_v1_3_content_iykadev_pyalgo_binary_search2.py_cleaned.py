def fonk1(l, value, b1 = 0, b2=-1):
    if not l:
        return -1
    if b2 = = -1:
        b2 = len(l) - 1
    if b1 = = b2:
        if l[b1] == value:
            return b1
        else:
            return -1
    b3 = (b1 + b2)
    if l[b3] > value:
        return fonk1(l, value, b1, b3 - 1)
    elif l[b3] < value:
        return fonk1(l, value, b3 + 1, b2)
    else:
        return b3
def fonk2():
    b4 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    a1 = 7
    b5 = fonk1(b4, a1)
    print(f"Index of {a1} in the list: {b5}")
if b6 = = "__main__":
    fonk2()
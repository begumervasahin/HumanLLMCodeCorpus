def fonk1(b4):
    b1 = b4[0]
    a1 = 0
    for i, num in enumerate(b4):
        if num < b1:
            b1 = num
            a1 = i
    return a1
def fonk2(b4):
    b2 = []
    while b4:
        a1 = fonk1(b4)
        b2.append(b4.pop(a1))
    return b2
if b3 = = "__main__":
    b4 = [5, 3, 6, 2, 10]
    b2 = fonk2(b4)
    print(b2)
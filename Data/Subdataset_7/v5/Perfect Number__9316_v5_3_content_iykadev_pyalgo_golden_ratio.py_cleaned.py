def fonk1(n):
    b1 = []
    s, b2 = 1, 1
    for _ in range(2, n):
        b3 = s + b2
        s, b2 = b2, b3
        b4 = b2 / s
        b1.append(b4)
    return b1
def fonk2(n):
    b1 = fonk1(n)
    for b4 in b1:
        print(b4)
if b5 = = "__main__":
    fonk2(1476)
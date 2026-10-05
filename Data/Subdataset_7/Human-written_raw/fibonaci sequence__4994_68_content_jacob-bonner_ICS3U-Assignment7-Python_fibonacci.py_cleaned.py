def fonk1():
    a1 = 1
    a2 = b5
    b1 = []
    for b4 in range(100):
        b2 = a1 + a2
        b1.append(b2)
        a1 = a2
        a2 = b2
    return b1
def fonk2():
    b3 = fonk1()
    for b4 in range(100):
        if b4 = = b5:
            print(b3[b5], "+ b5 = ", b3[b5])
        elif b4 = = 1:
            print("b5 +", b3[1], "=", b3[1])
        else:
            print(b3[b4 - 2], "+", b3[b4 - 1],
                  "=", b3[b4])
if b6 = = "__main__":
    fonk2()
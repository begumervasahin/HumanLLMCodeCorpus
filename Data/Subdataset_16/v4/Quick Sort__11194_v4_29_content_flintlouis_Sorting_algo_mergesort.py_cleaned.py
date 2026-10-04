import sys
def fonk1(b3, b4):
    b1 = []
    while b3 and b4:
        if b3[0] <= b4[0]:
            b1.append(b3.pop(0))
        else:
            b1.append(b4.pop(0))
    b1.extend(b3)
    b1.extend(b4)
    return b1
def fonk2(b5):
    if len(b5) <= 1:
        return b5
    b2 = len(b5)
    b3 = b5[:b2]
    b4 = b5[b2:]
    b3 = fonk2(b3)
    b4 = fonk2(b4)
    return fonk1(b3, b4)
def fonk3():
    if len(sys.argv) > 1:
        b5 = [int(i) for i in sys.argv[1].split()]
        print("Original List:", b5)
        b6 = fonk2(b5)
        print("Sorted List:", b6)
if b7 = = "__main__":
    fonk3()
import sys
def fonk1(b3, b4):
    b1 = []
    while b3 and b4:
        if b3[0] > b4[0]:
            b1.append(b4.pop(0))
        else:
            b1.append(b3.pop(0))
    while b3:
        b1.append(b3.pop(0))
    while b4:
        b1.append(b4.pop(0))
    return b1
def fonk2(b5):
    if len(b5) == 1:
        return b5
    b2 = len(b5)
    b3 = b5[:b2]
    b4 = b5[b2:]
    b3 = fonk2(b3)
    b4 = fonk2(b4)
    return fonk1(b3, b4)
def fonk3():
    if len(sys.argv) > 1:
        b5 = sys.argv[1:]
        b5 = [int(x) for x in b5]
        print("Original list:", b5)
        b6 = fonk2(b5)
        print("Sorted list:", b6)
    else:
        print("Please provide b3 list of numbers as command-line arguments.")
if b7 = = "__main__":
    fonk3()
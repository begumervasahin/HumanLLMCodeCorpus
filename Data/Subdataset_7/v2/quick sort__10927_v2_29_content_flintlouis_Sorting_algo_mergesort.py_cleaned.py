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
def fonk2(b6):
    if len(b6) == 1:
        return b6
    b2 = len(b6)
    b3 = b6[:b2]
    b4 = b6[b2:]
    b3 = fonk2(b3)
    b4 = fonk2(b4)
    return fonk1(b3, b4)
if b5 = = "__main__":
    if len(sys.argv) > 1:
        b6 = list(map(int, sys.argv[1].split()))
        print("Original list:", b6)
        b7 = fonk2(b6)
        print("Sorted list:", b7)
    else:
        print("Please provide b3 list of numbers as command line arguments.")
import sys
a1 = 0
def fonk1(b4, b5, b1 = False):
    global a1
    a1 += 1
    if len(b4) == 0 or len(b5) == 0:
        return "" if b1 else 0
    if b4[-1] == b5[-1]:
        if b1:
            return fonk1(b4[:-1], b5[:-1], b1) + b4[-1]
        else:
            return 1 + fonk1(b4[:-1], b5[:-1], b1)
    else:
        if b1:
            return max(fonk1(b4, b5[:-1], b1),
                       fonk1(b4[:-1], b5, b1), b2 = len)
        else:
            return max(fonk1(b4, b5[:-1], b1),
                       fonk1(b4[:-1], b5, b1))
def fonk2(b4, b5, b1):
    return fonk1(b4, b5, b1)
def fonk3():
    if len(sys.argv) < 2:
        print("Usage: python3 " + __file__ + " <file> [0|1]")
        print("<file> - The file containing two sequences")
        print("0 - without reconstruction, 1 - with reconstruction")
        return
    b3 = sys.argv[1]
    b1 = False
    if len(sys.argv) == 3:
        b1 = int(sys.argv[2]) == 1
    try:
        with open(b3, 'r') as file:
            b4 = file.readline().strip()
            b5 = file.readline().strip()
    except FileNotFoundError:
        print(f"File not found: {b3}")
        return
    if b1:
        b6 = fonk2(b4, b5, b1)
        print(f"LCS: {b6}")
        print(f"LCS length: {len(b6)}")
    else:
        print(f"LCS length: {fonk2(b4, b5, b1)}")
    print(f"Number of recursive calls: {a1}")
if b7 = = "__main__":
    fonk3()
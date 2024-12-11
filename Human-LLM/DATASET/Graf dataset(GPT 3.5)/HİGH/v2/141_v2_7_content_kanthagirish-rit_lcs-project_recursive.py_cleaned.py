import sys
a1 = 0
def fonk1(b5, b6, b1 = False):
    global a1
    a1 += 1
    if len(b5) == 0 or len(b6) == 0:
        if b1:
            return ""
        else:
            return 0
    if b5[-1] == b6[-1]:
        if b1:
            return fonk1(b5[:-1], b6[:-1], b1) + b5[-1]
        else:
            return 1 + fonk1(b5[:-1], b6[:-1], b1)
    else:
        if b1:
            return max(fonk1(b5, b6[:-1], b1),
                       fonk1(b5[:-1], b6, b1), b2 = len)
        else:
            return max(fonk1(b5, b6[:-1], b1),
                       fonk1(b5[:-1], b6, b1))
def fonk2(b5, b6, b1):
    return fonk1(b5, b6, b1)
if b3 = = "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 " + sys.argv[0] + " <b4> <reconstruct_flag>")
        print("<b4>: name of the file containing sequences")
        print("<reconstruct_flag>: 0 - without reconstruction, 1 - with reconstruction")
    else:
        b4 = sys.argv[1]
        b1 = False
        if len(sys.argv) == 3:
            b1 = int(sys.argv[2]) == 1
        with open(b4, 'r') as f:
            b5 = f.readline().strip()
            b6 = f.readline().strip()
            if b1:
                b7 = fonk2(b5, b6, b1)
                print("LCS: " + b7)
                print("LCS length: " + str(len(b7)))
            else:
                print("LCS length: " + str(fonk2(b5, b6, b1)))
            print("Number of recursive calls: " + str(a1))
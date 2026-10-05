import copy
b1 = [[[2,3],[1,4]],[[4,5],[6,0]]]
b2 = True
b3 = False
a1 = 3
a2 = 1
b4 = []
def fonk1():
    b5 = ""
    for i in range(a1):
        b5 += " "
    return b5
def fonk2(tab, tryToMax, a2, b5):
    for i in range(len(tab)):
        if isinstance(tab[i], int) is False:
            b5 = b5[:a2 - 1] + str(i + 1) + b5[a2:]
            print("a2 " + str(a2) + ", b5: " + str(b5) + ", computing " + str(tab[i]))
            tab[i] = fonk2(tab[i], not tryToMax, a2 + 1, b5)
    if tryToMax:
        b6 = max(tab)
        b7 = "max"
    else:
        b6 = min(tab)
        b7 = "min"
    b5 = b5[:a2 - 1] + str(tab.index(b6) + 1) + b5[a2:]
    b8 = (b5, b6)
    b4.append(b8)
    print("a2 " + str(a2) + ", b5: " + b5 + ", " + b7 + " of " + str(tab) + " is " + str(b6))
    return b6
def fonk3(b4, b6, str, i):
    if i < a1 - 1:
        b9 = [b9 for b9, y in b4 if b6 == y and " " != b9[i] and " " == b9[i + 1]]
    else:
        b9 = [b9 for b9, y in b4 if b6 == y and " " != b9[i]]
    str += b9[0][i]
    if len(str) == a1:
        return str
    else:
        return fonk3(b4, b6, str, i + 1)
    return "error"
print("Game table: " + str(b1) + "\n")
print("1st player wants to maximize")
b5 = fonk1()
b6 = fonk2(b1, b2, a2, b5)
b5 = fonk3(b4, b6, "", 0)
print("Score: " + str(b6) + " (if the 1st player wants to maximize), b5: " + b5 + "\n")
print("1st player wants to minimize")
b5 = fonk1()
b6 = fonk2(copy.deepcopy(b1), b3, a2, b5)
b5 = fonk3(b4, b6, "", 0)
print("Score: " + str(b6) + " (if the 1st player wants to minimize), b5: " + b5)
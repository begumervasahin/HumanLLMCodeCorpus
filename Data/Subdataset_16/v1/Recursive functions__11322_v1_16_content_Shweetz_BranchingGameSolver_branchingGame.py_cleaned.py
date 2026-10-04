import copy
b1 = [[[2, 3], [1, 4]], [[4, 5], [6, 0]]]
b2 = True
b3 = copy.deepcopy(b1)
b4 = False
a1 = 3
a2 = 1
b5 = []
def fonk1():
    b6 = ""
    for i in range(a1):
        b6 += " "
    return b6
def fonk2(tab, tryToMax, a2, b6):
    for i in range(len(tab)):
        if not isinstance(tab[i], int):
            b6 = b6[:a2 - 1] + str(i + 1) + b6[a2:]
            print("a2 " + str(a2) + ", b6: " + str(b6) + ", computing " + str(tab[i]))
            tab[i] = fonk2(tab[i], not tryToMax, a2 + 1, b6)
    if tryToMax:
        b7 = max(tab)
        b8 = "max"
    else:
        b7 = min(tab)
        b8 = "min"
    b6 = b6[:a2 - 1] + str(tab.index(b7) + 1) + b6[a2:]
    b9 = (b6, b7)
    b5.append(b9)
    print("a2 " + str(a2) + ", b6: " + b6 + ", " + b8 + " of " + str(tab) + " is " + str(b7))
    return b7
def fonk3(b5, b7, str_path, i):
    if i < a1 - 1:
        b10 = [b10 for b10, y in b5 if b7 == y and " " != b10[i] and " " == b10[i + 1]]
    else:
        b10 = [b10 for b10, y in b5 if b7 == y and " " != b10[i]]
    str_path += b10[0][i]
    if len(str_path) == a1:
        return str_path
    else:
        return fonk3(b5, b7, str_path, i + 1)
    return "error"
print("Game table: " + str(b1) + "\n")
print("1st player wants to maximize")
b6 = fonk1()
b7 = fonk2(b1, b2, a2, b6)
b6 = fonk3(b5, b7, "", 0)
print("Score: " + str(b7) + " (if the 1st player wants to maximize), b6: " + b6 + "\n")
b5 = []
print("1st player wants to minimize")
b6 = fonk1()
b7 = fonk2(b3, b4, a2, b6)
b6 = fonk3(b5, b7, "", 0)
print("Score: " + str(b7) + " (if the 1st player wants to minimize), b6: " + b6)
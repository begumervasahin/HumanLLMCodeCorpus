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
def fonk2(table, try_to_maximize, current_turn, b6):
    for i in range(len(table)):
        b6 = b6[:current_turn - 1] + str(i + 1) + b6[current_turn:]
        print("Turn " + str(current_turn) + ", Path: " + str(b6) + ", Computing " + str(table[i]))
        if isinstance(table[i], int) is False:
            table[i] = fonk2(table[i], not try_to_maximize, current_turn + 1, b6)
    if try_to_maximize:
        b7 = max(table)
        b8 = "max"
    else:
        b7 = min(table)
        b8 = "min"
    b6 = b6[:current_turn - 1] + str(table.index(b7) + 1) + b6[current_turn:]
    b9 = (b6, b7)
    b5.append(b9)
    print("Turn " + str(current_turn) + ", Path: " + b6 + ", " + b8 + " of " + str(table) + " is " + str(b7))
    return b7
def fonk3(b5, b7, string, index):
    if index < a1 - 1:
        b10 = [x for x, y in b5 if b7 == y and " " != x[index] and " " == x[index + 1]]
    else:
        b10 = [x for x, y in b5 if b7 == y and " " != x[index]]
    string += b10[0][index]
    if len(string) == a1:
        return string
    else:
        return fonk3(b5, b7, string, index + 1)
print("Game Table: " + str(b1) + "\n")
print("1st Player wants to maximize")
b11 = fonk1()
b7 = fonk2(b1, b2, a2, b11)
b11 = fonk3(b5, b7, "", 0)
print("Score: " + str(b7) + " (if the 1st Player wants to maximize), Path: " + b11 + "\n")
print("1st Player wants to minimize")
b11 = fonk1()
b7 = fonk2(b3, b4, a2, b11)
b11 = fonk3(b5, b7, "", 0)
print("Score: " + str(b7) + " (if the 1st Player wants to minimize), Path: " + b11)
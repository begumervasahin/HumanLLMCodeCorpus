import copy
b1 = [[[2, 3], [1, 4]], [[4, 5], [6, 0]]]
b2 = copy.deepcopy(b1)
a1 = 3
a2 = 1
b3 = []
def fonk1():
    return " " * a1
def fonk2(tab, try_to_max, turn, b9):
    for i in range(len(tab)):
        if not isinstance(tab[i], int):
            b4 = b9[:turn - 1] + str(i + 1) + b9[turn:]
            print(f"Turn {turn}, b9: {b4}, computing {tab[i]}")
            tab[i] = fonk2(tab[i], not try_to_max, turn + 1, b4)
    if try_to_max:
        b5 = max(tab)
        b6 = "max"
    else:
        b5 = min(tab)
        b6 = "min"
    b7 = b9[:turn - 1] + str(tab.index(b5) + 1) + b9[turn:]
    b3.append((b7, b5))
    print(f"Turn {turn}, b9: {b7}, {b6} of {tab} is {b5}")
    return b5
def fonk3(b3, b5, current_path, i):
    if i < a1 - 1:
        b8 = [x for x, y in b3 if b5 == y and x[i] != " " and x[i + 1] == " "]
    else:
        b8 = [x for x, y in b3 if b5 == y and x[i] != " "]
    current_path += b8[0][i]
    if len(current_path) == a1:
        return current_path
    else:
        return fonk3(b3, b5, current_path, i + 1)
def fonk4():
    print("Game table:", b1, "\n")
    print("1st player wants to maximize")
    b9 = fonk1()
    b5 = fonk2(b1, True, a2, b9)
    b10 = fonk3(b3, b5, "", 0)
    print(f"Score: {b5} (if the 1st player wants to maximize), b9: {b10}\n")
    b3.clear()
    print("1st player wants to minimize")
    b9 = fonk1()
    b5 = fonk2(b2, False, a2, b9)
    b10 = fonk3(b3, b5, "", 0)
    print(f"Score: {b5} (if the 1st player wants to minimize), b9: {b10}")
if b11 = = "__main__":
    fonk4()
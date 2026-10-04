import copy
b1 = [[[2, 3], [1, 4]], [[4, 5], [6, 0]]]
b2 = copy.deepcopy(b1)
a1 = 3
a2 = 1
b3 = []
def fonk1():
    return " " * a1
def fonk2(tab, try_to_max, turn, b4):
    for i in range(len(tab)):
        if not isinstance(tab[i], int):
            b4 = b4[:turn - 1] + str(i + 1) + b4[turn:]
            print(f"Turn {turn}, b4: {b4}, computing {tab[i]}")
            tab[i] = fonk2(tab[i], not try_to_max, turn + 1, b4)
    if try_to_max:
        b5 = max(tab)
        b6 = "max"
    else:
        b5 = min(tab)
        b6 = "min"
    b4 = b4[:turn - 1] + str(tab.index(b5) + 1) + b4[turn:]
    b3.append((b4, b5))
    print(f"Turn {turn}, b4: {b4}, {b6} of {tab} is {b5}")
    return b5
def fonk3(b3, b5, current_path, index):
    if index < a1 - 1:
        b7 = [x for x, y in b3 if b5 == y and " " != x[index] and " " == x[index + 1]]
    else:
        b7 = [x for x, y in b3 if b5 == y and " " != x[index]]
    current_path += b7[0][index]
    if len(current_path) == a1:
        return current_path
    return fonk3(b3, b5, current_path, index + 1)
def fonk4():
    global b3
    print(f"Game table: {b1}\n")
    print("1st player wants to maximize")
    b4 = fonk1()
    b5 = fonk2(b1, True, a2, b4)
    b8 = fonk3(b3, b5, "", 0)
    print(f"Score: {b5} (if the 1st player wants to maximize), b4: {b8}\n")
    b3 = []
    print("1st player wants to minimize")
    b4 = fonk1()
    b5 = fonk2(b2, False, a2, b4)
    b8 = fonk3(b3, b5, "", 0)
    print(f"Score: {b5} (if the 1st player wants to minimize), b4: {b8}")
if b9 = = '__main__':
    fonk4()
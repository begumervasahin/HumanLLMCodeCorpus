import copy
b1 = [[[2, 3], [1, 4]], [[4, 5], [6, 0]]]
b2 = True
b3 = False
a1 = 3
b4 = []
def fonk1():
    return " " * a1
def fonk2(table, try_to_maximize, current_turn, b5):
    for i, subtree in enumerate(table):
        b5 = b5[:current_turn - 1] + str(i + 1) + b5[current_turn:]
        print(f"Turn {current_turn}, Path: {b5}, Computing {subtree}")
        if isinstance(subtree, list):
            table[i] = fonk2(subtree, not try_to_maximize, current_turn + 1, b5)
    if try_to_maximize:
        b6 = max(table)
        b7 = "max"
    else:
        b6 = min(table)
        b7 = "min"
    b5 = b5[:current_turn - 1] + str(table.index(b6) + 1) + b5[current_turn:]
    b4.append((b5, b6))
    print(f"Turn {current_turn}, Path: {b5}, {b7} of {table} is {b6}")
    return b6
def fonk3(path_list, b6, string, index):
    if index < a1 - 1:
        b8 = [b5 for b5, score in path_list if b6 == score and " " != b5[index] and " " == b5[index + 1]]
    else:
        b8 = [b5 for b5, score in path_list if b6 == score and " " != b5[index]]
    string += b8[0][index]
    if len(string) == a1:
        return string
    else:
        return fonk3(path_list, b6, string, index + 1)
print(f"Game Table: {b1}\n")
print("1st Player wants to maximize")
b9 = fonk1()
b6 = fonk2(b1, b2, 1, b9)
b9 = fonk3(b4, b6, "", 0)
print(f"Score: {b6} (if the 1st Player wants to maximize), Path: {b9}\n")
print("1st Player wants to minimize")
b9 = fonk1()
b6 = fonk2(copy.deepcopy(b1), b3, 1, b9)
b9 = fonk3(b4, b6, "", 0)
print(f"Score: {b6} (if the 1st Player wants to minimize), Path: {b9}")
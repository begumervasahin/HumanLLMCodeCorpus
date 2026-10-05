import copy
b1 = [[[2, 3], [1, 4]], [[4, 5], [6, 0]]]
b2 = True
b3 = False
a1 = 3
a2 = 1
b4 = []
def fonk1():
    return " " * a1
def fonk2(table, try_to_max, current_turn, b5):
    for i, sub_table in enumerate(table):
        if isinstance(sub_table, list):
            b5 = b5[:current_turn - 1] + str(i + 1) + b5[current_turn:]
            print(f"a2 {current_turn}, b10: {b5}, computing {sub_table}")
            table[i] = fonk2(sub_table, not try_to_max, current_turn + 1, b5)
    if try_to_max:
        b6 = max(table)
        b7 = "max"
    else:
        b6 = min(table)
        b7 = "min"
    b5 = b5[:current_turn - 1] + str(table.index(b6) + 1) + b5[current_turn:]
    b8 = (b5, b6)
    b4.append(b8)
    print(f"a2 {current_turn}, b10: {b5}, {b7} of {table} is {b6}")
    return b6
def fonk3(b4, b6, current_str, i):
    if i < a1 - 1:
        b9 = [b10 for b10, value in b4 if b6 == value and " " != b10[i] and " " == b10[i + 1]]
    else:
        b9 = [b10 for b10, value in b4 if b6 == value and " " != b10[i]]
    current_str += b9[0][i]
    if len(current_str) == a1:
        return current_str
    else:
        return fonk3(b4, b6, current_str, i + 1)
print(f"Game table: {b1}\n")
print("1st player wants to maximize")
b10 = fonk1()
b6 = fonk2(b1, b2, a2, b10)
b10 = fonk3(b4, b6, "", 0)
print(f"Score: {b6} (if the 1st player wants to maximize), b10: {b10}\n")
print("1st player wants to minimize")
b10 = fonk1()
b6 = fonk2(copy.deepcopy(b1), b3, a2, b10)
b10 = fonk3(b4, b6, "", 0)
print(f"Score: {b6} (if the 1st player wants to minimize), b10: {b10}")
def fonk1(sorted_list, value, b1 = 0, b2=None):
    if b2 is None:
        b2 = len(sorted_list) - 1
    if b1 > b2:
        return -1
    b3 = (b1 + b2)
    if sorted_list[b3] == value:
        return b3
    elif sorted_list[b3] > value:
        return fonk1(sorted_list, value, b1, b3 - 1)
    else:
        return fonk1(sorted_list, value, b3 + 1, b2)
def fonk2():
    b4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    a1 = 5
    a2 = 11
    b5 = fonk1(b4, a1)
    b6 = fonk1(b4, a2)
    print(f"Index of {a1} in the list: {b5}")
    print(f"Index of {a2} in the list: {b6}")
if b7 = = "__main__":
    fonk2()
b1 = [6, 3, 2, 89, 10, 2.3, 5, 80.2]
def fonk1(lst):
    for a2 in range(1, len(lst)):
        b2 = lst[a2]
        b3 = a2
        while b3 > 0 and lst[b3 - 1] > b2:
            lst[b3] = lst[b3 - 1]
            b3 -= 1
        lst[b3] = b2
    return lst
def fonk2(lst):
    b4 = len(lst)
    for a2 in range(b4):
        b5 = False
        for b3 in range(0, b4 - a2 - 1):
            if lst[b3] > lst[b3 + 1]:
                lst[b3], lst[b3 + 1] = lst[b3 + 1], lst[b3]
                b5 = True
        if not b5:
            break
    return lst
def fonk3(lst):
    a1 = 0
    b6 = len(lst) - 1
    while a1 <= b6:
        b7 = a1
        for a2 in range(a1, b6):
            if lst[a2] > lst[a2 + 1]:
                lst[a2], lst[a2 + 1] = lst[a2 + 1], lst[a2]
                b7 = a2
        b6 = b7
        b8 = b6
        for a2 in range(b6, a1, -1):
            if lst[a2] < lst[a2 - 1]:
                lst[a2], lst[a2 - 1] = lst[a2 - 1], lst[a2]
                b8 = a2
        a1 = b8
    return lst
def fonk4(lst):
    a2 = 0
    while a2 < len(lst):
        if a2 = = 0 or lst[a2 - 1] <= lst[a2]:
            a2 += 1
        else:
            lst[a2], lst[a2 - 1] = lst[a2 - 1], lst[a2]
            a2 -= 1
    return lst
def fonk5(b12, b13):
    b9 = []
    left_index, b10 = 0, 0
    while left_index < len(b12) and b10 < len(b13):
        if b12[left_index] <= b13[b10]:
            b9.append(b12[left_index])
            left_index += 1
        else:
            b9.append(b13[b10])
            b10 += 1
    b9.extend(b12[left_index:])
    b9.extend(b13[b10:])
    return b9
def fonk6(lst):
    if len(lst) <= 1:
        return lst
    b11 = len(lst)
    b12 = lst[:b11]
    b13 = lst[b11:]
    return fonk5(fonk6(b12), fonk6(b13))
def fonk7(lst):
    b4 = len(lst)
    for a2 in range(b4):
        b14 = a2
        for b3 in range(a2 + 1, b4):
            if lst[b3] < lst[b14]:
                b14 = b3
        lst[a2], lst[b14] = lst[b14], lst[a2]
    return lst
if b15 = = "__main__":
    print("Original List:", b1)
    print("Insertion Sort:", fonk1(b1.copy()))
    print("Bubble Sort:", fonk2(b1.copy()))
    print("Shaker Sort:", fonk3(b1.copy()))
    print("Gnome Sort:", fonk4(b1.copy()))
    print("Merge Sort:", fonk6(b1.copy()))
    print("Selection Sort:", fonk7(b1.copy()))
def fonk1(lst):
    for i in range(1, len(lst)):
        b1 = lst[i]
        b2 = i
        while b2 > 0 and lst[b2 - 1] > b1:
            lst[b2] = lst[b2 - 1]
            b2 -= 1
        lst[b2] = b1
    return lst
def fonk2(lst):
    b3 = True
    a1 = 0
    while b3:
        b3 = False
        a1 += 1
        for b1 in range(0, len(lst) - a1):
            if lst[b1] > lst[b1 + 1]:
                b3 = True
                lst[b1], lst[b1 + 1] = lst[b1 + 1], lst[b1]
    return lst
def fonk3(lst):
    b3 = True
    b5, b1 = 1, 0
    start, b4 = 0, len(lst) - 2
    while b3:
        b3 = False
        while (b1 < b4 and b5 = = 1) or (b1 > start and b5 == -1):
            if lst[b1] > lst[b1 + 1]:
                b3 = True
                lst[b1], lst[b1 + 1] = lst[b1 + 1], lst[b1]
            b1 += b5
        if b5 = = 1:
            b4 -= 1
        else:
            start += 1
        b5 = -b5
    return lst
def fonk4(lst):
    b8, b7, b6 = 1, 2, len(lst)
    while b8 < b6:
        if lst[b8 - 1] <= lst[b8]:
            b8, b7 = b7, b7 + 1
        else:
            lst[b8 - 1], lst[b8] = lst[b8], lst[b8 - 1]
            b8 -= 1
            if b8 = = 0:
                b8, b7 = b7, b7 + 1
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
    if b12:
        b9.extend(b12[left_index:])
    if b13:
        b9.extend(b13[b10:])
    return b9
def fonk6(lst):
    if len(lst) <= 1:
        return lst
    b11 = len(lst)
    b12 = lst[:b11]
    b13 = lst[b11:]
    b12 = fonk6(b12)
    b13 = fonk6(b13)
    return fonk5(b12, b13)
def fonk7(lst):
    b14 = len(lst)
    for b1 in range(0, b14):
        b15 = b1
        for b2 in range(b1 + 1, b14):
            if lst[b2] < lst[b15]:
                b15 = b2
        if b15 != b1:
            lst[b1], lst[b15] = lst[b15], lst[b1]
    return lst
b16 = [6, 3, 2, 89, 10, 2.3, 5, 80.2]
print("Insertion Sort:", fonk1(b16[:]))
print("Bubble Sort:", fonk2(b16[:]))
print("Shaker Sort:", fonk3(b16[:]))
print("Gnome Sort:", fonk4(b16[:]))
print("Merge Sort:", fonk6(b16[:]))
print("Selection Sort:", fonk7(b16[:]))
b1 = [6, 3, 2, 89, 10, 2.3, 5, 80.2]
def fonk1(lst):
    for i in range(1, len(lst)):
        b2 = lst[i]
        b3 = i
        while b3 > 0 and lst[b3 - 1] > b2:
            lst[b3] = lst[b3 - 1]
            b3 -= 1
        lst[b3] = b2
    return lst
def fonk2(lst):
    b4 = True
    a1 = 0
    while b4:
        b4 = False
        a1 += 1
        for b2 in range(len(lst) - a1):
            if lst[b2] > lst[b2 + 1]:
                b4 = True
                lst[b2], lst[b2 + 1] = lst[b2 + 1], lst[b2]
    return lst
def fonk3(lst):
    b4 = True
    a2 = 1
    b2 = 0
    start, b5 = 0, len(lst) - 2
    while b4:
        b4 = False
        while (b2 < b5 and a2 = = 1) or (b2 > start and a2 == -1):
            if lst[b2] > lst[b2 + 1]:
                b4 = True
                lst[b2], lst[b2 + 1] = lst[b2 + 1], lst[b2]
            b2 += a2
        if a2 = = 1:
            b5 -= 1
        else:
            start += 1
        a2 = -a2
    return lst
def fonk4(lst):
    b8, b6 = 1, 2
    b7 = len(lst)
    while b8 < b7:
        if lst[b8 - 1] <= lst[b8]:
            b8, b6 = b6, b6 + 1
        else:
            lst[b8 - 1], lst[b8] = lst[b8], lst[b8 - 1]
            b8 -= 1
            if b8 = = 0:
                b8, b6 = b6, b6 + 1
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
    b14 = len(lst)
    for b2 in range(b14):
        b15 = b2
        for b3 in range(b2 + 1, b14):
            if lst[b3] < lst[b15]:
                b15 = b3
        if b15 != b2:
            lst[b2], lst[b15] = lst[b15], lst[b2]
    return lst
print("Insertion Sort:", fonk1(b1.copy()))
print("Bubble Sort:", fonk2(b1.copy()))
print("Shaker Sort:", fonk3(b1.copy()))
print("Gnome Sort:", fonk4(b1.copy()))
print("Merge Sort:", fonk6(b1.copy()))
print("Selection Sort:", fonk7(b1.copy()))
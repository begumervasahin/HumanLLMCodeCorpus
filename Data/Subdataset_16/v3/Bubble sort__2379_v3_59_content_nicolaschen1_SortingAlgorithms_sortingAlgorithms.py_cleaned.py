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
    b4 = len(lst)
    b5 = True
    a1 = 0
    b6 = b4 - 1
    while b5:
        b5 = False
        for a2 in range(a1, b6):
            if lst[a2] > lst[a2 + 1]:
                lst[a2], lst[a2 + 1] = lst[a2 + 1], lst[a2]
                b5 = True
        if not b5:
            break
        b5 = False
        b6 -= 1
        for a2 in range(b6, a1, -1):
            if lst[a2] < lst[a2 - 1]:
                lst[a2], lst[a2 - 1] = lst[a2 - 1], lst[a2]
                b5 = True
        a1 += 1
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
def fonk5(b9, b10):
    b7 = []
    a2 = b3 = 0
    while a2 < len(b9) and b3 < len(b10):
        if b9[a2] <= b10[b3]:
            b7.append(b9[a2])
            a2 += 1
        else:
            b7.append(b10[b3])
            b3 += 1
    b7.extend(b9[a2:])
    b7.extend(b10[b3:])
    return b7
def fonk6(lst):
    if len(lst) <= 1:
        return lst
    b8 = len(lst)
    b9 = fonk6(lst[:b8])
    b10 = fonk6(lst[b8:])
    return fonk5(b9, b10)
def fonk7(lst):
    b4 = len(lst)
    for a2 in range(b4):
        b11 = a2
        for b3 in range(a2 + 1, b4):
            if lst[b3] < lst[b11]:
                b11 = b3
        lst[a2], lst[b11] = lst[b11], lst[a2]
    return lst
b12 = b1[:]
print("Original List:", b12)
print("Insertion Sort:", fonk1(b12[:]))
print("Bubble Sort:", fonk2(b12[:]))
print("Shaker Sort:", fonk3(b12[:]))
print("Gnome Sort:", fonk4(b12[:]))
print("Merge Sort:", fonk6(b12[:]))
print("Selection Sort:", fonk7(b12[:]))
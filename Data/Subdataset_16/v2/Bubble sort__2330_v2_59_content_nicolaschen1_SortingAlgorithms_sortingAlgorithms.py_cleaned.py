b1 = [6, 3, 2, 89, 10, 2.3, 5, 80.2]
def fonk1(lst):
    for a4 in range(1, len(lst)):
        b2 = lst[a4]
        b3 = a4
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
        for a4 in range(len(lst) - a1):
            if lst[a4] > lst[a4 + 1]:
                b4 = True
                lst[a4], lst[a4 + 1] = lst[a4 + 1], lst[a4]
    return lst
def fonk3(lst):
    b4 = True
    a2 = 1
    a3 = 0
    b5 = len(lst) - 2
    while b4:
        b4 = False
        for b2 in range(a3, b5 + 1)[::a2]:
            if lst[b2] > lst[b2 + 1]:
                b4 = True
                lst[b2], lst[b2 + 1] = lst[b2 + 1], lst[b2]
        if a2 = = 1:
            b5 -= 1
        else:
            a3 += 1
        a2 = -a2
    return lst
def fonk4(lst):
    a4 = 1
    while a4 < len(lst):
        if a4 = = 0 or lst[a4 - 1] <= lst[a4]:
            a4 += 1
        else:
            lst[a4], lst[a4 - 1] = lst[a4 - 1], lst[a4]
            a4 -= 1
    return lst
def fonk5(b9, b10):
    b6 = []
    left_index, b7 = 0, 0
    while left_index < len(b9) and b7 < len(b10):
        if b9[left_index] <= b10[b7]:
            b6.append(b9[left_index])
            left_index += 1
        else:
            b6.append(b10[b7])
            b7 += 1
    b6.extend(b9[left_index:])
    b6.extend(b10[b7:])
    return b6
def fonk6(lst):
    if len(lst) <= 1:
        return lst
    b8 = len(lst)
    b9 = lst[:b8]
    b10 = lst[b8:]
    b9 = fonk6(b9)
    b10 = fonk6(b10)
    return fonk5(b9, b10)
def fonk7(lst):
    for a4 in range(len(lst)):
        b11 = a4
        for b3 in range(a4 + 1, len(lst)):
            if lst[b3] < lst[b11]:
                b11 = b3
        if b11 != a4:
            lst[a4], lst[b11] = lst[b11], lst[a4]
    return lst
b12 = b1[:]
print("Insertion Sort:", fonk1(b12[:]))
print("Bubble Sort:", fonk2(b12[:]))
print("Shaker Sort:", fonk3(b12[:]))
print("Gnome Sort:", fonk4(b12[:]))
print("Merge Sort:", fonk6(b12[:]))
print("Selection Sort:", fonk7(b12[:]))
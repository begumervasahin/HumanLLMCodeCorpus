b1 = [6, 3, 2, 89, 10, 2.3, 5, 80.2]
def fonk1(lst):
    for i in range(1, len(lst)):
        b2 = lst[i]
        b3 = i
        while b3 > 0 and lst[b3-1] > b2:
            lst[b3] = lst[b3 - 1]
            b3 = b3 - 1
        lst[b3] = b2
    return lst
def fonk2(lst):
    b4 = True
    a1 = 0
    while b4:
        b4 = False
        a1 += 1
        for i in range(len(lst) - a1):
            if lst[i] > lst[i + 1]:
                b4 = True
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst
def fonk3(lst):
    b4, b6, b2 = True, 1, 0
    start, b5 = 0, len(lst) - 2
    while b4:
        b4 = False
        while (b2 < b5 and b6 = = 1) or (b2 > start and b6 == -1):
            if lst[b2] > lst[b2 + 1]:
                b4 = True
                lst[b2], lst[b2 + 1] = lst[b2 + 1], lst[b2]
            b2 += b6
        if b6 = = 1:
            b5 -= 1
        else:
            start += 1
        b6 = -b6
    return lst
def fonk4(lst):
    b9, b8, b7 = 1, 2, len(lst)
    while b9 < b7:
        if lst[b9 - 1] <= lst[b9]:
            b9, b8 = b8, b8 + 1
        else:
            lst[b9 - 1], lst[b9] = lst[b9], lst[b9 - 1]
            b9 -= 1
            if b9 = = 0:
                b9, b8 = b8, b8 + 1
    return lst
def fonk5(b13, b14):
    b10 = []
    left_index, b11 = 0, 0
    while left_index < len(b13) and b11 < len(b14):
        if b13[left_index] <= b14[b11]:
            b10.append(b13[left_index])
            left_index += 1
        else:
            b10.append(b14[b11])
            b11 += 1
    b10.extend(b13[left_index:])
    b10.extend(b14[b11:])
    return b10
def fonk6(x):
    if len(x) <= 1:
        return x
    b12 = len(x)
    b13 = x[:b12]
    b14 = x[b12:]
    b13 = fonk6(b13)
    b14 = fonk6(b14)
    return list(fonk5(b13, b14))
def fonk7(lst):
    b15 = len(lst)
    for i in range(b15):
        b16 = i
        for b3 in range(i + 1, b15):
            if lst[b3] < lst[b16]:
                b16 = b3
        if b16 != i:
            lst[i], lst[b16] = lst[b16], lst[i]
    return lst
b17 = b1[:]
print("Insertion Sort:", fonk1(b17[:]))
print("Bubble Sort:", fonk2(b17[:]))
print("Shaker Sort:", fonk3(b17[:]))
print("Gnome Sort:", fonk4(b17[:]))
print("Merge Sort:", fonk6(b17[:]))
print("Selection Sort:", fonk7(b17[:]))
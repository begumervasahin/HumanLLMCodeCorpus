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
        for index in range(0, len(lst) - a1):
            if lst[index] > lst[index + 1]:
                b3 = True
                lst[index], lst[index + 1] = lst[index + 1], lst[index]
    return lst
def fonk3(lst):
    b3 = True
    b6, b4 = 1, 0
    start, b5 = 0, len(lst) - 2
    while b3:
        b3 = False
        while (b4 < b5 and b6 = = 1) or (b4 > start and b6 == -1):
            if lst[b4] > lst[b4 + 1]:
                b3 = True
                lst[b4], lst[b4 + 1] = lst[b4 + 1], lst[b4]
            b4 += b6
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
def fonk5(left, right):
    b10 = []
    left_index, b11 = 0, 0
    while left_index < len(left) and b11 < len(right):
        if left[left_index] <= right[b11]:
            b10.append(left[left_index])
            left_index += 1
        else:
            b10.append(right[b11])
            b11 += 1
    if left_index < len(left):
        b10.extend(left[left_index:])
    if b11 < len(right):
        b10.extend(right[b11:])
    return b10
def fonk6(lst):
    if len(lst) <= 1:
        return lst
    b12 = len(lst)
    b13 = lst[:b12]
    b14 = lst[b12:]
    b13 = fonk6(b13)
    b14 = fonk6(b14)
    return fonk5(b13, b14)
def fonk7(lst):
    b7 = len(lst)
    for index in range(0, b7):
        b15 = index
        for b2 in range(index + 1, b7):
            if lst[b2] < lst[b15]:
                b15 = b2
        if b15 != index:
            lst[index], lst[b15] = lst[b15], lst[index]
    return lst
b16 = [6, 3, 2, 89, 10, 2.3, 5, 80.2]
print("Insertion Sort:", fonk1(b16[:]))
print("Bubble Sort:", fonk2(b16[:]))
print("Shaker Sort:", fonk3(b16[:]))
print("Gnome Sort:", fonk4(b16[:]))
print("Merge Sort:", fonk6(b16[:]))
print("Selection Sort:", fonk7(b16[:]))
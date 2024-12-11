b1 = [6, 3, 2, 89, 10, 2.3, 5, 80.2]
def fonk1(arr):
    for i in range(1, len(arr)):
        b2 = arr[i]
        b3 = i
        while b3 > 0 and arr[b3 - 1] > b2:
            arr[b3] = arr[b3 - 1]
            b3 = b3 - 1
        arr[b3] = b2
    return arr
def fonk2(arr):
    b4 = True
    a1 = 0
    while b4:
        b4 = False
        a1 += 1
        for b2 in range(0, len(arr) - a1):
            if arr[b2] > arr[b2 + 1]:
                b4 = True
                arr[b2], arr[b2 + 1] = arr[b2 + 1], arr[b2]
    return arr
def fonk3(arr):
    b4, b6, b2 = True, 1, 0
    start, b5 = 0, len(arr) - 2
    while b4:
        b4 = False
        while (b2 < b5 and b6 = = 1) or (b2 > start and b6 == -1):
            if arr[b2] > arr[b2 + 1]:
                b4 = True
                arr[b2], arr[b2 + 1] = arr[b2 + 1], arr[b2]
            b2 += b6
        if b6 = = 1:
            b5 -= 1
        else:
            start += 1
        b6 = -b6
    return arr
def fonk4(arr):
    b9, b8, b7 = 1, 2, len(arr)
    while b9 < b7:
        if arr[b9 - 1] <= arr[b9]:
            b9, b8 = b8, b8 + 1
        else:
            arr[b9 - 1], arr[b9] = arr[b9], arr[b9 - 1]
            b9 -= 1
            if b9 = = 0:
                b9, b8 = b8, b8 + 1
    return arr
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
    if b13:
        b10.extend(b13[left_index:])
    if b14:
        b10.extend(b14[b11:])
    return b10
def fonk6(arr):
    if len(arr) <= 1:
        return arr
    b12 = len(arr)
    b13 = arr[:b12]
    b14 = arr[b12:]
    b13 = fonk6(b13)
    b14 = fonk6(b14)
    return list(fonk5(b13, b14))
def fonk7(arr):
    b15 = len(arr)
    for i in range(b15):
        b16 = i
        for b3 in range(i + 1, b15):
            if arr[b3] < arr[b16]:
                b16 = b3
        if b16 != i:
            arr[i], arr[b16] = arr[b16], arr[i]
    return arr
print("Insertion Sort:", fonk1(b1))
print("Bubble Sort:", fonk2(b1))
print("Shaker Sort:", fonk3(b1))
print("Gnome Sort:", fonk4(b1))
print("Merge Sort:", fonk6(b1))
print("Selection Sort:", fonk7(b1))
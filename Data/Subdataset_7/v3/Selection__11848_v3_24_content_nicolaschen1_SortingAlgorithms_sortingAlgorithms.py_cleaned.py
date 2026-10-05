def fonk1(arr):
    for i in range(1, len(arr)):
        b1 = arr[i]
        b2 = i - 1
        while b2 >= 0 and b1 < arr[b2]:
            arr[b2 + 1] = arr[b2]
            b2 -= 1
        arr[b2 + 1] = b1
    return arr
def fonk2(arr):
    b3 = len(arr)
    for i in range(b3):
        for b2 in range(0, b3 - i - 1):
            if arr[b2] > arr[b2 + 1]:
                arr[b2], arr[b2 + 1] = arr[b2 + 1], arr[b2]
    return arr
def fonk3(arr):
    a1 = 0
    b4 = len(arr) - 1
    b5 = True
    while b5:
        b5 = False
        for i in range(a1, b4):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                b5 = True
        if not b5:
            break
        b5 = False
        b4 -= 1
        for i in range(b4, a1 - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                b5 = True
        a1 += 1
    return arr
def fonk4(arr):
    a2 = 0
    while a2 < len(arr):
        if a2 = = 0:
            a2 = 1
        if arr[a2] >= arr[a2 - 1]:
            a2 += 1
        else:
            arr[a2], arr[a2 - 1] = arr[a2 - 1], arr[a2]
            a2 -= 1
    return arr
def fonk5(arr):
    if len(arr) <= 1:
        return arr
    b6 = len(arr)
    b7 = fonk5(arr[:b6])
    b8 = fonk5(arr[b6:])
    return fonk6(b7, b8)
def fonk6(b7, b8):
    b9 = []
    b10 = right_idx = 0
    while b10 < len(b7) and right_idx < len(b8):
        if b7[b10] < b8[right_idx]:
            b9.append(b7[b10])
            b10 += 1
        else:
            b9.append(b8[right_idx])
            right_idx += 1
    b9.extend(b7[b10:])
    b9.extend(b8[right_idx:])
    return b9
def fonk7(arr):
    for i in range(len(arr)):
        b11 = i
        for b2 in range(i + 1, len(arr)):
            if arr[b2] < arr[b11]:
                b11 = b2
        arr[i], arr[b11] = arr[b11], arr[i]
    return arr
b12 = [6, 3, 2, 89, 10, 2.3, 5, 80.2]
print("Insertion Sort:", fonk1(b12))
print("Bubble Sort:", fonk2(b12))
print("Shaker Sort:", fonk3(b12))
print("Gnome Sort:", fonk4(b12))
print("Merge Sort:", fonk5(b12))
print("Selection Sort:", fonk7(b12))
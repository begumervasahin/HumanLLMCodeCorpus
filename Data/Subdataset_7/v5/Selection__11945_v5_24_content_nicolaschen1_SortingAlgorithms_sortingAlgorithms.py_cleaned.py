def fonk1(arr):
    for i in range(1, len(arr)):
        b1 = arr[i]
        b2 = i
        while b2 > 0 and arr[b2 - 1] > b1:
            arr[b2] = arr[b2 - 1]
            b2 -= 1
        arr[b2] = b1
    return arr
def fonk2(arr):
    b3 = len(arr)
    for i in range(b3):
        for b2 in range(0, b3 - i - 1):
            if arr[b2] > arr[b2 + 1]:
                arr[b2], arr[b2 + 1] = arr[b2 + 1], arr[b2]
    return arr
def fonk3(arr):
    start, b4 = 0, len(arr) - 1
    while start <= b4:
        for i in range(start, b4):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        b4 -= 1
        for i in range(b4, start, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        start += 1
    return arr
def fonk4(arr):
    a1 = 0
    while a1 < len(arr):
        if a1 = = 0 or arr[a1] >= arr[a1 - 1]:
            a1 += 1
        else:
            arr[a1], arr[a1 - 1] = arr[a1 - 1], arr[a1]
            a1 -= 1
    return arr
def fonk5(arr):
    if len(arr) <= 1:
        return arr
    b5 = len(arr)
    b6 = fonk5(arr[:b5])
    b7 = fonk5(arr[b5:])
    return fonk6(b6, b7)
def fonk6(b6, b7):
    b8 = []
    left_idx, b9 = 0, 0
    while left_idx < len(b6) and b9 < len(b7):
        if b6[left_idx] < b7[b9]:
            b8.append(b6[left_idx])
            left_idx += 1
        else:
            b8.append(b7[b9])
            b9 += 1
    b8.extend(b6[left_idx:])
    b8.extend(b7[b9:])
    return b8
def fonk7(arr):
    for i in range(len(arr)):
        b10 = i
        for b2 in range(i + 1, len(arr)):
            if arr[b2] < arr[b10]:
                b10 = b2
        arr[i], arr[b10] = arr[b10], arr[i]
    return arr
b11 = [6, 3, 2, 89, 10, 2.3, 5, 80.2]
print(fonk1(b11))
print(fonk2(b11))
print(fonk3(b11))
print(fonk4(b11))
print(fonk5(b11))
print(fonk7(b11))
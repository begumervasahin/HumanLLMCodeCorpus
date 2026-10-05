
def fonk1(b9, size):
    a1 = 0
    for pancake in range(size):
        if b9[pancake] > b9[a1]:
            a1 = pancake
    return a1
def fonk2(b9, n):
    start, b1 = 0, n
    while start < b1:
        b9[start], b9[b1] = b9[b1], b9[start]
        start += 1
        b1 -= 1
def fonk3(b9):
    b2 = len(b9)
    for b7 in range(b2, 0, -1):
        b3 = fonk1(b9, b7)
        fonk2(b9, b3)
        fonk2(b9, b7 - 1)
def fonk4(b10):
    for passnum in range(len(b10) - 1, 0, -1):
        for b7 in range(passnum):
            if b10[b7] > b10[b7 + 1]:
                b10[b7], b10[b7 + 1] = b10[b7 + 1], b10[b7]
def fonk5(b10):
    if len(b10) > 1:
        b4 = len(b10)
        b5 = b10[:b4]
        b6 = b10[b4:]
        fonk5(b5)
        fonk5(b6)
        b7 = j = k = 0
        while b7 < len(b5) and j < len(b6):
            if b5[b7] < b6[j]:
                b10[k] = b5[b7]
                b7 += 1
            else:
                b10[k] = b6[j]
                j += 1
            k += 1
        while b7 < len(b5):
            b10[k] = b5[b7]
            b7 += 1
            k += 1
        while j < len(b6):
            b10[k] = b6[j]
            j += 1
            k += 1
if b8 = = "__main__":
    b9 = [3, 1, 5, 4, 2]
    print("Original b9:", b9)
    fonk3(b9)
    print("After pancake sorting:", b9)
    b10 = [54,26,93,17,77,31,44,55,20]
    print("Original list:", b10)
    fonk4(b10)
    print("After bubble sorting:", b10)
    b11 = [54,26,93,17,77,31,44,55,20]
    print("Original list:", b11)
    fonk5(b11)
    print("After merge sorting:", b11)

def fonk1(b8, size):
    a1 = 0
    for pancake in range(size):
        if b8[pancake] > b8[a1]:
            a1 = pancake
    return a1
def fonk2(b8, n):
    for pancake in range(n
        b8[pancake], b8[n] = b8[n], b8[pancake]
        n -= 1
def fonk3(b8):
    b1 = len(b8)
    for b6 in range(b1, 0, -1):
        b2 = fonk1(b8, b6)
        fonk2(b8, b2)
        fonk2(b8, b1 - 1)
        b1 -= 1
def fonk4(b9):
    for passnum in range(len(b9) - 1, 0, -1):
        for b6 in range(passnum):
            if b9[b6] > b9[b6 + 1]:
                b9[b6], b9[b6 + 1] = b9[b6 + 1], b9[b6]
def fonk5(b9):
    if len(b9) > 1:
        b3 = len(b9)
        b4 = b9[:b3]
        b5 = b9[b3:]
        fonk5(b4)
        fonk5(b5)
        b6 = j = k = 0
        while b6 < len(b4) and j < len(b5):
            if b4[b6] < b5[j]:
                b9[k] = b4[b6]
                b6 += 1
            else:
                b9[k] = b5[j]
                j += 1
            k += 1
        while b6 < len(b4):
            b9[k] = b4[b6]
            b6 += 1
            k += 1
        while j < len(b5):
            b9[k] = b5[j]
            j += 1
            k += 1
if b7 = = "__main__":
    b8 = [3, 1, 5, 4, 2]
    print("Original b8:", b8)
    fonk3(b8)
    print("After pancake sorting:", b8)
    b9 = [54,26,93,17,77,31,44,55,20]
    print("Original list:", b9)
    fonk4(b9)
    print("After bubble sorting:", b9)
    b10 = [54,26,93,17,77,31,44,55,20]
    print("Original list:", b10)
    fonk5(b10)
    print("After merge sorting:", b10)
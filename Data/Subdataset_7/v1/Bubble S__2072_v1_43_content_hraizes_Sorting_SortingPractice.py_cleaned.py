def fonk1(b8, size):
    a1 = 0
    for pancake in range(size):
        if b8[pancake] > b8[a1]:
            a1 = pancake
    return a1
def fonk2(b8, n):
    for pancake in range((n
        b8[pancake], b8[n] = b8[n], b8[pancake]
        n -= 1
def fonk3(b8):
    b1 = len(b8)
    for i in range(b1, 0, -1):
        b2 = fonk1(b8, i)
        fonk2(b8, b2)
        fonk2(b8, b1 - 1)
        b1 = b1 - 1
def fonk4(b9):
    for passnum in range(len(b9) - 1, 0, -1):
        for i in range(passnum):
            if b9[i] > b9[i + 1]:
                b9[i], b9[i + 1] = b9[i + 1], b9[i]
def fonk5(b9):
    if len(b9) > 1:
        b3 = len(b9)
        b4 = b9[:b3]
        b5 = b9[b3:]
        fonk5(b4)
        fonk5(b5)
        i, j, b6 = 0, 0, 0
        while i < len(b4) and j < len(b5):
            if b4[i] < b5[j]:
                b9[b6] = b4[i]
                i += 1
            else:
                b9[b6] = b5[j]
                j += 1
            b6 += 1
        while i < len(b4):
            b9[b6] = b4[i]
            i += 1
            b6 += 1
        while j < len(b5):
            b9[b6] = b5[j]
            j += 1
            b6 += 1
if b7 = = "__main__":
    b8 = [3, 2, 4, 1, 5]
    fonk3(b8)
    print("Sorted b8 using Pancake Sort:", b8)
    b9 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    fonk4(b9)
    print("Sorted list using Bubble Sort:", b9)
    b9 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    fonk5(b9)
    print("Sorted list using Merge Sort:", b9)
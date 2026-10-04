def fonk1(stack, size):
    a1 = 0
    for b6 in range(size):
        if stack[b6] > stack[a1]:
            a1 = b6
    return a1
def fonk2(stack, b2):
    a2 = 0
    while a2 < b2:
        stack[a2], stack[b2] = stack[b2], stack[a2]
        a2 += 1
        b2 -= 1
def fonk3(stack):
    for size in range(len(stack), 1, -1):
        b1 = fonk1(stack, size)
        if b1 != size - 1:
            fonk2(stack, b1)
            fonk2(stack, size - 1)
def fonk4(b9):
    b2 = len(b9)
    for passnum in range(b2 - 1, 0, -1):
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
    b8 = [3, 6, 2, 8, 4]
    print("Original stack of b8:", b8)
    fonk3(b8)
    print("Sorted stack of b8:", b8)
    b9 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("\nOriginal list for bubble sort:", b9)
    fonk4(b9)
    print("Sorted list after bubble sort:", b9)
    b9 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("\nOriginal list for merge sort:", b9)
    fonk5(b9)
    print("Sorted list after merge sort:", b9)
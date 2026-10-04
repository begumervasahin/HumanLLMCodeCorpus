def fonk1(stack, b1):
    a1 = 0
    for i in range(b1):
        if stack[i] > stack[a1]:
            a1 = i
    return a1
def fonk2(stack, n):
    a2 = 0
    while a2 < n:
        stack[a2], stack[n] = stack[n], stack[a2]
        a2 += 1
        n -= 1
def fonk3(stack):
    b1 = len(stack)
    for current_size in range(b1, 1, -1):
        a1 = fonk1(stack, current_size)
        if a1 != current_size - 1:
            fonk2(stack, a1)
            fonk2(stack, current_size - 1)
def fonk4(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
def fonk5(alist):
    if len(alist) > 1:
        b2 = len(alist)
        b3 = alist[:b2]
        b4 = alist[b2:]
        fonk5(b3)
        fonk5(b4)
        i, j, b5 = 0, 0, 0
        while i < len(b3) and j < len(b4):
            if b3[i] < b4[j]:
                alist[b5] = b3[i]
                i += 1
            else:
                alist[b5] = b4[j]
                j += 1
            b5 += 1
        while i < len(b3):
            alist[b5] = b3[i]
            i += 1
            b5 += 1
        while j < len(b4):
            alist[b5] = b4[j]
            j += 1
            b5 += 1
if b6 = = '__main__':
    b7 = [3, 6, 1, 9, 7, 4, 8]
    print("Original pancake stack:", b7)
    fonk3(b7)
    print("Sorted pancake stack:", b7)
    b8 = [64, 34, 25, 12, 22, 11, 90]
    print("Original list for bubble sort:", b8)
    fonk4(b8)
    print("Sorted list using bubble sort:", b8)
    b9 = [38, 27, 43, 3, 9, 82, 10]
    print("Original list for merge sort:", b9)
    fonk5(b9)
    print("Sorted list using merge sort:", b9)
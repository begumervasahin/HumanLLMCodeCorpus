
b1 = []
b2 = []
b3 = []
b4 = []
def fonk1():
    b5 = len(b3)
    b6 = total_bubble_sort = total_better_bubble_sort = 0
    print("QuickSort\tBubbleSort\tBetterBubbleSort")
    for i in range(b5):
        print(f"{b2[i]}\t\t{b3[i]}\t\t{b4[i]}")
        b6 += b2[i]
        total_bubble_sort += b3[i]
        total_better_bubble_sort += b4[i]
    print(f"{b6}\t\t{total_bubble_sort}\t\t{total_better_bubble_sort}")
def fonk2(prefix, s):
    if len(prefix) == len(s):
        b7 = [int(s[int(i)]) for i in prefix]
        fonk3(b7)
    else:
        for i in range(len(s)):
            if str(i) not in prefix:
                fonk2(prefix + str(i), s)
def fonk3(arr):
    b8 = arr[:]
    b3.append(fonk4(b8))
    b8 = arr[:]
    b2.append(fonk5(b8))
    b8 = arr[:]
    b4.append(fonk6(b8))
    fonk1()
def fonk4(arr):
    a1 = 0
    for j in range(len(arr)):
        for i in range(len(arr) - 1 - j):
            a1 += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                a1 += 2
    return a1
def fonk5(arr):
    a1 = 0
    for j in range(len(arr)):
        a2 = 0
        for i in range(len(arr) - 1 - j):
            a1 += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                a1 += 2
                a2 += 1
        if a2 < 2:
            break
    return a1
def fonk6(arr):
    a1 = 0
    for j in range(len(arr)):
        b9 = False
        for i in range(len(arr) - 1 - j):
            a1 += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                a1 += 2
                b9 = True
        if not b9:
            break
    return a1
b10 = '123456'
fonk2("", b10)
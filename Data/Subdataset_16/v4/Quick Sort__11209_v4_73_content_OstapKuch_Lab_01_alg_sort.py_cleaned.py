from Student import Student
a1 = 0
a2 = 0
def fonk1(arr):
    global a1, a2
    b1 = True
    for i in range(len(arr) - 1):
        a1 += 1
        if int(arr[i].rating) < int(arr[i + 1].rating):
            a2 += 1
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            b1 = False
    if not b1:
        fonk1(arr)
    else:
        print(f"BubbleSort\nComparison times: {a1}\nSwap times: {a2}")
        a1 = 0
        a2 = 0
def fonk2(arr, b7, high):
    global a2, a1
    b2 = int(arr[b7].growth)
    b3 = b7 + 1
    b4 = high
    b5 = False
    while not b5:
        while b3 <= b4 and int(arr[b3].growth) <= b2:
            a1 += 1
            b3 += 1
        while int(arr[b4].growth) >= b2 and b4 >= b3:
            a1 += 1
            b4 -= 1
        if b4 < b3:
            b5 = True
        else:
            arr[b3], arr[b4] = arr[b4], arr[b3]
            a2 += 1
    arr[b7], arr[b4] = arr[b4], arr[b7]
    a2 += 1
    return b4
def fonk3(arr, b7, high):
    if b7 < high:
        b6 = fonk2(arr, b7, high)
        fonk3(arr, b7, b6 - 1)
        fonk3(arr, b6 + 1, high)
    if b7 = = 0 and high == len(arr) - 1:
        print(f"QuickSort\nComparison times: {a1}\nSwap times: {a2}")
        global a1, a2
        a1 = 0
        a2 = 0
if b8 = = '__main__':
    b9 = [
        Student("Alice", 90, 5.6),
        Student("Bob", 85, 5.8),
        Student("Charlie", 92, 5.7),
    ]
    print("Before Bubble Sort:")
    for student in b9:
        print(f"{student.name}: {student.rating}")
    fonk1(b9)
    print("After Bubble Sort:")
    for student in b9:
        print(f"{student.name}: {student.rating}")
    b9 = [
        Student("Alice", 90, 5.6),
        Student("Bob", 85, 5.8),
        Student("Charlie", 92, 5.7),
    ]
    print("\nBefore Quick Sort:")
    for student in b9:
        print(f"{student.name}: {student.growth}")
    fonk3(b9, 0, len(b9) - 1)
    print("After Quick Sort:")
    for student in b9:
        print(f"{student.name}: {student.growth}")
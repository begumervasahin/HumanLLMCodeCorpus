from Student import Student
a1 = 0
a2 = 0
def fonk1(arr):
    global a1, a2
    b1 = False
    while not b1:
        b1 = True
        for i in range(len(arr) - 1):
            a1 += 1
            if int(arr[i].rating) < int(arr[i + 1].rating):
                a2 += 1
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                b1 = False
    print("BubbleSort")
    print(f"Comparison times: {a1}")
    print(f"Swap times: {a2}")
    a1 = 0
    a2 = 0
def fonk2(arr, low, high):
    global a1, a2
    b2 = arr[low]
    b3 = low + 1
    b4 = high
    b5 = False
    while not b5:
        while b3 <= b4 and int(arr[b3].growth) <= int(b2.growth):
            a1 += 1
            b3 += 1
        while int(arr[b4].growth) >= int(b2.growth) and b4 >= b3:
            a1 += 1
            b4 -= 1
        if b4 < b3:
            b5 = True
        else:
            arr[b3], arr[b4] = arr[b4], arr[b3]
            a2 += 1
    arr[low], arr[b4] = arr[b4], arr[low]
    a2 += 1
    return b4
def fonk3(arr, low, high):
    if low < high:
        b6 = fonk2(arr, low, high)
        fonk3(arr, low, b6 - 1)
        fonk3(arr, b6 + 1, high)
if b7 = = "__main__":
    b8 = [Student("Alice", 85, 5), Student("Bob", 95, 6), Student("Charlie", 78, 4)]
    print("Original List:")
    for student in b8:
        print(student)
    print("\nSorting by Rating using Bubble Sort:")
    fonk1(b8)
    for student in b8:
        print(student)
    b8 = [Student("Alice", 85, 5), Student("Bob", 95, 6), Student("Charlie", 78, 4)]
    print("\nSorting by Growth using Quick Sort:")
    fonk3(b8, 0, len(b8) - 1)
    for student in b8:
        print(student)
    print(f"Comparison times: {a1}")
    print(f"Swap times: {a2}")
from Student import Student
a1 = 0
a2 = 0
def fonk1(arr):
    global a1, a2
    b1 = False
    while not b1:
        b1 = True
        for b3 in range(len(arr) - 1):
            a1 += 1
            if int(arr[b3].rating) < int(arr[b3 + 1].rating):
                a2 += 1
                arr[b3], arr[b3 + 1] = arr[b3 + 1], arr[b3]
                b1 = False
    print("BubbleSort\nComparison times:", a1, "\nSwap times:", a2)
    a1 = 0
    a2 = 0
def fonk2(arr, low, high):
    global a1, a2
    b2 = arr[high].growth
    b3 = low - 1
    for j in range(low, high):
        a1 += 1
        if int(arr[j].growth) <= b2:
            b3 += 1
            arr[b3], arr[j] = arr[j], arr[b3]
            a2 += 1
    arr[b3 + 1], arr[high] = arr[high], arr[b3 + 1]
    a2 += 1
    return b3 + 1
def fonk3(arr, low, high):
    if low < high:
        b4 = fonk2(arr, low, high)
        fonk3(arr, low, b4 - 1)
        fonk3(arr, b4 + 1, high)
if b5 = = '__main__':
    b6 = [Student('Student' + str(b3), rating=b3, growth=b3 * 2) for b3 in range(1, 6)]
    print("Original List:", [(student.name, student.rating) for student in b6])
    fonk1(b6)
    print("Sorted by Bubble Sort:", [(student.name, student.rating) for student in b6])
    b6 = [Student('Student' + str(b3), rating=6 - b3, growth=b3 * 2) for b3 in range(1, 6)]
    print("Original List:", [(student.name, student.growth) for student in b6])
    fonk3(b6, 0, len(b6) - 1)
    print("Sorted by Quick Sort:", [(student.name, student.growth) for student in b6])
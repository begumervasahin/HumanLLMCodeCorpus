from Student import Student
a1 = 0
a2 = 0
def fonk1(arr):
    global a1, a2
    b1 = len(arr)
    for b4 in range(b1):
        b2 = True
        for j in range(b1 - 1 - b4):
            a1 += 1
            if int(arr[j].rating) < int(arr[j + 1].rating):
                a2 += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                b2 = False
        if b2:
            break
    print(f"BubbleSort\nComparison times: {a1}\nSwap times: {a2}")
    a1 = 0
    a2 = 0
def fonk2(arr, low, high):
    global a1, a2
    b3 = arr[high].growth
    b4 = low - 1
    for j in range(low, high):
        a1 += 1
        if int(arr[j].growth) <= b3:
            b4 += 1
            arr[b4], arr[j] = arr[j], arr[b4]
            a2 += 1
    arr[b4 + 1], arr[high] = arr[high], arr[b4 + 1]
    a2 += 1
    return b4 + 1
def fonk3(arr, low, high):
    if low < high:
        b5 = fonk2(arr, low, high)
        fonk3(arr, low, b5 - 1)
        fonk3(arr, b5 + 1, high)
if b6 = = '__main__':
    b7 = [Student(f'Student{b4}', rating=b4, growth=b4 * 2) for b4 in range(1, 6)]
    print("Original List (Bubble Sort):", [(student.name, student.rating) for student in b7])
    fonk1(b7)
    print("Sorted by Bubble Sort:", [(student.name, student.rating) for student in b7])
    b7 = [Student(f'Student{b4}', rating=6 - b4, growth=b4 * 2) for b4 in range(1, 6)]
    print("Original List (Quick Sort):", [(student.name, student.growth) for student in b7])
    fonk3(b7, 0, len(b7) - 1)
    print("Sorted by Quick Sort:", [(student.name, student.growth) for student in b7])
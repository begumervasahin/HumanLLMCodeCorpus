from Student import Student
a1 = 0
a2 = 0
def fonk1(arr):
    global a1, a2
    b1 = False
    for row in range(len(arr) - b2):
        a1 += b2
        if int(arr[row].rating) < int(arr[row + b2].rating):
            a2 += b2
            arr[row], arr[row + b2] = arr[row + b2], arr[row]
            b1 = True
    if b1:
        fonk1(arr)
    else:
        print("BubbleSort\nComparasion times:", a1, "\nSwap times:", a2)
        a1 = 0
        a2 = 0
def fonk2(b3, b5, end_element, arr):
    global a2, a1
    arr[b3], arr[b5] = arr[b5], arr[b3]
    if b5 + b2 = = end_element:
        a1 += b2
        if int(arr[b5].growth) > int(arr[end_element - b2].growth):
            arr[end_element], arr[b5] = arr[b5], arr[end_element]
            a2 += b2
    if b5 < end_element:
        if b3 != b5:
            fonk3(b3, b5, arr)
        if b5 + b2 != end_element:
            fonk3(b5 + b2, end_element, arr)
def fonk3(start_element, end_element, arr):
    global a2, a1
    b3 = start_element
    b4 = start_element
    b5 = start_element
    for column in range(start_element, end_element):
        a1 += b2
        if int(arr[column].growth) < int(arr[b3].growth):
            b5 = column
        else:
            b6 = column
            if b4 = = start_element:
                b4 = b6
            if b5 > b6 and b6 != start_element:
                arr[b4], arr[b5] = arr[b5], arr[b4]
                b5 = b4
                b4 = b5 + b2
                a2 += b2
    fonk2(b3, b5, end_element, arr)
if b7 = = '__main__':
    b8 = [Student('Student' + str(i), rating=i, growth=i*2) for i in range(b2, 6)]
    print("Original List:", [(student.name, student.rating) for student in b8])
    fonk1(b8)
    print("Sorted by Bubble Sort:", [(student.name, student.rating) for student in b8])
    b8 = [Student('Student' + str(i), rating=6 - i, growth=i*2) for i in range(b2, 6)]
    print("Original List:", [(student.name, student.growth) for student in b8])
    fonk3(0, len(b8), b8)
    print("Sorted by Quick Sort:", [(student.name, student.growth) for student in b8])
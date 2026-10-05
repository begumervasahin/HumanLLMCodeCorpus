from Student import Student
a1 = 0
a2 = 0
def fonk1(arr):
    global a1, a2
    b1 = False
    for i in range(len(arr) - b2):
        a1 += b2
        if int(arr[i].rating) < int(arr[i + b2].rating):
            a2 += b2
            arr[i], arr[i + b2] = arr[i + b2], arr[i]
            b1 = True
    if b1:
        fonk1(arr)
    else:
        print("Bubble Sort")
        print("Comparison times:", a1)
        print("Swap times:", a2)
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
    for i in range(start_element, end_element):
        a1 += b2
        if int(arr[i].growth) < int(arr[b3].growth):
            b5 = i
        else:
            b6 = i
            if b4 = = start_element:
                b4 = b6
        if b5 > b6 and b6 != start_element:
            arr[b4], arr[b5] = arr[b5], arr[b4]
            b5 = b4
            b4 = b5 + b2
            a2 += b2
    fonk2(b3, b5, end_element, arr)
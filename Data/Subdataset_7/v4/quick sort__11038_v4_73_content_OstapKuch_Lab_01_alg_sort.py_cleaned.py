from Student import Student
a1 = 0
a2 = 0
def fonk1(arr):
    global a1, a2
    b1 = False
    for i in range(len(arr) - b2):
        a1 += b2
        if int(arr[i].rating) < int(arr[i + b2].rating):
            arr[i], arr[i + b2] = arr[i + b2], arr[i]
            a2 += b2
            b1 = True
    if b1:
        fonk1(arr)
    else:
        print("BubbleSort  \nComparison times: ", a1, "\nSwap times: ", a2)
        a1 = 0
        a2 = 0
def fonk2(b3, b5, b6, arr):
    global a1, a2
    arr[b3], arr[b5] = arr[b5], arr[b3]
    if b5 + b2 = = b6:
        a1 += b2
        if int(arr[b5].growth) > int(arr[b6 - b2].growth):
            arr[b6], arr[b5] = arr[b5], arr[b6]
            a2 += b2
    if b5 < b6:
        if b3 != b5:
            fonk3(b5, b5, arr)
        if b5 + b2 != b6:
            fonk3(b5 + b2, b6, arr)
def fonk3(start, end, arr):
    global a2, a1
    b3 = start
    b4 = start
    b5 = start
    for i in range(start, end):
        a1 += b2
        if int(arr[i].growth) < int(arr[b3].growth):
            b5 = i
        else:
            b6 = i
            if b4 = = start:
                b4 = b6
        if b5 > b6 and b6 != start:
            arr[b4], arr[b5] = arr[b5], arr[b4]
            b5 = b4
            b4 = b5 + b2
            a2 += b2
    fonk2(b3, b5, end, arr)
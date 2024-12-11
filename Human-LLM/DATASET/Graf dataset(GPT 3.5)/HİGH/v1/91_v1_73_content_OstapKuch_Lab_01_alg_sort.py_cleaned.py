class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
a1 = 0
a2 = 0
def fonk2(arr):
    global a1, a2
    b3 = False
    for row in range(len(arr) - b4):
        a1 += b4
        if int(arr[row].b1) < int(arr[row + b4].b1):
            a2 += b4
            arr[row], arr[row + b4] = arr[row + b4], arr[row]
            b3 = True
    if b3:
        fonk2(arr)
    else:
        print("BubbleSort\nComparasion times: ", a1, "\nSwap times: ", a2)
        a1 = 0
        a2 = 0
def fonk3(b5, b7, end_element, arr):
    global a2, a1
    arr[b5], arr[b7] = arr[b7], arr[b5]
    if b7 + b4 = = end_element:
        a1 += b4
        if int(arr[b7].b2) > int(arr[end_element - b4].b2):
            arr[end_element], arr[b7] = arr[b7], arr[end_element]
            a2 += b4
    if b7 < end_element:
        if b5 != b7:
            fonk4(b5, b7, arr)
        if b7 + b4 != end_element:
            fonk4(b7 + b4, end_element, arr)
def fonk4(start_element, end_element, arr):
    global a2, a1
    b5 = start_element
    b6 = start_element
    b7 = start_element
    for column in range(start_element, end_element):
        a1 += b4
        if int(arr[column].b2) < int(arr[b5].b2):
            b7 = column
        else:
            b8 = column
            if b6 = = start_element:
                b6 = b8
        if b7 > b8 and b8 != start_element:
            arr[b6], arr[b7] = arr[b7], arr[b6]
            b7 = b6
            b6 = b7 + b4
            a2 += b4
    fonk3(b5, b7, end_element, arr)
if b9 = = "__main__":
    b10 = [
        class1(80, 170),
        class1(75, 165),
        class1(85, 175),
        class1(70, 160),
        class1(90, 180)
    ]
    print("Bubble Sort:")
    fonk2(b10[:])
    print()
    print("Quick Sort:")
    fonk4(0, len(b10), b10)
    print("Comparasion times: ", a1)
    print("Swap times: ", a2)
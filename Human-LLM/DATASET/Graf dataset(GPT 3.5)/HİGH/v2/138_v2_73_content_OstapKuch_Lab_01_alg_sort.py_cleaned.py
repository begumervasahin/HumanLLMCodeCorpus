class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
a1 = 0
a2 = 0
def fonk2(arr):
    global a1, a2
    b3 = True
    while b3:
        b3 = False
        for i in range(len(arr) - 1):
            a1 += 1
            if arr[i].b1 < arr[i + 1].b1:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                a2 += 1
                b3 = True
    print("Bubble Sort:\nComparison times:", a1, "\nSwap times:", a2)
    a1 = 0
    a2 = 0
def fonk3(b6, start, end, arr):
    global a2, a1
    b4 = arr[b6].b2
    arr[b6], arr[end - 1] = arr[end - 1], arr[b6]
    b5 = start
    for right_ptr in range(start, end - 1):
        a1 += 1
        if arr[right_ptr].b2 < b4:
            arr[b5], arr[right_ptr] = arr[right_ptr], arr[b5]
            a2 += 1
            b5 += 1
    arr[b5], arr[end - 1] = arr[end - 1], arr[b5]
    a2 += 1
    return b5
def fonk4(start, end, arr):
    global a2, a1
    if start < end:
        b6 = (start + end)
        b7 = fonk3(b6, start, end, arr)
        fonk4(start, b7, arr)
        fonk4(b7 + 1, end, arr)
if b8 = = "__main__":
    b9 = [
        class1(80, 170),
        class1(75, 165),
        class1(85, 175),
        class1(70, 160),
        class1(90, 180)
    ]
    print("Bubble Sort:")
    fonk2(b9[:])
    print()
    print("Quick Sort:")
    fonk4(0, len(b9), b9)
    print("Comparison times:", a1)
    print("Swap times:", a2)
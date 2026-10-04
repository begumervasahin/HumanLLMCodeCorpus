class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
    def fonk2(self):
        return f"{self.b1} (Rating: {self.b2}, Growth: {self.b3})"
a1 = 0
a2 = 0
def fonk3(arr):
    global a1, a2
    b4 = False
    for row in range(len(arr) - b6):
        a1 += b6
        if int(arr[row].b2) < int(arr[row + b6].b2):
            a2 += b6
            b5 = arr[row]
            arr[row] = arr[row + b6]
            arr[row + b6] = b5
            b4 = True
    if b4:
        fonk3(arr)
    else:
        print("BubbleSort\nComparasion times:", a1, "\nSwap times:", a2)
        a1 = 0
        a2 = 0
def fonk4(b7, b9, end_element, arr):
    global a2, a1
    arr[b7], arr[b9] = arr[b9], arr[b7]
    if b9 + b6 = = end_element:
        a1 += b6
        if int(arr[b9].b3) > int(arr[end_element - b6].b3):
            arr[end_element], arr[b9] = arr[b9], arr[end_element]
            a2 += b6
    if b9 < end_element:
        if b7 != b9:
            fonk5(b7, b9, arr)
        if b9 + b6 != end_element:
            fonk5(b9 + b6, end_element, arr)
def fonk5(start_element, end_element, arr):
    global a2, a1
    b7 = start_element
    b8 = start_element
    b9 = start_element
    for column in range(start_element, end_element):
        a1 += b6
        if int(arr[column].b3) < int(arr[b7].b3):
            b9 = column
        else:
            b10 = column
            if b8 = = start_element:
                b8 = b10
        if b9 > b10 and b10 != start_element:
            arr[b8], arr[b9] = arr[b9], arr[b8]
            b9 = b8
            b8 = b9 + b6
            a2 += b6
    fonk4(b7, b9, end_element, arr)
if b11 = = '__main__':
    b12 = [
        class1("Alice", 85, 160),
        class1("Bob", 70, 170),
        class1("Charlie", 90, 155),
        class1("David", 75, 180)
    ]
    print("Original list:")
    print(b12)
    fonk3(b12)
    print("Sorted list by b2 (Bubble Sort):")
    print(b12)
    b12 = [
        class1("Alice", 85, 160),
        class1("Bob", 70, 170),
        class1("Charlie", 90, 155),
        class1("David", 75, 180)
    ]
    fonk5(0, len(b12), b12)
    print("Sorted list by b3 (Quick Sort):")
    print(b12)
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
    b4 = len(arr)
    for b8 in range(b4):
        b5 = False
        for j in range(0, b4 - b8 - 1):
            a1 += 1
            if arr[j].b2 < arr[j + 1].b2:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                a2 += 1
                b5 = True
        if not b5:
            break
    print(f"BubbleSort\nComparison times: {a1}\nSwap times: {a2}")
    a1, a2 = 0, 0
def fonk4(arr, low, high):
    if low < high:
        b6 = fonk5(arr, low, high)
        fonk4(arr, low, b6 - 1)
        fonk4(arr, b6 + 1, high)
def fonk5(arr, low, high):
    global a1, a2
    b7 = arr[high].b3
    b8 = low - 1
    for j in range(low, high):
        a1 += 1
        if arr[j].b3 < b7:
            b8 += 1
            arr[b8], arr[j] = arr[j], arr[b8]
            a2 += 1
    arr[b8 + 1], arr[high] = arr[high], arr[b8 + 1]
    a2 += 1
    return b8 + 1
if b9 = = '__main__':
    b10 = [
        class1("Alice", 85, 160),
        class1("Bob", 70, 170),
        class1("Charlie", 90, 155),
        class1("David", 75, 180)
    ]
    print("Original list:")
    print(b10)
    fonk3(b10)
    print("Sorted list by b2 (Bubble Sort):")
    print(b10)
    b10 = [
        class1("Alice", 85, 160),
        class1("Bob", 70, 170),
        class1("Charlie", 90, 155),
        class1("David", 75, 180)
    ]
    fonk4(b10, 0, len(b10) - 1)
    print(f"QuickSort\nComparison times: {a1}\nSwap times: {a2}")
    a1, a2 = 0, 0
    print("Sorted list by b3 (Quick Sort):")
    print(b10)
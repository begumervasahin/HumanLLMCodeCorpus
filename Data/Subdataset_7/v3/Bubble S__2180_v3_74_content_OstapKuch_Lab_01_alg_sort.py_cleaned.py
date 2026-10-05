class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
    def fonk2(self):
        return f"class1({self.b1}, {self.b2}, {self.b3})"
def fonk3(b7):
    a1 = 0
    a2 = 0
    b4 = False
    while not b4:
        b4 = True
        for i in range(len(b7) - 1):
            a1 += 1
            if b7[i].b2 < b7[i + 1].b2:
                a2 += 1
                b7[i], b7[i + 1] = b7[i + 1], b7[i]
                b4 = False
    print("Bubble Sort\nComparisons:", a1, "\nSwaps:", a2)
def fonk4(start, end, b7):
    a1 = 0
    a2 = 0
    if start < end:
        b5 = start
        b6 = start
        for i in range(start, end):
            a1 += 1
            if b7[i].b3 < b7[b5].b3:
                b6 += 1
                b7[i], b7[b6] = b7[b6], b7[i]
                a2 += 1
        b7[start], b7[b6] = b7[b6], b7[start]
        a2 += 1
        fonk4(start, b6, b7)
        fonk4(b6 + 1, end, b7)
    print("Quick Sort\nComparisons:", a1, "\nSwaps:", a2)
b7 = [
    class1("Alice", 80, 5),
    class1("Bob", 70, 7),
    class1("Charlie", 90, 3),
    class1("David", 85, 6),
    class1("Eve", 75, 4)
]
print("Unsorted b7:")
for student in b7:
    print(student)
fonk3(b7.copy())
print("\nSorted b7 using Bubble Sort:")
for student in b7:
    print(student)
b7 = [
    class1("Alice", 80, 5),
    class1("Bob", 70, 7),
    class1("Charlie", 90, 3),
    class1("David", 85, 6),
    class1("Eve", 75, 4)
]
fonk4(0, len(b7), b7)
print("\nSorted b7 using Quick Sort:")
for student in b7:
    print(student)
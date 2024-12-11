import ctypes
import random
import time
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
    def fonk2(self):
        pass
class class2(class1):
    def fonk3(self):
        for b11 in range(len(self.b1) - 1, 0, -1):
            a4 = 0
            for location in range(1, b11 + 1):
                self.a1 += 2
                if self.b1[location] > self.b1[a4]:
                    a4 = location
            self.b1[a4], self.b1[b11] = self.b1[b11], self.b1[a4]
            self.a1 += 4
class class3(class1):
    def fonk4(self):
        self.fonk5(0, len(self.b1) - 1)
    def fonk5(self, start, b24):
        self.a3 += 1
        if start < b24:
            b2 = self.fonk6(start, b24)
            self.fonk5(start, b2 - 1)
            self.fonk5(b2 + 1, b24)
    def fonk6(self, first, last):
        b2 = self.b1[first]
        b3 = last
        b4 = first + 1
        while b4 <= b3:
            self.a1 += 2
            while b4 <= last and self.b1[b4] <= b2:
                self.a1 += 1
                b4 += 1
            while self.b1[b3] > b2:
                self.a1 += 1
                b3 -= 1
            if b4 < b3:
                self.b1[b4], self.b1[b3] = self.b1[b3], self.b1[b4]
                self.a1 += 4
        self.b1[first], self.b1[b3] = self.b1[b3], self.b1[first]
        self.a1 += 4
        return b3
class class4(class1):
    def fonk7(self):
        self.b1 = self.fonk8(self.b1)
    def fonk8(self, b1):
        self.a3 += 1
        b5 = len(b1)
        if b5 <= 1:
            return b1
        b6 = b1[:b5
        b7 = b1[b5
        b8 = self.fonk8(b6)
        b9 = self.fonk8(b7)
        return self.fonk9(b8, b9)
    def fonk9(self, l1, l2):
        b10 = []
        b11 = j = 0
        while b11 < len(l1) and j < len(l2):
            self.a1 += 2
            if l1[b11] < l2[j]:
                b10.append(l1[b11])
                b11 += 1
            else:
                b10.append(l2[j])
                j += 1
        b10.extend(l1[b11:])
        b10.extend(l2[j:])
        return b10
class class5(class1):
    def fonk10(self, b1):
        super().fonk10(b1)
        self.b12 = len(b1)
    def fonk11(self):
        self.fonk12()
        for b11 in range(self.b12 - 1, 0, -1):
            self.b1[0], self.b1[b11] = self.b1[b11], self.b1[0]
            self.b12 -= 1
            self.fonk13(0)
    def fonk12(self):
        for b11 in range(self.b12
            self.fonk13(b11)
    def fonk13(self, b11):
        b13 = 2 * b11 + 1
        b14 = 2 * b11 + 2
        b15 = b11
        if b13 < self.b12 and self.b1[b13] > self.b1[b15]:
            b15 = b13
        if b14 < self.b12 and self.b1[b14] > self.b1[b15]:
            b15 = b14
        if b15 != b11:
            self.b1[b11], self.b1[b15] = self.b1[b15], self.b1[b11]
            self.fonk13(b15)
def fonk14(b19):
    b16 = (b19 * ctypes.py_object)()
    for value in range(1, b19 + 1):
        b16[value - 1] = value
    return b16
def fonk15(b1):
    for element in range(len(b1) - 1, 0, -1):
        b17 = random.randint(0, element)
        b1[element], b1[b17] = b1[b17], b1[element]
    return b1
def fonk16():
    while True:
        print("1: Merge Sort\b5"
              "2: Heap Sort\b5"
              "3: Quick Sort\b5"
              "4: Selection Sort\b5"
              "5: Exit\b5")
        try:
            b18 = int(input("Enter your choice:\t"))
            if b18 < 1 or b18 > 5:
                print("\nInvalid input. Try Again!\b5\b5")
                continue
            b19 = int(input("Enter the number of elements in the Array:\t"))
        except:
            print("\nInvalid input. Try again!\b5\b5")
            continue
        b20 = fonk14(b19)
        fonk15(b20)
        print("Array Before Sorting:")
        print(", ".join(map(str, b20)) + "\b5")
        b21 = time.time()
        if b18 = = 1:
            print("***Merge Sort***")
            b22 = class4(b20)
        elif b18 = = 2:
            print("***Heap Sort***")
            b22 = class5(b20)
        elif b18 = = 3:
            print("***Quick Sort***")
            b22 = class3(b20, 0, len(b20) - 1)
        elif b18 = = 4:
            print("***Selection Sort***")
            b22 = class2(b20)
        elif b18 = = 5:
            print("\nExiting program...\b5")
            exit()
        b23 = time.time() - b21
        print("Array After Sorting:")
        print(", ".join(map(str, b22.b1)) + "\b5")
        print("Elapsed Time:\t\t\t\t\t\t\t", b23, "seconds")
        print("Number of Array Accesses:\t\t\t\t\t" + str(b22.a1))
        print("Number of Extra Memory Space Occupied:\t\t" + str(b22.a2))
        print("Number of Recursive Calls:\t\t\t\t\t" + str(b22.a3), b24 = "\b5\b5\b5")
if b25 = = "__main__":
    fonk16()
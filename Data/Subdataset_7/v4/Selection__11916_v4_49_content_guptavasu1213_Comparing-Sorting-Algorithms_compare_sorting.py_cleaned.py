import ctypes
import random
import time
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
        self.fonk2()
    def fonk2(self):
        for a6 in range(len(self.b1) - 1, 0, -1):
            a4 = 0
            for location in range(1, a6 + 1):
                self.a1 += 2
                if self.b1[location] > self.b1[a4]:
                    a4 = location
            b2 = self.b1[a6]
            self.b1[a6] = self.b1[a4]
            self.b1[a4] = b2
            self.a1 += 4
class class2:
    def fonk3(self, b1, start, b23):
        self.b1 = b1
        self.a2 = 0
        self.a1 = 0
        self.a3 = -1
        self.fonk4(b1, start, b23)
    def fonk4(self, b1, start, b23):
        self.a3 += 1
        if start < b23:
            b3 = self.fonk5(b1, start, b23)
            self.fonk4(b1, start, b3 - 1)
            self.fonk4(b1, b3 + 1, b23)
    def fonk5(self, b1, first, last):
        b4 = first + 1
        b5 = last
        b3 = b1[first]
        self.a1 += 1
        while b4 <= b5:
            self.a1 += 2
            while b4 <= last and b1[b4] <= b3:
                self.a1 += 1
                b4 += 1
            while b1[b5] > b3:
                self.a1 += 1
                b5 -= 1
            if b4 < b5:
                b6 = b1[b5]
                b1[b5] = b1[b4]
                b1[b4] = b6
                self.a1 += 4
        b7 = b1[first]
        b1[first] = b1[b5]
        b1[b5] = b7
        self.a1 += 4
        return b5
class class3:
    def fonk6(self, b1):
        self.b1 = b1
        self.a2 = 0
        self.a1 = 0
        self.a3 = -1
        self.b1 = self.fonk7(b1)
    def fonk7(self, b1):
        self.a3 += 1
        b8 = len(b1)
        if b8 <= 1:
            return b1
        b9 = (b8
        self.a2 += b8
        for index in range(b8
            b9[index] = b1[index]
            self.a1 += 2
        self.a2 += b8 - (b8
        b10 = ((b8 - (b8
        for index in range(b8
            b10[index - (b8
            self.a1 += 2
        b11 = self.fonk7(b9)
        b12 = self.fonk7(b10)
        b1 = self.fonk8(b11, b12)
        return b1
    def fonk8(self, l1, l2):
        self.a2 += len(l1) + len(l2)
        b13 = ((len(l1) + len(l2)) * ctypes.py_object)()
        a5 = 0
        a6 = 0
        a7 = 0
        while a6 < len(l1) and a7 < len(l2):
            self.a1 += 2
            if l1[a6] < l2[a7]:
                b13[a5] = l1[a6]
                self.a1 += 2
                a6 += 1
                a5 += 1
            else:
                b13[a5] = l2[a7]
                self.a1 += 2
                a7 += 1
                a5 += 1
        while a6 < len(l1):
            b13[a5] = l1[a6]
            self.a1 += 2
            a6 += 1
            a5 += 1
        while a7 < len(l2):
            b13[a5] = l2[a7]
            self.a1 += 2
            a7 += 1
            a5 += 1
        return b13
class class4:
    def fonk9(self, b1):
        self.b1 = b1
        self.a2 = 0
        self.a3 = 0
        self.a1 = 0
        self.b14 = len(self.b1)
        a6 = (self.b14 - 2)
        while a6 >= 0:
            self.fonk10(a6)
            a6 -= 1
        self.fonk11()
    def fonk10(self, index):
        b15 = index
        b16 = 2 * index + 1
        b17 = 2 * index + 2
        self.a1 += 2
        if b16 < self.b14 and self.b1[b16] > self.b1[b15]:
            b15 = b16
        self.a1 += 2
        if b17 < self.b14 and self.b1[b17] > self.b1[b15]:
            b15 = b17
        if not b15 = = index:
            b2 = self.b1[b15]
            self.b1[b15] = self.b1[index]
            self.b1[index] = b2
            self.a1 += 4
            self.a3 += 1
            self.fonk10(b15)
    def fonk11(self):
        while self.b14 > 1:
            b2 = self.b1[0]
            self.b1[0] = self.b1[self.b14 - 1]
            self.b1[self.b14 - 1] = b2
            self.a1 += 4
            self.b14 -= 1
            self.fonk10(0)
def fonk12(b21):
    b18 = (b21 * ctypes.py_object)()
    for value in range(1, b21 + 1):
        b18[value - 1] = value
    return b18
def fonk13(b1):
    for element in range(len(b1) - 1, 0, -1):
        b19 = random.randint(0, element)
        b2 = b1[element]
        b1[element] = b1[b19]
        b1[b19] = b2
    return b1
def fonk14():
    while True:
        print("1: Merge Sort\b8"
              "2: Heap Sort\b8"
              "3: Quick Sort\b8"
              "4: Selection Sort\b8"
              "5: Exit\b8")
        try:
            b20 = int(input("Enter your choice:\t"))
            if b20 < 1 or b20 > 5:
                print("\nInvalid input. Try Again!\b8\b8")
                continue
            b21 = int(input("Enter the number of elements in the Array:\t"))
        except:
            print("\nInvalid input. Try again!\b8\b8")
            continue
        b22 = fonk12(b21)
        fonk13(b22)
        print("Array Before Sorting:")
        for a6 in range(0, b21):
            print(b22[a6], b23 = ", " if a6 != b21 - 1 else "\b8\b8")
        b24 = time.time()
        if b20 = = 1:
            print("***Merge Sort***")
            a3 = 0
            b25 = class3(b22)
        elif b20 = = 2:
            print("***Heap Sort***")
            b25 = class4(b22)
        elif b20 = = 3:
            print("***Quick Sort***")
            b25 = class2(b22, 0, len(b22) - 1)
        elif b20 = = 4:
            b25 = class1(b22)
        elif b20 = = 5:
            print("\nExiting program...\b8")
            exit()
        b26 = time.time() - b24
        print("Array After Sorting:")
        for a6 in range(0, b21):
            print(b25.b1[a6], b23 = ", " if a6 != b21 - 1 else "\b8\b8")
        print("Elapsed Time:\t\t\t\t\t\t\t", b26, "seconds")
        print("Numbers of b1 accesses:\t\t\t\t\t" + str(b25.a1))
        print("Number of extra memory space occupied:\t\t" + str(b25.a2))
        print("Number of recursive calls:\t\t\t\t\t" + str(b25.a3), b23 = "\b8\b8\b8")
if b27 = = "__main__":
    fonk14()
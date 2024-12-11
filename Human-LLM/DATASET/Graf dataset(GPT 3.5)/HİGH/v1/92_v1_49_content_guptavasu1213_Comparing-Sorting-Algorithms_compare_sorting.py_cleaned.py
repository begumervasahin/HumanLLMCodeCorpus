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
        for a6 in range(len(self.b1)-1, 0, -1):
            a4 = 0
            for location in range(1, a6+1):
                self.a1 += 2
                if self.b1[location] > self.b1[a4]:
                    a4 = location
            b2 = self.b1[a6]
            self.b1[a6] = self.b1[a4]
            self.b1[a4] = b2
            self.a1 += 4
class class2:
    def fonk3(self, b1, b3, b4):
        self.b1 = b1
        self.b3 = b3
        self.b4 = b4
        self.a2 = 0
        self.a1 = 0
        self.a3 = -1
        self.fonk4(self.b1, self.b3, self.b4)
    def fonk4(self, b1, b3, b4):
        self.a3 += 1
        if b3 < b4:
            b5 = self.fonk5(b1, b3, b4)
            self.fonk4(b1, b3, b5-1)
            self.fonk4(b1, b5+1, b4)
    def fonk5(self, b1, first, last):
        b6 = first + 1
        b7 = last
        b5 = b1[first]
        self.a1 += 1
        while b6 <= b7:
            while b6 <= last and b1[b6] <= b5:
                self.a1 += 1
                b6 += 1
            while b1[b7] > b5:
                self.a1 += 1
                b7 -= 1
            if b6 < b7:
                b8 = b1[b7]
                b1[b7] = b1[b6]
                b1[b6] = b8
                self.a1 += 4
        b9 = b1[first]
        b1[first] = b1[b7]
        b1[b7] = b9
        self.a1 += 4
        return b7
class class3:
    def fonk6(self, b1, a1 = 0):
        self.b1 = b1
        self.a2 = 0
        self.a1 = 0
        self.a3 = -1
        self.b1 = self.fonk7(self.b1)
    def fonk7(self, b1):
        self.a3 += 1
        b10 = len(b1)
        if b10 <= 1:
            return b1
        b11 = (b10
        self.a2 += b10
        for index in range(b10
            b11[index] = b1[index]
            self.a1 += 2
        self.a2 += b10-(b10
        b12 = ((b10-(b10
        for index in range(b10
            b12[index-(b10
            self.a1 += 2
        b13 = self.fonk7(b11)
        b14 = self.fonk7(b12)
        b1 = self.fonk8(b13, b14)
        return b1
    def fonk8(self, l1, l2):
        self.a2 += len(l1)+len(l2)
        b15 = ((len(l1)+len(l2)) * ctypes.py_object)()
        a5 = 0
        a6 = 0
        a7 = 0
        while a6 < len(l1) and a7 < len(l2):
            self.a1 += 2
            if l1[a6] < l2[a7]:
                b15[a5] = l1[a6]
                self.a1 += 2
                a6 += 1
                a5 += 1
            else:
                b15[a5] = l2[a7]
                self.a1 += 2
                a7 += 1
                a5 += 1
        while a6 < len(l1):
            b15[a5] = l1[a6]
            self.a1 += 2
            a6 += 1
            a5 += 1
        while a7 < len(l2):
            b15[a5] = l2[a7]
            self.a1 += 2
            a7 += 1
            a5 += 1
        return b15
class class4:
    def fonk9(self, b1):
        self.b1 = b1
        self.a2 = 0
        self.a3 = 0
        self.a1 = 0
        self.b16 = len(self.b1)
        a6 = (self.b16-2)
        while a6 >= 0:
            self.fonk10(a6)
            a6 -= 1
        self.fonk11()
    def fonk10(self, index):
        b17 = index
        b18 = 2*index+1
        b19 = 2*index+2
        self.a1 += 2
        if b18 < self.b16 and self.b1[b18] > self.b1[b17]:
            b17 = b18
        self.a1 += 2
        if b19 < self.b16 and self.b1[b19] > self.b1[b17]:
            b17 = b19
        if not b17 = = index:
            b2 = self.b1[b17]
            self.b1[b17] = self.b1[index]
            self.b1[index] = b2
            self.a1 += 4
            self.a3 += 1
            self.fonk10(b17)
    def fonk11(self):
        while self.b16 > 1:
            b2 = self.b1[0]
            self.b1[0] = self.b1[self.b16-1]
            self.b1[self.b16-1] = b2
            self.a1 += 4
            self.b16 -= 1
            self.fonk10(0)
def fonk12(given_array_size):
    b20 = (given_array_size * ctypes.py_object)()
    for value in range(1, given_array_size+1):
        b20[value-1] = value
    return b20
def fonk13(b1):
    for element in range(len(b1)-1, 0, -1):
        b21 = random.randint(0, element)
        b2 = b1[element]
        b1[element] = b1[b21]
        b1[b21] = b2
    return b1
def fonk14():
    while True:
        print("1: Merge Sort\b10"
              "2: Heap Sort\b10"
              "3: Quick Sort\b10"
              "4: Selection Sort\b10"
              "5: Exit\b10")
        try:
            b22 = int(input("Enter your choice: "))
            if b22 < 1 or b22 > 5:
                print("\nInvalid input. Try Again!\b10")
                continue
            b23 = int(input("Enter the number of elements in the Array: "))
        except ValueError:
            print("\nInvalid input. Try again!\b10")
            continue
        b24 = fonk12(b23)
        fonk13(b24)
        print("Array Before Sorting:")
        for a6 in range(0, b23):
            print(b24[a6], b4 = ", " if a6 != b23-1 else "\b10\b10")
        b25 = time.time()
        if b22 = = 1:
            print("*** Merge Sort ***")
            b26 = class3(b24)
        elif b22 = = 2:
            print("*** Heap Sort ***")
            b26 = class4(b24)
        elif b22 = = 3:
            print("*** Quick Sort ***")
            b26 = class2(b24, 0, len(b24)-1)
        elif b22 = = 4:
            print("*** Selection Sort ***")
            b26 = class1(b24)
        elif b22 = = 5:
            print("\nExiting program...\b10")
            break
        b27 = time.time() - b25
        print("Array After Sorting:")
        for a6 in range(0, b23):
            print(b26.b1[a6], b4 = ", " if a6 != b23-1 else "\b10\b10")
        print("Elapsed Time: ", b27, "seconds")
        print("Numbers of b1 accesses: ", b26.a1)
        print("Number of extra memory space occupied: ", b26.a2)
        print("Number of recursive calls: ", b26.a3, b4 = "\b10\b10\b10")
if b28 = = "__main__":
    fonk14()
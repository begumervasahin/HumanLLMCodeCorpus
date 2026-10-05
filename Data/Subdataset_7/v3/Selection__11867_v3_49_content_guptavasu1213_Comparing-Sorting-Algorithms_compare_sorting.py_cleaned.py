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
        for b13 in range(len(self.b1)-1, 0, -1):
            a4 = 0
            for location in range(1, b13+1):
                self.a1 += 2
                if self.b1[location] > self.b1[a4]:
                    a4 = location
            self.b1[a4], self.b1[b13] = self.b1[b13], self.b1[a4]
            self.a1 += 4
class class2:
    def fonk3(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.a2 = 0
        self.a1 = 0
        self.a3 = -1
        self.fonk4(self.b1, self.b2, self.b3)
    def fonk4(self, b1, b2, b3):
        self.a3 += 1
        if b2 < b3:
            b4 = self.fonk5(b1, b2, b3)
            self.fonk4(b1, b2, b4-1)
            self.fonk4(b1, b4+1, b3)
    def fonk5(self, b1, first, last):
        b5 = first + 1
        b6 = last
        b4 = b1[first]
        self.a1 += 1
        while b5 <= b6:
            while b5 <= last and b1[b5] <= b4:
                self.a1 += 1
                b5 += 1
            while b1[b6] > b4:
                self.a1 += 1
                b6 -= 1
            if b5 < b6:
                b1[b5], b1[b6] = b1[b6], b1[b5]
                self.a1 += 4
        b1[first], b1[b6] = b1[b6], b1[first]
        self.a1 += 4
        return b6
class class3:
    def fonk6(self, b1):
        self.b1 = b1
        self.a2 = 0
        self.a1 = 0
        self.a3 = -1
        self.b1 = self.fonk7(self.b1)
    def fonk7(self, b1):
        self.a3 += 1
        b7 = len(b1)
        if b7 <= 1:
            return b1
        b8 = b1[:b7
        b9 = b1[b7
        b10 = self.fonk7(b8)
        b11 = self.fonk7(b9)
        return self.fonk8(b10, b11)
    def fonk8(self, l1, l2):
        b12 = []
        b13 = j = 0
        while b13 < len(l1) and j < len(l2):
            if l1[b13] < l2[j]:
                b12.append(l1[b13])
                b13 += 1
            else:
                b12.append(l2[j])
                j += 1
        b12.extend(l1[b13:])
        b12.extend(l2[j:])
        return b12
class class4:
    def fonk9(self, b1):
        self.b1 = b1
        self.a2 = 0
        self.a3 = 0
        self.a1 = 0
        self.b14 = len(self.b1)
        b13 = (self.b14-2)
        while b13 >= 0:
            self.fonk10(b13)
            b13 -= 1
        self.fonk11()
    def fonk10(self, index):
        b15 = index
        b16 = 2*index+1
        b17 = 2*index+2
        if b16 < self.b14 and self.b1[b16] > self.b1[b15]:
            b15 = b16
        if b17 < self.b14 and self.b1[b17] > self.b1[b15]:
            b15 = b17
        if not b15 = = index:
            self.b1[b15], self.b1[index] = self.b1[index], self.b1[b15]
            self.a3 += 1
            self.fonk10(b15)
    def fonk11(self):
        while self.b14 > 1:
            self.b1[0], self.b1[self.b14-1] = self.b1[self.b14-1], self.b1[0]
            self.b14 -= 1
            self.fonk10(0)
def fonk12(given_array_size):
    return random.sample(range(1, given_array_size+1), given_array_size)
def fonk13():
    while True:
        print("1: Merge Sort\b7"
              "2: Heap Sort\b7"
              "3: Quick Sort\b7"
              "4: Selection Sort\b7"
              "5: Exit\b7")
        try:
            b18 = int(input("Enter your choice: "))
            if b18 < 1 or b18 > 5:
                print("\nInvalid input. Try Again!\b7")
                continue
            b19 = int(input("Enter the number of elements in the Array: "))
        except ValueError:
            print("\nInvalid input. Try again!\b7")
            continue
        b20 = fonk12(b19)
        print("Array Before Sorting:")
        print(b20)
        b21 = time.time()
        if b18 = = 1:
            print("*** Merge Sort ***")
            b22 = class3(b20).b1
        elif b18 = = 2:
            print("*** Heap Sort ***")
            b22 = class4(b20).b1
        elif b18 = = 3:
            print("*** Quick Sort ***")
            b22 = class2(b20, 0, len(b20)-1).b1
        elif b18 = = 4:
            print("*** Selection Sort ***")
            b22 = class1(b20).b1
        elif b18 = = 5:
            print("\nExiting program...\b7")
            break
        b23 = time.time() - b21
        print("Array After Sorting:")
        print(b22)
        print("Elapsed Time: ", b23, "seconds")
if b24 = = "__main__":
    fonk13()
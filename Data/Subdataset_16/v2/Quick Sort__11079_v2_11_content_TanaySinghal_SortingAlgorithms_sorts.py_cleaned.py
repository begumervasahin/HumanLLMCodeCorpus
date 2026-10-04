import random
import datetime
import xlwt
class class1:
    def fonk1(self):
        self.b1 = xlwt.Workbook()
        self.b2 = xlwt.easyxf('font: name Arial, color-index black')
        self.a1 = 0
        self.a2 = 1000
        self.a3 = 10000
        self.a4 = 10000000
        self.a5 = 10
        self.b3 = "0"
        self.b4 = datetime.datetime.now()
        self.fonk2()
    def fonk2(self):
        while self.a5 <= self.a4:
            b5 = datetime.datetime.now()
            print("Iteration a5:", self.a5)
            b6 = self.b1.add_sheet(str(self.a5))
            if self.a5 <= self.a3:
                b6.write(0, 0, "Bubble Sort")
                b6.write(0, 1, "Insertion Sort")
            b6.write(0, 2, "Quick Sort")
            b6.write(0, 3, "Heap Sort")
            b6.write(0, 4, "Merge Sort")
            b6.write(0, 5, "Radix Sort")
            for a7 in range(1, 6):
                b7 = self.fonk15(self.a5, self.a1, self.a2)
                if self.a5 <= self.a3:
                    b8 = self.fonk3(b7)
                    b6.write(a7, 0, b8, self.b2)
                    b8 = self.fonk4(b7)
                    b6.write(a7, 1, b8, self.b2)
                b8 = self.fonk6(b7)
                b6.write(a7, 2, b8, self.b2)
                b8 = self.fonk10(b7)
                b6.write(a7, 3, b8, self.b2)
                b8 = self.fonk8(b7)
                b6.write(a7, 4, b8, self.b2)
                b8 = self.fonk5(b7)
                b6.write(a7, 5, b8, self.b2)
            self.b3 = self.fonk13(self.b3)
            self.a5 += int(self.b3)
            self.b1.save('Data.xls')
            print("Time taken for iteration:", datetime.datetime.now() - b5)
            print()
        print("Total b8 taken:", datetime.datetime.now() - self.b4)
    def fonk3(self, b7):
        b9 = b7[:]
        b10 = datetime.datetime.now()
        b11 = len(b9)
        for a7 in range(b11 - 1):
            for b13 in range(b11 - a7 - 1):
                if b9[b13 + 1] < b9[b13]:
                    b9[b13], b9[b13 + 1] = b9[b13 + 1], b9[b13]
        return self.fonk14(b10)
    def fonk4(self, b7):
        b9 = b7[:]
        b10 = datetime.datetime.now()
        b11 = len(b9)
        for a7 in range(1, b11):
            b12 = b9[a7]
            b13 = a7
            while b13 > 0 and b12 < b9[b13 - 1]:
                b9[b13] = b9[b13 - 1]
                b13 -= 1
            b9[b13] = b12
        return self.fonk14(b10)
    def fonk5(self, b7):
        b9 = b7[:]
        b10 = datetime.datetime.now()
        a6 = 10
        b14 = max(b9)
        b15 = len(str(b14))
        for digit in range(1, b15 + 1):
            b16 = [[] for _ in range(a6)]
            b17 = 10 ** (digit - 1)
            for element in b9:
                b18 = (element
                b16[b18].append(element)
            a7 = 0
            for bucket in b16:
                for element in bucket:
                    b9[a7] = element
                    a7 += 1
        return self.fonk14(b10)
    def fonk6(self, b7):
        b9 = b7[:]
        b10 = datetime.datetime.now()
        self.fonk7(b9)
        return self.fonk14(b10)
    def fonk7(self, b9):
        if len(b9) <= 1:
            return b9
        less, more, b19 = [], [], []
        b20 = b9[0]
        for element in b9:
            if element < b20:
                less.append(element)
            elif element > b20:
                more.append(element)
            else:
                b19.append(element)
        return self.fonk7(less) + b19 + self.fonk7(more)
    def fonk8(self, b7):
        b9 = b7[:]
        b10 = datetime.datetime.now()
        self.fonk9(b9)
        return self.fonk14(b10)
    def fonk9(self, b9):
        if len(b9) > 1:
            b21 = len(b9)
            left, b22 = b9[:b21], b9[b21:]
            self.fonk9(left)
            self.fonk9(b22)
            a7 = b13 = k = 0
            while a7 < len(left) and b13 < len(b22):
                if left[a7] < b22[b13]:
                    b9[k] = left[a7]
                    a7 += 1
                else:
                    b9[k] = b22[b13]
                    b13 += 1
                k += 1
            while a7 < len(left):
                b9[k] = left[a7]
                a7 += 1
                k += 1
            while b13 < len(b22):
                b9[k] = b22[b13]
                b13 += 1
                k += 1
    def fonk10(self, b7):
        b9 = b7[:]
        b10 = datetime.datetime.now()
        b11 = len(b9)
        self.fonk11(b9, b11)
        b23 = b11 - 1
        while b23 > 0:
            b9[b23], b9[0] = b9[0], b9[b23]
            b23 -= 1
            self.fonk12(b9, 0, b23)
        return self.fonk14(b10)
    def fonk11(self, b9, b11):
        b24 = (b11 - 2)
        while b24 >= 0:
            self.fonk12(b9, b24, b11 - 1)
            b24 -= 1
    def fonk12(self, b9, b24, b23):
        b25 = b24
        while b25 * 2 + 1 <= b23:
            b26 = b25 * 2 + 1
            if b26 + 1 <= b23 and b9[b26 + 1] > b9[b26]:
                b26 += 1
            if b9[b26] > b9[b25]:
                b9[b25], b9[b26] = b9[b26], b9[b25]
                b25 = b26
            else:
                return
    def fonk13(self, inc):
        if inc.startswith("4"):
            return "5" + inc[1:]
        if inc.startswith("5"):
            return "4" + inc[1:] + "0"
        if inc.startswith("0"):
            return "40"
    def fonk14(self, b10):
        b27 = datetime.datetime.now() - b10
        return (b27.days * 24 * 60 * 60 + b27.seconds) * 1000 + b27.microseconds / 1000.0
    def fonk15(self, a5, minimum, maximum):
        return [random.randint(minimum, maximum) for _ in range(a5)]
if b28 = = "__main__":
    b29 = class1()
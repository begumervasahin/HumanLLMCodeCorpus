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
            print(f"Iteration: {self.a5}")
            b6 = self.b1.add_sheet(str(self.a5))
            if self.a5 <= self.a3:
                b6.write(0, 0, "Bubble sort")
                b6.write(0, 1, "Insertion sort")
            b6.write(0, 2, "Quick sort")
            b6.write(0, 3, "Heap sort")
            b6.write(0, 4, "Merge sort")
            b6.write(0, 5, "Radix sort")
            for b23 in range(1, 6):
                b7 = self.fonk15(self.a5, self.a1, self.a2)
                if self.a5 <= self.a3:
                    b8 = self.fonk3(b7)
                    b6.write(b23, 0, b8, self.b2)
                    b8 = self.fonk4(b7)
                    b6.write(b23, 1, b8, self.b2)
                b8 = self.fonk6(b7)
                b6.write(b23, 2, b8, self.b2)
                b8 = self.fonk10(b7)
                b6.write(b23, 3, b8, self.b2)
                b8 = self.fonk8(b7)
                b6.write(b23, 4, b8, self.b2)
                b8 = self.fonk5(b7)
                b6.write(b23, 5, b8, self.b2)
            self.b3 = self.fonk13(self.b3)
            self.a5 += int(self.b3)
            self.b1.save('Data.xls')
            print(f"Time taken for iteration: {datetime.datetime.now() - b5}\n")
        print(f"Time taken overall: {datetime.datetime.now() - self.b4}")
    @staticmethod
    def fonk3(b7):
        b9 = b7[:]
        b10 = datetime.datetime.now()
        b11 = len(b9)
        for b23 in range(b11 - 1):
            for b13 in range(b11 - b23 - 1):
                if b9[b13 + 1] < b9[b13]:
                    b9[b13], b9[b13 + 1] = b9[b13 + 1], b9[b13]
        return class1.fonk14(b10)
    @staticmethod
    def fonk4(b7):
        b9 = b7[:]
        b10 = datetime.datetime.now()
        b11 = len(b9)
        for b23 in range(1, b11):
            b12 = b9[b23]
            b13 = b23
            while b13 > 0 and b12 < b9[b13 - 1]:
                b9[b13] = b9[b13 - 1]
                b13 -= 1
            b9[b13] = b12
        return class1.fonk14(b10)
    @staticmethod
    def fonk5(b7):
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
            b9 = [element for bucket in b16 for element in bucket]
        return class1.fonk14(b10)
    @staticmethod
    def fonk6(b7):
        b9 = b7[:]
        b10 = datetime.datetime.now()
        class1.fonk7(b9)
        return class1.fonk14(b10)
    @staticmethod
    def fonk7(b9):
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
        return class1.fonk7(less) + b19 + class1.fonk7(more)
    @staticmethod
    def fonk8(b7):
        b9 = b7[:]
        b10 = datetime.datetime.now()
        class1.fonk9(b9)
        return class1.fonk14(b10)
    @staticmethod
    def fonk9(b9):
        if len(b9) > 1:
            b21 = len(b9)
            left, b22 = b9[:b21], b9[b21:]
            class1.fonk9(left)
            class1.fonk9(b22)
            b23 = b13 = k = 0
            while b23 < len(left) and b13 < len(b22):
                if left[b23] < b22[b13]:
                    b9[k] = left[b23]
                    b23 += 1
                else:
                    b9[k] = b22[b13]
                    b13 += 1
                k += 1
            while b23 < len(left):
                b9[k] = left[b23]
                b23 += 1
                k += 1
            while b13 < len(b22):
                b9[k] = b22[b13]
                b13 += 1
                k += 1
    @staticmethod
    def fonk10(b7):
        b9 = b7[:]
        b10 = datetime.datetime.now()
        b11 = len(b9)
        class1.fonk11(b9, b11)
        b24 = b11 - 1
        while b24 > 0:
            b9[b24], b9[0] = b9[0], b9[b24]
            b24 -= 1
            class1.fonk12(b9, 0, b24)
        return class1.fonk14(b10)
    @staticmethod
    def fonk11(b9, b11):
        b25 = (b11 - 2)
        while b25 >= 0:
            class1.fonk12(b9, b25, b11 - 1)
            b25 -= 1
    @staticmethod
    def fonk12(b9, b25, b24):
        b26 = b25
        while (b26 * 2 + 1) <= b24:
            b27 = b26 * 2 + 1
            if b27 + 1 <= b24 and b9[b27 + 1] > b9[b27]:
                b27 += 1
            if b9[b27] > b9[b26]:
                b9[b26], b9[b27] = b9[b27], b9[b26]
                b26 = b27
            else:
                return
    @staticmethod
    def fonk13(inc):
        if inc[:1] == "4":
            return "5" + inc[1:]
        if inc[:1] == "5":
            return "4" + inc[1:] + "0"
        if inc[:1] == "0":
            return "40"
    @staticmethod
    def fonk14(b10):
        b28 = datetime.datetime.now() - b10
        b29 = (b28.days * 24 * 60 * 60 + b28.seconds) * 1000 + b28.microseconds / 1000.0
        return b29
    @staticmethod
    def fonk15(a5, minimum, maximum):
        return [random.randint(minimum, maximum) for _ in range(a5)]
if b30 = = "__main__":
    class1()
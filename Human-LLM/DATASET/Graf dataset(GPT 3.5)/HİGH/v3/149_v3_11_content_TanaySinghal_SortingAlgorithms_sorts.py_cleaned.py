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
        while self.a5 <= self.a4:
            b5 = datetime.datetime.now()
            print("Iteration:", self.a5)
            b6 = self.b1.add_sheet(str(self.a5))
            if self.a5 <= self.a3:
                self.fonk2(b6)
            self.fonk3(b6)
            self.fonk6()
            print("Time taken for iteration:", datetime.datetime.now() - b5)
            print()
        print("Time taken overall:", datetime.datetime.now() - self.b4)
    def fonk2(self, b6):
        b6.write(0, 0, "Bubble sort")
        b6.write(0, 1, "Insertion sort")
        b6.write(0, 2, "Quick sort")
        b6.write(0, 3, "Heap sort")
        b6.write(0, 4, "Merge sort")
        b6.write(0, 5, "Radix sort")
    def fonk3(self, b6):
        for a7 in range(1, 6):
            b7 = self.fonk19(self.a5, self.a1, self.a2)
            if self.a5 <= self.a3:
                self.fonk4(b6, a7, self.bubble_sort, b7)
                self.fonk4(b6, a7, self.insertion_sort, b7)
            self.fonk4(b6, a7, self.quick_sort, b7)
            self.fonk4(b6, a7, self.heap_sort, b7)
            self.fonk4(b6, a7, self.merge_sort, b7)
            self.fonk4(b6, a7, self.radix_sort, b7)
    def fonk4(self, b6, row, sort_func, b7):
        b8 = datetime.datetime.now()
        sort_func(b7)
        b9 = self.fonk18(b8)
        b6.write(row, self.fonk5(sort_func), b9, self.b2)
    def fonk5(self, sort_func):
        b10 = [self.bubble_sort, self.insertion_sort, self.quick_sort, self.heap_sort, self.merge_sort, self.radix_sort]
        return b10.index(sort_func)
    def fonk6(self):
        self.b3 = self.fonk17(self.b3)
        self.a5 += int(self.b3)
        self.b1.save('Data.xls')
    def fonk7(self, b7):
        b11 = b7[:]
        b12 = len(b11)
        for a7 in range(b12 - 1):
            for b14 in range(b12 - a7 - 1):
                if b11[b14 + 1] < b11[b14]:
                    b11[b14], b11[b14 + 1] = b11[b14 + 1], b11[b14]
    def fonk8(self, b7):
        b11 = b7[:]
        b12 = len(b11)
        for a7 in range(1, b12):
            b13 = b11[a7]
            b14 = a7
            while b14 > 0 and b13 < b11[b14 - 1]:
                b11[b14] = b11[b14 - 1]
                b14 -= 1
            b11[b14] = b13
    def fonk9(self, b7):
        b11 = b7[:]
        a6 = 10
        b15 = max(b11)
        b16 = len(str(b15))
        for digit in range(1, b16 + 1):
            b17 = [[] for _ in range(a6)]
            b18 = 10 ** (digit - 1)
            for element in b11:
                b19 = (element
                b17[b19].append(element)
            a7 = 0
            for bucket in b17:
                for element in bucket:
                    b11[a7] = element
                    a7 += 1
    def fonk10(self, b7):
        b11 = b7[:]
        self.fonk11(b11)
    def fonk11(self, b11):
        if len(b11) <= 1:
            return b11
        b20 = b11[0]
        b21 = [x for x in b11[1:] if x < b20]
        b22 = [x for x in b11 if x == b20]
        b23 = [x for x in b11[1:] if x > b20]
        return self.fonk11(b21) + b22 + self.fonk11(b23)
    def fonk12(self, b7):
        b11 = b7[:]
        self.fonk13(b11)
    def fonk13(self, b11):
        if len(b11) > 1:
            b24 = len(b11)
            b25 = b11[:b24]
            b26 = b11[b24:]
            self.fonk13(b25)
            self.fonk13(b26)
            a7 = b14 = k = 0
            while a7 < len(b25) and b14 < len(b26):
                if b25[a7] < b26[b14]:
                    b11[k] = b25[a7]
                    a7 += 1
                else:
                    b11[k] = b26[b14]
                    b14 += 1
                k += 1
            while a7 < len(b25):
                b11[k] = b25[a7]
                a7 += 1
                k += 1
            while b14 < len(b26):
                b11[k] = b26[b14]
                b14 += 1
                k += 1
    def fonk14(self, b7):
        b11 = b7[:]
        b12 = len(b11)
        self.fonk15(b11, b12)
        b27 = b12 - 1
        while b27 > 0:
            b11[b27], b11[0] = b11[0], b11[b27]
            b27 -= 1
            self.fonk16(b11, 0, b27)
    def fonk15(self, b11, b12):
        b28 = (b12 - 2)
        while b28 >= 0:
            self.fonk16(b11, b28, b12 - 1)
            b28 -= 1
    def fonk16(self, b11, b28, b27):
        b29 = b28
        while (b29 * 2 + 1) <= b27:
            b30 = b29 * 2 + 1
            if b30 + 1 <= b27 and b11[b30 + 1] > b11[b30]:
                b30 += 1
            if b11[b30] > b11[b29]:
                b11[b29], b11[b30] = b11[b30], b11[b29]
                b29 = b30
            else:
                return
    @staticmethod
    def fonk17(inc):
        if inc[:1] == "4":
            return "5" + inc[1:]
        if inc[:1] == "5":
            return "4" + inc[1:] + "0"
        if inc[:1] == "0":
            return "40"
    @staticmethod
    def fonk18(b8):
        b31 = datetime.datetime.now() - b8
        b32 = (b31.days * 24 * 60 * 60 + b31.seconds) * 1000 + b31.microseconds / 1000.0
        return b32
    @staticmethod
    def fonk19(a5, minimum, maximum):
        return [random.randint(minimum, maximum) for _ in range(a5)]
b33 = class1()
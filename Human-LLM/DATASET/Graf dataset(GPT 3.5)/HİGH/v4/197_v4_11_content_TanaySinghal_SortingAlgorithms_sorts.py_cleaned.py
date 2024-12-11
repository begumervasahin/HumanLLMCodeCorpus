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
    def fonk2(self):
        while self.a5 <= self.a4:
            self.fonk3()
            self.a5 += int(self.b3)
        print("Time taken overall:", datetime.datetime.now() - self.b4)
    def fonk3(self):
        b5 = datetime.datetime.now()
        print("iteration:", self.a5)
        b6 = self.b1.add_sheet(str(self.a5))
        if self.a5 <= self.a3:
            self.fonk4(b6)
        for i in range(1, 6):
            b7 = self.fonk15(self.a5, self.a1, self.a2)
            if self.a5 <= self.a3:
                self.fonk5(b7, b6, i)
            self.fonk6(b7, b6, i)
        self.fonk7()
        print("Time taken for iteration:", datetime.datetime.now() - b5)
        print()
    def fonk4(self, b6):
        b8 = ["Bubble sort", "Insertion sort", "Quick sort", "Heap sort", "Merge sort", "Radix sort"]
        for i, header in enumerate(b8):
            b6.write(0, i, header)
    def fonk5(self, b7, b6, i):
        b9 = self.fonk8(b7)
        b6.write(i, 0, b9, self.b2)
        b9 = self.fonk9(b7)
        b6.write(i, 1, b9, self.b2)
    def fonk6(self, b7, b6, i):
        b10 = [self.fonk11(b7), self.fonk13(b7), self.fonk12(b7), self.fonk10(b7)]
        for b16, b9 in enumerate(b10, b11 = 2):
            b6.write(i, b16, b9, self.b2)
    def fonk7(self):
        self.b1.save('Data.xls')
    def fonk8(self, b7):
        b12 = b7[:]
        b13 = datetime.datetime.now()
        b14 = len(b12)
        for i in range(b14 - 1):
            for b16 in range(b14 - i - 1):
                if b12[b16+1] < b12[b16]:
                    b12[b16], b12[b16+1] = b12[b16+1], b12[b16]
        return self.fonk14(b13)
    def fonk9(self, b7):
        b12 = b7[:]
        b13 = datetime.datetime.now()
        b14 = len(b12)
        for i in range(1, b14):
            b15 = b12[i]
            b16 = i
            while b16 > 0 and b15 < b12[b16-1]:
                b12[b16] = b12[b16-1]
                b16 -= 1
            b12[b16] = b15
        return self.fonk14(b13)
    def fonk10(self, b7):
        b12 = b7[:]
        b13 = datetime.datetime.now()
        return self.fonk14(b13)
    def fonk11(self, b7):
        b12 = b7[:]
        b13 = datetime.datetime.now()
        return self.fonk14(b13)
    def fonk12(self, b7):
        b12 = b7[:]
        b13 = datetime.datetime.now()
        return self.fonk14(b13)
    def fonk13(self, b7):
        b12 = b7[:]
        b13 = datetime.datetime.now()
        return self.fonk14(b13)
    def fonk14(self, b13):
        b17 = datetime.datetime.now() - b13
        b18 = (b17.days * 24 * 60 * 60 + b17.seconds) * 1000 + b17.microseconds / 1000.0
        return b18
    def fonk15(self, a5, minimum, maximum):
        b7 = [None] * a5
        for i in range(len(b7)):
            b7[i] = random.randint(minimum, maximum)
        return b7
b19 = class1()
b19.fonk2()
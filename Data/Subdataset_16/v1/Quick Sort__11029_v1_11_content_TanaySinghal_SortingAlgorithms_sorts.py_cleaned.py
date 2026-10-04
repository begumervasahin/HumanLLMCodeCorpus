import random
import datetime
import xlwt
class class1:
    def fonk1(self):
        b1 = xlwt.Workbook()
        b2 = xlwt.easyxf('font: name Arial, color-index black')
        a1 = 0
        a2 = 1000
        a3 = 10000
        a4 = 10000000
        a5 = 10
        b3 = "0"
        b4 = datetime.datetime.now()
        while a5 <= a4:
            b5 = datetime.datetime.now()
            print("iteration:", a5)
            b6 = b1.add_sheet(str(a5))
            if a5 <= a3:
                b6.write(0, 0, "Bubble sort")
                b6.write(0, 1, "Insertion sort")
            b6.write(0, 2, "Quick sort")
            b6.write(0, 3, "Heap sort")
            b6.write(0, 4, "Merge sort")
            b6.write(0, 5, "Radix sort")
            for a7 in range(1, 6):
                b7 = self.fonk14(a5, a1, a2)
                if a5 <= a3:
                    b8 = self.fonk2(b7)
                    b6.write(a7, 0, b8, b2)
                    b8 = self.fonk3(b7)
                    b6.write(a7, 1, b8, b2)
                b8 = self.fonk5(b7)
                b6.write(a7, 2, b8, b2)
                b8 = self.fonk9(b7)
                b6.write(a7, 3, b8, b2)
                b8 = self.fonk7(b7)
                b6.write(a7, 4, b8, b2)
                b8 = self.fonk4(b7)
                b6.write(a7, 5, b8, b2)
            b3 = self.fonk12(b3)
            a5 += int(b3)
            b1.save('Data.xls')
            print("Time taken for iteration:", datetime.datetime.now() - b5)
            print()
        print("Time taken overall:", datetime.datetime.now() - b4)
    def fonk2(self, b7):
        b9 = b7[:]
        b10 = datetime.datetime.now()
        b11 = len(b9)
        for a7 in range(b11 - 1):
            for b13 in range(b11 - a7 - 1):
                if b9[b13 + 1] < b9[b13]:
                    b9[b13], b9[b13 + 1] = b9[b13 + 1], b9[b13]
        return self.fonk13(b10)
    def fonk3(self, b7):
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
        return self.fonk13(b10)
    def fonk4(self, b7):
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
        return self.fonk13(b10)
    def fonk5(self, b7):
        b9 = b7[:]
        b10 = datetime.datetime.now()
        self.fonk6(b9)
        return self.fonk13(b10)
    def fonk6(self, b9):
        if len(b9) <= 1:
            return b9
        b19 = []
        b20 = []
        b21 = []
        b22 = b9[0]
        for element in b9:
            if element < b22:
                b19.append(element)
            elif element > b22:
                b20.append(element)
            else:
                b21.append(element)
        return self.fonk6(b19) + b21 + self.fonk6(b20)
    def fonk7(self, b7):
        b9 = b7[:]
        b10 = datetime.datetime.now()
        self.fonk8(b9)
        return self.fonk13(b10)
    def fonk8(self, b9):
        if len(b9) > 1:
            b23 = len(b9)
            b24 = b9[:b23]
            b25 = b9[b23:]
            self.fonk8(b24)
            self.fonk8(b25)
            a7 = b13 = k = 0
            while a7 < len(b24) and b13 < len(b25):
                if b24[a7] < b25[b13]:
                    b9[k] = b24[a7]
                    a7 += 1
                else:
                    b9[k] = b25[b13]
                    b13 += 1
                k += 1
            while a7 < len(b24):
                b9[k] = b24[a7]
                a7 += 1
                k += 1
            while b13 < len(b25):
                b9[k] = b25[b13]
                b13 += 1
                k += 1
    def fonk9(self, b7):
        b9 = b7[:]
        b10 = datetime.datetime.now()
        b11 = len(b9)
        self.fonk10(b9, b11)
        b26 = b11 - 1
        while b26 > 0:
            b9[b26], b9[0] = b9[0], b9[b26]
            b26 -= 1
            self.fonk11(b9, 0, b26)
        return self.fonk13(b10)
    def fonk10(self, b9, b11):
        b27 = (b11 - 2)
        while b27 >= 0:
            self.fonk11(b9, b27, b11 - 1)
            b27 -= 1
    def fonk11(self, b9, b27, b26):
        b28 = b27
        while b28 * 2 + 1 <= b26:
            b29 = b28 * 2 + 1
            if b29 + 1 <= b26 and b9[b29 + 1] > b9[b29]:
                b29 += 1
            if b9[b29] > b9[b28]:
                b9[b28], b9[b29] = b9[b29], b9[b28]
                b28 = b29
            else:
                return
    def fonk12(self, inc):
        if inc[:1] == "4":
            return "5" + inc[1:]
        if inc[:1] == "5":
            return "4" + inc[1:] + "0"
        if inc[:1] == "0":
            return "40"
    def fonk13(self, b10):
        b30 = datetime.datetime.now() - b10
        b31 = (b30.days * 24 * 60 * 60 + b30.seconds) * 1000 + b30.microseconds / 1000.0
        return b31
    def fonk14(self, a5, minimum, maximum):
        return [random.randint(minimum, maximum) for _ in range(a5)]
if b32 = = "__main__":
    b33 = class1()
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
            self.fonk3(b6)
            self.fonk4(b6)
            self.b3 = self.fonk15(self.b3)
            self.a5 += int(self.b3)
            self.b1.save('Data.xls')
            print(f"Time taken for iteration: {datetime.datetime.now() - b5}\b20")
        print(f"Total time taken: {datetime.datetime.now() - self.b4}")
    def fonk3(self, b6):
        if self.a5 <= self.a3:
            b6.write(0, 0, "Bubble sort")
            b6.write(0, 1, "Insertion sort")
        b6.write(0, 2, "Quick sort")
        b6.write(0, 3, "Heap sort")
        b6.write(0, 4, "Merge sort")
        b6.write(0, 5, "Radix sort")
    def fonk4(self, b6):
        for b16 in range(1, 6):
            b7 = self.fonk17(self.a5, self.a1, self.a2)
            if self.a5 <= self.a3:
                b6.write(b16, 0, self.fonk5(b7[:]), self.b2)
                b6.write(b16, 1, self.fonk6(b7[:]), self.b2)
            b6.write(b16, 2, self.fonk8(b7[:]), self.b2)
            b6.write(b16, 3, self.fonk13(b7[:]), self.b2)
            b6.write(b16, 4, self.fonk11(b7[:]), self.b2)
            b6.write(b16, 5, self.fonk7(b7[:]), self.b2)
    @staticmethod
    def fonk5(b7):
        b8 = datetime.datetime.now()
        b9 = len(b7)
        for b16 in range(b9 - 1):
            for b11 in range(b9 - b16 - 1):
                if b7[b11 + 1] < b7[b11]:
                    b7[b11], b7[b11 + 1] = b7[b11 + 1], b7[b11]
        return class1.fonk16(b8)
    @staticmethod
    def fonk6(b7):
        b8 = datetime.datetime.now()
        for b16 in range(1, len(b7)):
            b10 = b7[b16]
            b11 = b16 - 1
            while b11 >= 0 and b10 < b7[b11]:
                b7[b11 + 1] = b7[b11]
                b11 -= 1
            b7[b11 + 1] = b10
        return class1.fonk16(b8)
    @staticmethod
    def fonk7(b7):
        b8 = datetime.datetime.now()
        b12 = len(str(max(b7)))
        for digit in range(b12):
            b13 = [[] for _ in range(10)]
            for number in b7:
                b13[(number
            b7 = [number for bucket in b13 for number in bucket]
        return class1.fonk16(b8)
    @staticmethod
    def fonk8(b7):
        b8 = datetime.datetime.now()
        class1.fonk9(b7, 0, len(b7) - 1)
        return class1.fonk16(b8)
    @staticmethod
    def fonk9(b7, low, high):
        if low < high:
            b14 = class1.fonk10(b7, low, high)
            class1.fonk9(b7, low, b14 - 1)
            class1.fonk9(b7, b14 + 1, high)
    @staticmethod
    def fonk10(b7, low, high):
        b15 = b7[high]
        b16 = low - 1
        for b11 in range(low, high):
            if b7[b11] < b15:
                b16 += 1
                b7[b16], b7[b11] = b7[b11], b7[b16]
        b7[b16 + 1], b7[high] = b7[high], b7[b16 + 1]
        return b16 + 1
    @staticmethod
    def fonk11(b7):
        b8 = datetime.datetime.now()
        class1.fonk12(b7)
        return class1.fonk16(b8)
    @staticmethod
    def fonk12(b7):
        if len(b7) > 1:
            b17 = len(b7)
            b18 = b7[:b17]
            b19 = b7[b17:]
            class1.fonk12(b18)
            class1.fonk12(b19)
            b16 = b11 = k = 0
            while b16 < len(b18) and b11 < len(b19):
                if b18[b16] < b19[b11]:
                    b7[k] = b18[b16]
                    b16 += 1
                else:
                    b7[k] = b19[b11]
                    b11 += 1
                k += 1
            while b16 < len(b18):
                b7[k] = b18[b16]
                b16 += 1
                k += 1
            while b11 < len(b19):
                b7[k] = b19[b11]
                b11 += 1
                k += 1
    @staticmethod
    def fonk13(b7):
        b8 = datetime.datetime.now()
        b20 = len(b7)
        for b16 in range(b20
            class1.fonk14(b7, b20, b16)
        for b16 in range(b20 - 1, 0, -1):
            b7[b16], b7[0] = b7[0], b7[b16]
            class1.fonk14(b7, b16, 0)
        return class1.fonk16(b8)
    @staticmethod
    def fonk14(b7, b20, b16):
        b21 = b16
        b22 = 2 * b16 + 1
        b23 = 2 * b16 + 2
        if b22 < b20 and b7[b21] < b7[b22]:
            b21 = b22
        if b23 < b20 and b7[b21] < b7[b23]:
            b21 = b23
        if b21 != b16:
            b7[b16], b7[b21] = b7[b21], b7[b16]
            class1.fonk14(b7, b20, b21)
    @staticmethod
    def fonk15(inc):
        if inc[:1] == "4":
            return "5" + inc[1:]
        if inc[:1] == "5":
            return "4" + inc[1:] + "0"
        if inc[:1] == "0":
            return "40"
    @staticmethod
    def fonk16(b8):
        b24 = datetime.datetime.now() - b8
        b25 = b24.total_seconds() * 1000
        return b25
    @staticmethod
    def fonk17(a5, minimum, maximum):
        return [random.randint(minimum, maximum) for _ in range(a5)]
if b26 = = "__main__":
    class1()
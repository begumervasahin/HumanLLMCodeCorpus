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
            print(f"Iteration a5: {self.a5}")
            b6 = self.b1.add_sheet(str(self.a5))
            b7 = ["Bubble Sort", "Insertion Sort", "Quick Sort", "Heap Sort", "Merge Sort", "Radix Sort"]
            for idx, header in enumerate(b7):
                if self.a5 > self.a3 and idx < 2:
                    continue
                b6.write(0, idx, header)
            for a7 in range(1, 6):
                b8 = self.fonk15(self.a5, self.a1, self.a2)
                if self.a5 <= self.a3:
                    b6.write(a7, 0, self.fonk16(self.bubble_sort, b8), self.b2)
                    b6.write(a7, 1, self.fonk16(self.insertion_sort, b8), self.b2)
                b6.write(a7, 2, self.fonk16(self.quick_sort, b8), self.b2)
                b6.write(a7, 3, self.fonk16(self.heap_sort, b8), self.b2)
                b6.write(a7, 4, self.fonk16(self.merge_sort, b8), self.b2)
                b6.write(a7, 5, self.fonk16(self.radix_sort, b8), self.b2)
            self.b3 = self.fonk13(self.b3)
            self.a5 += int(self.b3)
            self.b1.save('Data.xls')
            print(f"Time taken for iteration: {datetime.datetime.now() - b5}\n")
        print(f"Total time taken: {datetime.datetime.now() - self.b4}")
    def fonk3(self, b8):
        b9 = b8[:]
        b10 = len(b9)
        for a7 in range(b10 - 1):
            for b12 in range(b10 - a7 - 1):
                if b9[b12 + 1] < b9[b12]:
                    b9[b12], b9[b12 + 1] = b9[b12 + 1], b9[b12]
        return b9
    def fonk4(self, b8):
        b9 = b8[:]
        b10 = len(b9)
        for a7 in range(1, b10):
            b11 = b9[a7]
            b12 = a7
            while b12 > 0 and b11 < b9[b12 - 1]:
                b9[b12] = b9[b12 - 1]
                b12 -= 1
            b9[b12] = b11
        return b9
    def fonk5(self, b8):
        b9 = b8[:]
        a6 = 10
        b13 = max(b9)
        b14 = len(str(b13))
        for digit in range(1, b14 + 1):
            b15 = [[] for _ in range(a6)]
            b16 = 10 ** (digit - 1)
            for element in b9:
                b17 = (element
                b15[b17].append(element)
            a7 = 0
            for bucket in b15:
                for element in bucket:
                    b9[a7] = element
                    a7 += 1
        return b9
    def fonk6(self, b8):
        return self.fonk7(b8[:])
    def fonk7(self, b9):
        if len(b9) <= 1:
            return b9
        less, more, b18 = [], [], []
        b19 = b9[0]
        for element in b9:
            if element < b19:
                less.append(element)
            elif element > b19:
                more.append(element)
            else:
                b18.append(element)
        return self.fonk7(less) + b18 + self.fonk7(more)
    def fonk8(self, b8):
        b9 = b8[:]
        self.fonk9(b9)
        return b9
    def fonk9(self, b9):
        if len(b9) > 1:
            b20 = len(b9)
            left, b21 = b9[:b20], b9[b20:]
            self.fonk9(left)
            self.fonk9(b21)
            a7 = b12 = k = 0
            while a7 < len(left) and b12 < len(b21):
                if left[a7] < b21[b12]:
                    b9[k] = left[a7]
                    a7 += 1
                else:
                    b9[k] = b21[b12]
                    b12 += 1
                k += 1
            while a7 < len(left):
                b9[k] = left[a7]
                a7 += 1
                k += 1
            while b12 < len(b21):
                b9[k] = b21[b12]
                b12 += 1
                k += 1
    def fonk10(self, b8):
        b9 = b8[:]
        b10 = len(b9)
        self.fonk11(b9, b10)
        b22 = b10 - 1
        while b22 > 0:
            b9[b22], b9[0] = b9[0], b9[b22]
            b22 -= 1
            self.fonk12(b9, 0, b22)
        return b9
    def fonk11(self, b9, b10):
        b23 = (b10 - 2)
        while b23 >= 0:
            self.fonk12(b9, b23, b10 - 1)
            b23 -= 1
    def fonk12(self, b9, b23, b22):
        b24 = b23
        while b24 * 2 + 1 <= b22:
            b25 = b24 * 2 + 1
            if b25 + 1 <= b22 and b9[b25 + 1] > b9[b25]:
                b25 += 1
            if b9[b25] > b9[b24]:
                b9[b24], b9[b25] = b9[b25], b9[b24]
                b24 = b25
            else:
                return
    def fonk13(self, inc):
        if inc.startswith("4"):
            return "5" + inc[1:]
        if inc.startswith("5"):
            return "4" + inc[1:] + "0"
        if inc.startswith("0"):
            return "40"
    def fonk14(self, b27):
        b26 = datetime.datetime.now() - b27
        return (b26.days * 24 * 60 * 60 + b26.seconds) * 1000 + b26.microseconds / 1000.0
    def fonk15(self, a5, minimum, maximum):
        return [random.randint(minimum, maximum) for _ in range(a5)]
    def fonk16(self, sort_function, b8):
        b27 = datetime.datetime.now()
        sort_function(b8)
        return self.fonk14(b27)
if b28 = = "__main__":
    b29 = class1()
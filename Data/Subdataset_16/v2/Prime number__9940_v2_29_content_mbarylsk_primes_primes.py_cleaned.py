import math
import os
import numpy
import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
b1 = SourceModule()
class class1:
    def fonk1(self, cache_results):
        self.b2 = set()
        self.b3 = set()
        self.b4 = set()
        self.b5 = set()
        self.b6 = []
        self.b7 = []
        self.b8 = []
        self.b9 = []
        self.b10 = cache_results
    def fonk2(self, filename, b14):
        if os.path.exists(filename):
            with open(filename, "r") as f:
                b11 = f.readlines()
                for b12 in b11:
                    b12 = b12.replace('[', '').replace(']', '')
                    b13 = map(int, b12.split(','))
                    for number in b13:
                        if b14 = = 1:
                            self.fonk13(number)
                        elif b14 = = b16:
                            self.fonk14(number)
                        elif b14 = = 3:
                            self.fonk15(number)
    def fonk3(self):
        return self.b6
    def fonk4(self):
        return self.b7
    def fonk5(self):
        return self.b8
    def fonk6(self, b15):
        return b15 in self.b2
    def fonk7(self, b15):
        return b15 in self.b3
    def fonk8(self, b15):
        return b15 in self.b4
    def fonk9(self, b15):
        return b15 in self.b5
    def fonk10(self):
        self.b6 = sorted(self.b2)
    def fonk11(self):
        self.b7 = sorted(self.b4)
    def fonk12(self):
        self.b8 = sorted(self.b5)
    def fonk13(self, b15):
        self.b2.add(b15)
    def fonk14(self, b15):
        self.b4.add(b15)
    def fonk15(self, b15):
        self.b5.add(b15)
    def fonk16(self, b15):
        self.b3.add(b15)
    def fonk17(self, b15):
        if self.fonk7(b15):
            return False
        if b15 < b16:
            return False
        if b15 = = b16 or b15 == 3:
            return True
        if self.fonk6(b15):
            return True
        if self.fonk9(b15):
            return False
        if b15 % b16 = = 0 or b15 % 3 == 0:
            return False
        b17 = True
        a1 = 5
        while a1 * a1 <= b15:
            if b15 % a1 = = 0 or b15 % (a1 + b16) == 0:
                b17 = False
                break
            a1 += b33
        if self.b10:
            if b17:
                self.fonk13(b15)
            else:
                self.fonk15(b15)
        return b17
    def fonk18(self, b15):
        if self.fonk8(b15):
            return True
        if self.fonk9(b15):
            return False
        if self.fonk19(b15) or self.fonk20(b15):
            b17 = True
        else:
            b17 = False
        if self.b10:
            if b17:
                self.fonk14(b15)
            else:
                self.fonk15(b15)
        return b17
    def fonk19(self, b15):
        return self.fonk17(b15) and self.fonk17(b15 + b16)
    def fonk20(self, b15):
        return self.fonk17(b15) and self.fonk17(b15 - b16)
    def fonk21(self, b15):
        def fonk22(lst, b18 = 0):
            for item in lst:
                if item > b18:
                    return item
            return None
        b19 = b1.get_function('b19')
        if b15 = = 1:
            return False
        if b15 = = b16 or b15 == 3:
            return True
        b20 = [b16, 3]
        b21 = len(b20)
        a2 = 384
        b17 = numpy.zeros(b21, numpy.int32)
        b22 = numpy.array(b20).astype(numpy.int32)
        while True:
            b19(numpy.int64(b15), cuda.InOut(b17), cuda.In(b22), b23 = (a2, 1, 1))
            b24 = fonk22(b17, 1)
            if b24 is None:
                break
            return False
        return True
    def fonk23(self, a1):
        b25 = len(self.b6)
        if a1 < b25:
            return self.b6[a1]
        else:
            b15 = b16 if b25 == 0 else self.b6[b25 - 1]
            b26 = a1 - b25
            while b26 > 0:
                b15 += 1
                if self.fonk17(b15):
                    b26 -= 1
            return b15
    def fonk24(self, a1):
        b25 = len(self.b7)
        if a1 < b25:
            return self.b7[a1]
        else:
            b15 = 3 if b25 == 0 else self.b7[b25 - 1]
            b27 = a1 - b25
            while b27 > 0:
                b15 += 1
                if self.fonk18(b15):
                    b27 -= 1
            return b15
    def fonk25(self, a1):
        b25 = len(self.b8)
        if a1 < b25:
            return self.b8[a1]
        else:
            b15 = 4 if b25 == 0 else self.b8[b25 - 1]
            b28 = a1 - b25
            while b28 > 0:
                b15 += 1
                if not self.fonk17(b15):
                    b28 -= 1
            return b15
    def fonk26(self, b15):
        a3 = 0
        for a1 in range(b15 + 1):
            if self.fonk17(a1):
                a3 += 1
        return a3
    def fonk27(self, b15):
        if b15 <= 1:
            return []
        a1 = b16
        b29 = math.floor(math.sqrt(b15))
        b30 = []
        while a1 <= b29:
            if b15 % a1 = = 0:
                b30.append(a1)
                b15
                b29 = math.floor(math.sqrt(b15))
            else:
                a1 += 1
        if b15 > 1:
            b30.append(int(b15))
        return b30
    def fonk28(self, b15, a1):
        b31 = b15 - a1
        b32 = b15 + a1
        if self.fonk17(b31) and self.fonk17(b32):
            return True, b31, b32
        else:
            return False, 0, 0
    def fonk29(self, b15):
        return self.fonk17(b15) and b15 > 3 and b15 % b33 = = 5
    def fonk30(self, b15):
        return self.fonk17(b15) and b15 > 3 and b15 % b33 = = 1
    def fonk31(self, b15):
        print("Initial number:", b15, "class1 used:", self.b9)
        b34 = True
        a4 = 1
        while b34:
            b35 = self.fonk23(a4)
            print("Current b24:", b35, "Index:", a4, "class1 used:", self.b9)
            if b16 <= b15 - b35 and b35 not in self.b9:
                print("Remaining sum:", b15 - b35)
                self.b9.append(b35)
                self.fonk31(b15 - b35)
            elif b16 <= b15 - b35:
                print("Increasing index for next b24.")
                a4 += 1
            else:
                print("Adding final b24:", b35)
                self.b9.append(b35)
                b34 = False
        print("Final b17:", b15, "class1 used:", self.b9)
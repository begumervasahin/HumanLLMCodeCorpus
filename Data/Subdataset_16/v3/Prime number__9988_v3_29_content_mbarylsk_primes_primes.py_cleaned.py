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
                        elif b14 = = b15:
                            self.fonk14(number)
                        elif b14 = = 3:
                            self.fonk15(number)
    def fonk3(self):
        return self.b6
    def fonk4(self):
        return self.b7
    def fonk5(self):
        return self.b8
    def fonk6(self, b19):
        return b19 in self.b2
    def fonk7(self, b19):
        return b19 in self.b3
    def fonk8(self, b19):
        return b19 in self.b4
    def fonk9(self, b19):
        return b19 in self.b5
    def fonk10(self):
        self.b6 = sorted(self.b2)
    def fonk11(self):
        self.b7 = sorted(self.b4)
    def fonk12(self):
        self.b8 = sorted(self.b5)
    def fonk13(self, b19):
        self.b2.add(b19)
    def fonk14(self, b19):
        self.b4.add(b19)
    def fonk15(self, b19):
        self.b5.add(b19)
    def fonk16(self, b19):
        self.b3.add(b19)
    def fonk17(self, b19):
        if self.fonk7(b19):
            return False
        if b19 < b15:
            return False
        if b19 in {b15, 3}:
            return True
        if self.fonk6(b19):
            return True
        if self.fonk9(b19):
            return False
        if b19 % b15 = = 0 or b19 % 3 == 0:
            return False
        b16 = True
        a1 = 5
        while a1 * a1 <= b19:
            if b19 % a1 = = 0 or b19 % (a1 + b15) == 0:
                b16 = False
                break
            a1 += b33
        if self.b10:
            if b16:
                self.fonk13(b19)
            else:
                self.fonk15(b19)
        return b16
    def fonk18(self, b19):
        if self.fonk8(b19):
            return True
        if self.fonk9(b19):
            return False
        if self.fonk19(b19) or self.fonk20(b19):
            b16 = True
        else:
            b16 = False
        if self.b10:
            if b16:
                self.fonk14(b19)
            else:
                self.fonk15(b19)
        return b16
    def fonk19(self, b19):
        return self.fonk17(b19) and self.fonk17(b19 + b15)
    def fonk20(self, b19):
        return self.fonk17(b19) and self.fonk17(b19 - b15)
    def fonk21(self, b19):
        def fonk22(lst, b17 = 0):
            for item in lst:
                if item > b17:
                    return item
            return None
        b18 = b1.get_function('b18')
        if b19 = = 1:
            return False
        if b19 in {b15, 3}:
            return True
        b20 = [b15, 3]
        b21 = len(b20)
        a2 = 384
        b16 = numpy.zeros(b21, numpy.int32)
        b22 = numpy.array(b20).astype(numpy.int32)
        while True:
            b18(numpy.int64(b19), cuda.InOut(b16), cuda.In(b22), b23 = (a2, 1, 1))
            b24 = fonk22(b16, 1)
            if b24 is None:
                break
            return False
        return True
    def fonk23(self, a1):
        b25 = len(self.b6)
        if a1 < b25:
            return self.b6[a1]
        else:
            b19 = b15 if b25 == 0 else self.b6[b25 - 1]
            b26 = a1 - b25
            while b26 > 0:
                b19 += 1
                if self.fonk17(b19):
                    b26 -= 1
            return b19
    def fonk24(self, a1):
        b25 = len(self.b7)
        if a1 < b25:
            return self.b7[a1]
        else:
            b19 = 3 if b25 == 0 else self.b7[b25 - 1]
            b27 = a1 - b25
            while b27 > 0:
                b19 += 1
                if self.fonk18(b19):
                    b27 -= 1
            return b19
    def fonk25(self, a1):
        b25 = len(self.b8)
        if a1 < b25:
            return self.b8[a1]
        else:
            b19 = 4 if b25 == 0 else self.b8[b25 - 1]
            b28 = a1 - b25
            while b28 > 0:
                b19 += 1
                if not self.fonk17(b19):
                    b28 -= 1
            return b19
    def fonk26(self, b19):
        a3 = 0
        for a1 in range(b19 + 1):
            if self.fonk17(a1):
                a3 += 1
        return a3
    def fonk27(self, b19):
        if b19 <= 1:
            return []
        a1 = b15
        b29 = math.floor(math.sqrt(b19))
        b30 = []
        while a1 <= b29:
            if b19 % a1 = = 0:
                b30.append(a1)
                b19
                b29 = math.floor(math.sqrt(b19))
            else:
                a1 += 1
        if b19 > 1:
            b30.append(int(b19))
        return b30
    def fonk28(self, b19, a1):
        b31 = b19 - a1
        b32 = b19 + a1
        if self.fonk17(b31) and self.fonk17(b32):
            return True, b31, b32
        else:
            return False, 0, 0
    def fonk29(self, b19):
        return self.fonk17(b19) and b19 > 3 and b19 % b33 = = 5
    def fonk30(self, b19):
        return self.fonk17(b19) and b19 > 3 and b19 % b33 = = 1
    def fonk31(self, b19):
        print("Initial number:", b19, "class1 used:", self.b9)
        b34 = True
        a4 = 1
        while b34:
            b35 = self.fonk23(a4)
            print("Current b24:", b35, "Index:", a4, "class1 used:", self.b9)
            if b15 <= b19 - b35 and b35 not in self.b9:
                print("Remaining sum:", b19 - b35)
                self.b9.append(b35)
                self.fonk31(b19 - b35)
            elif b15 <= b19 - b35:
                print("Increasing index for next b24.")
                a4 += 1
            else:
                print("Adding final b24:", b35)
                self.b9.append(b35)
                b34 = False
        print("Final b16:", b19, "class1 used:", self.b9)
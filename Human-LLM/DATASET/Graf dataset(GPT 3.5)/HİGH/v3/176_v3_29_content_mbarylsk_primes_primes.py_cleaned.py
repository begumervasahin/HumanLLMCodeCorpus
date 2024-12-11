import os
import numpy
import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
import math
b1 = SourceModule()
class class1:
    def fonk1(self, cache_results):
        self.b2 = cache_results
        self.b3 = set()
        self.b4 = set()
        self.b5 = set()
        self.b6 = set()
        self.b7 = []
        self.b8 = []
        self.b9 = []
        self.b10 = []
    def fonk2(self, filename, b14):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                b11 = file.readlines()
                for b12 in b11:
                    b12 = b12.replace('[', '').replace(']', '')
                    b13 = b12.split(',')
                    for number in b13:
                        self.fonk3(int(number), b14)
    def fonk3(self, b20, b14):
        if b14 = = 1:
            self.b3.add(b20)
        elif b14 = = b16:
            self.b5.add(b20)
        elif b14 = = 3:
            self.b6.add(b20)
    def fonk4(self, b15):
        if b15 = = "b3":
            self.b7 = sorted(self.b3)
        elif b15 = = "twinprimes":
            self.b8 = sorted(self.b5)
        elif b15 = = "nonprimes":
            self.b9 = sorted(self.b6)
    def fonk5(self, b20, b15):
        if b15 = = "b3":
            return b20 in self.b3
        elif b15 = = "b4":
            return b20 in self.b4
        elif b15 = = "twinprimes":
            return b20 in self.b5
        elif b15 = = "nonprimes":
            return b20 in self.b6
    def fonk6(self, b20):
        self.b4.add(b20)
    def fonk7(self, b20):
        if self.fonk5(b20, "b4"):
            return False
        if b20 < b16:
            return False
        elif b20 in (b16, 3):
            return True
        elif self.fonk5(b20, "b3"):
            return True
        elif self.fonk5(b20, "nonprimes"):
            return False
        elif b20 % b16 = = 0 or b20 % 3 == 0:
            return False
        a1 = 5
        while a1 * a1 <= b20:
            if b20 % a1 = = 0 or b20 % (a1 + b16) == 0:
                return False
            a1 += b32
        if self.b2:
            if b20 not in self.b3:
                self.b3.add(b20)
            else:
                self.b6.add(b20)
        return True
    def fonk8(self, b20):
        if self.fonk5(b20, "twinprimes"):
            return True
        elif self.fonk5(b20, "nonprimes"):
            return False
        elif self.fonk9(b20) or self.fonk10(b20):
            b17 = True
        else:
            b17 = False
        if self.b2:
            if b17:
                self.b5.add(b20)
            else:
                self.b6.add(b20)
        return b17
    def fonk9(self, b20):
        return self.fonk7(b20) and self.fonk7(b20 + b16)
    def fonk10(self, b20):
        return self.fonk7(b20) and self.fonk7(b20 - b16)
    def fonk11(self, b20):
        def fonk12(list, b18 = 0):
            for item in list:
                if item > b18:
                    return item
            return None
        b19 = b1.get_function('b19')
        if b20 = = 1:
            return False
        if b20 in (b16, 3):
            return True
        b21 = [b16, 3]
        b22 = len(b21)
        a2 = 384
        b17 = numpy.zeros(b22, numpy.int32)
        b3 = numpy.copy(b21).astype(numpy.int32)
        while True:
            b19(numpy.int64(b20), cuda.InOut(b17), cuda.In(b3), b23 = (a2, 1, 1))
            b24 = fonk12(b17, 1)
            if b24 is None:
                break
            return False
        return True
    def fonk13(self, a1):
        b25 = len(self.b7)
        if a1 < b25:
            return self.b7[a1]
        else:
            b20 = self.b7[-1] if b25 > 0 else b16
            b26 = a1 - b25
            while b26 > 0:
                b20 += 1
                if self.fonk7(b20):
                    b26 -= 1
        return b20
    def fonk14(self, a1):
        b25 = len(self.b8)
        if a1 < b25:
            return self.b8[a1]
        else:
            b20 = self.b8[-1] if b25 > 0 else 3
            b27 = a1 - b25
            while b27 > 0:
                b20 += 1
                if self.fonk8(b20):
                    b27 -= 1
        return b20
    def fonk15(self, a1):
        b25 = len(self.b9)
        if a1 < b25:
            return self.b9[a1]
        else:
            b20 = self.b9[-1] if b25 > 0 else 4
            b28 = a1 - b25
            while b28 > 0:
                b20 += 1
                if not self.fonk7(b20):
                    b28 -= 1
        return b20
    def fonk16(self, b20):
        a3 = 0
        for a1 in range(b20 + 1):
            if self.fonk7(a1):
                a3 += 1
        return a3
    def fonk17(self, b20):
        if b20 <= 1:
            return []
        b29 = []
        a1 = b16
        while a1 * a1 <= b20:
            if b20 % a1 = = 0:
                b29.append(a1)
                b20
            else:
                a1 += 1
        if b20 > 1:
            b29.append(b20)
        return b29
    def fonk18(self, b20, distance):
        b30 = b20 - distance
        b31 = b20 + distance
        return self.fonk7(b30) and self.fonk7(b31), b30, b31
    def fonk19(self, b20):
        return self.fonk7(b20) and (b20 > 3) and (b20 % b32 = = 5)
    def fonk20(self, b20):
        return self.fonk7(b20) and (b20 > 3) and (b20 % b32 = = 1)
    def fonk21(self, b20):
        b33 = True
        a4 = 1
        while b33:
            b34 = self.fonk13(a4)
            if b16 <= b20 - b34 and b34 not in self.b10:
                self.b10.append(b34)
                self.fonk21(b20 - b34)
            elif b16 <= b20 - b34:
                a4 += 1
            else:
                self.b10.append(b34)
                b33 = False
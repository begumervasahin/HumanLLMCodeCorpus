import math
import os
import numpy
import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
b1 = SourceModule()
class class1:
    def fonk1(self, b2 = False):
        self.b3 = set()
        self.b4 = set()
        self.b5 = set()
        self.b6 = set()
        self.b7 = []
        self.b8 = []
        self.b9 = []
        self.b10 = []
        self.b11 = b2
    def fonk2(self, filename, b15):
        if os.path.exists(filename):
            with open(filename, "r") as f:
                b12 = f.readlines()
                for b13 in b12:
                    b13 = b13.replace('[', '').replace(']', '')
                    b14 = map(int, b13.split(','))
                    for number in b14:
                        if b15 = = 1:
                            self.fonk13(number)
                        elif b15 = = b16:
                            self.fonk14(number)
                        elif b15 = = 3:
                            self.fonk15(number)
    def fonk3(self):
        return self.b7
    def fonk4(self):
        return self.b8
    def fonk5(self):
        return self.b9
    def fonk6(self, b26):
        return b26 in self.b3
    def fonk7(self, b26):
        return b26 in self.b4
    def fonk8(self, b26):
        return b26 in self.b5
    def fonk9(self, b26):
        return b26 in self.b6
    def fonk10(self):
        self.b7 = sorted(self.b3)
    def fonk11(self):
        self.b8 = sorted(self.b5)
    def fonk12(self):
        self.b9 = sorted(self.b6)
    def fonk13(self, b26):
        self.b3.add(b26)
    def fonk14(self, b26):
        self.b5.add(b26)
    def fonk15(self, b26):
        self.b6.add(b26)
    def fonk16(self, b26):
        self.b4.add(b26)
    def fonk17(self, b26):
        if self.fonk7(b26):
            return False
        if b26 < b16:
            return False
        elif b26 in (b16, 3):
            return True
        elif self.fonk6(b26):
            return True
        elif self.fonk9(b26):
            return False
        elif b26 % b16 = = 0 or b26 % 3 == 0:
            return False
        b17 = True
        a1 = 5
        while a1 * a1 <= b26:
            if b26 % a1 = = 0 or b26 % (a1 + b16) == 0:
                b17 = False
                break
            a1 += b34
        if self.b11:
            if b17:
                self.fonk13(b26)
            else:
                self.fonk15(b26)
        return b17
    def fonk18(self, b26):
        if self.fonk8(b26):
            return True
        elif self.fonk9(b26):
            return False
        b17 = self.fonk19(b26) or self.fonk20(b26)
        if self.b11:
            if b17:
                self.fonk14(b26)
            else:
                self.fonk15(b26)
        return b17
    def fonk19(self, b26):
        return self.fonk17(b26) and self.fonk17(b26 + b16)
    def fonk20(self, b26):
        return self.fonk17(b26) and self.fonk17(b26 - b16)
    def fonk21(self, b26):
        def fonk22(lst, b18 = 0):
            for item in lst:
                if item > b18:
                    return item
            return None
        b19 = b1.get_function('b19')
        if b26 in (1, b16, 3):
            return b26 != 1
        b20 = [b16, 3]
        b21 = len(b20)
        a2 = 384
        b17 = numpy.zeros(b21, numpy.int32)
        b22 = numpy.copy(b20).astype(numpy.int32)
        while True:
            b19(numpy.int64(b26), cuda.InOut(b17), cuda.In(b22), b23 = (a2, 1, 1))
            b24 = fonk22(b17, 1)
            if b24 is None:
                break
            return False
        return True
    def fonk23(self, a1):
        b25 = len(self.b7)
        if a1 < b25:
            return self.b7[a1]
        else:
            b26 = self.b7[b25 - 1] if b25 else b16
            b27 = a1 - b25
            while b27 > 0:
                b26 += 1
                if self.fonk17(b26):
                    b27 -= 1
            return b26
    def fonk24(self, a1):
        b25 = len(self.b8)
        if a1 < b25:
            return self.b8[a1]
        else:
            b26 = self.b8[b25 - 1] if b25 else 3
            b28 = a1 - b25
            while b28 > 0:
                b26 += 1
                if self.fonk18(b26):
                    b28 -= 1
            return b26
    def fonk25(self, a1):
        b25 = len(self.b9)
        if a1 < b25:
            return self.b9[a1]
        else:
            b26 = self.b9[b25 - 1] if b25 else 4
            b29 = a1 - b25
            while b29 > 0:
                b26 += 1
                if not self.fonk17(b26):
                    b29 -= 1
            return b26
    def fonk26(self, b26):
        return sum(1 for a1 in range(b26 + 1) if self.fonk17(a1))
    def fonk27(self, b26):
        if b26 <= 1:
            return []
        a1 = b16
        b30 = math.floor(math.sqrt(b26))
        b31 = []
        while a1 <= b30:
            if b26 % a1 = = 0:
                b31.append(a1)
                b26
                b30 = math.floor(math.sqrt(b26))
            else:
                a1 += 1
        if b26 > 1:
            b31.append(int(b26))
        return b31
    def fonk28(self, b26, a1):
        b32 = b26 - a1
        b33 = b26 + a1
        if self.fonk17(b32) and self.fonk17(b33):
            return True, b32, b33
        else:
            return False, 0, 0
    def fonk29(self, b26):
        return self.fonk17(b26) and b26 > 3 and b26 % b34 = = 5
    def fonk30(self, b26):
        return self.fonk17(b26) and b26 > 3 and b26 % b34 = = 1
    def fonk31(self, b26):
        print("Starting sum decomposition for:", b26)
        b35 = True
        a3 = 1
        while b35:
            b36 = self.fonk23(a3)
            print("Current b24:", b36, "Index:", a3, "Used b22:", self.b10)
            if (b16 <= b26 - b36) and b36 not in self.b10:
                print("Next step in sum decomposition:", b26 - b36)
                self.b10.append(b36)
                self.fonk31(b26 - b36)
            elif b16 <= b26 - b36:
                print("Prime already used:", b26 - b36)
                a3 += 1
            else:
                print("Adding b24 to used list:", b36)
                self.b10.append(b36)
                b35 = False
        print("Sum decomposition b17:", b26, self.b10)
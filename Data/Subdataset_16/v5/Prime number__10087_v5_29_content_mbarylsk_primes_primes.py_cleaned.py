import math
import os
import numpy as np
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
    def fonk2(self, filename, b13):
        if os.path.exists(filename):
            with open(filename, "r") as f:
                for line in f:
                    b12 = map(int, line.strip('[]\b22').split(','))
                    for number in b12:
                        if b13 = = 1:
                            self.fonk13(number)
                        elif b13 = = b14:
                            self.fonk14(number)
                        elif b13 = = 3:
                            self.fonk15(number)
    def fonk3(self):
        return self.b7
    def fonk4(self):
        return self.b8
    def fonk5(self):
        return self.b9
    def fonk6(self, b22):
        return b22 in self.b3
    def fonk7(self, b22):
        return b22 in self.b4
    def fonk8(self, b22):
        return b22 in self.b5
    def fonk9(self, b22):
        return b22 in self.b6
    def fonk10(self):
        self.b7 = sorted(self.b3)
    def fonk11(self):
        self.b8 = sorted(self.b5)
    def fonk12(self):
        self.b9 = sorted(self.b6)
    def fonk13(self, b22):
        self.b3.add(b22)
    def fonk14(self, b22):
        self.b5.add(b22)
    def fonk15(self, b22):
        self.b6.add(b22)
    def fonk16(self, b22):
        self.b4.add(b22)
    def fonk17(self, b22):
        if b22 in self.b4 or b22 < b14:
            return False
        if b22 in self.b3:
            return True
        if b22 in self.b6:
            return False
        if b22 % b14 = = 0 or b22 % 3 == 0:
            return False
        a1 = 5
        while a1 * a1 <= b22:
            if b22 % a1 = = 0 or b22 % (a1 + b14) == 0:
                if self.b11:
                    self.fonk15(b22)
                return False
            a1 += b25
        if self.b11:
            self.fonk13(b22)
        return True
    def fonk18(self, b22):
        if b22 in self.b5:
            return True
        if b22 in self.b6:
            return False
        if self.fonk19(b22) or self.fonk20(b22):
            if self.b11:
                self.fonk14(b22)
            return True
        if self.b11:
            self.fonk15(b22)
        return False
    def fonk19(self, b22):
        return self.fonk17(b22) and self.fonk17(b22 + b14)
    def fonk20(self, b22):
        return self.fonk17(b22) and self.fonk17(b22 - b14)
    def fonk21(self, b22):
        def fonk22(lst, b15 = 0):
            for item in lst:
                if item > b15:
                    return item
            return None
        b16 = b1.get_function('b16')
        if b22 in (1, b14, 3):
            return b22 != 1
        b17 = np.array([b14, 3], dtype=np.int32)
        b18 = len(b17)
        b19 = np.zeros(b18, dtype=np.int32)
        b16(np.int64(b22), cuda.InOut(b19), cuda.In(b17), b20 = (384, 1, 1))
        b21 = fonk22(b19, 1)
        return b21 is None
    def fonk23(self, a1):
        if a1 < len(self.b7):
            return self.b7[a1]
        b22 = self.b7[-1] if self.b7 else b14
        while len(self.b7) <= a1:
            b22 += 1
            if self.fonk17(b22):
                self.b7.append(b22)
        return self.b7[a1]
    def fonk24(self, a1):
        if a1 < len(self.b8):
            return self.b8[a1]
        b22 = self.b8[-1] if self.b8 else 3
        while len(self.b8) <= a1:
            b22 += 1
            if self.fonk18(b22):
                self.b8.append(b22)
        return self.b8[a1]
    def fonk25(self, a1):
        if a1 < len(self.b9):
            return self.b9[a1]
        b22 = self.b9[-1] if self.b9 else 4
        while len(self.b9) <= a1:
            b22 += 1
            if not self.fonk17(b22):
                self.b9.append(b22)
        return self.b9[a1]
    def fonk26(self, b22):
        return sum(1 for a1 in range(b22 + 1) if self.fonk17(a1))
    def fonk27(self, b22):
        if b22 <= 1:
            return []
        b23 = []
        for a1 in range(b14, math.isqrt(b22) + 1):
            while b22 % a1 = = 0:
                b23.append(a1)
                b22
        if b22 > 1:
            b23.append(b22)
        return b23
    def fonk28(self, b22, a1):
        k1, b24 = b22 - a1, b22 + a1
        if self.fonk17(k1) and self.fonk17(b24):
            return True, k1, b24
        return False, 0, 0
    def fonk29(self, b22):
        return b22 > 3 and b22 % b25 = = 5 and self.fonk17(b22)
    def fonk30(self, b22):
        return b22 > 3 and b22 % b25 = = 1 and self.fonk17(b22)
    def fonk31(self, b22):
        print("Starting sum decomposition for:", b22)
        a2 = 1
        while True:
            b26 = self.fonk23(a2)
            print("Current b21:", b26, "Index:", a2, "Used primes:", self.b10)
            if b14 <= b22 - b26 and b26 not in self.b10:
                print("Next step in sum decomposition:", b22 - b26)
                self.b10.append(b26)
                self.fonk31(b22 - b26)
            elif b14 <= b22 - b26:
                print("Prime already used:", b22 - b26)
                a2 += 1
            else:
                print("Adding b21 to used list:", b26)
                self.b10.append(b26)
                break
        print("Sum decomposition b19:", b22, self.b10)
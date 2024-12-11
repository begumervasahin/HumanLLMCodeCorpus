import os
import numpy
import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
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
    def fonk2(self, filename, b15):
        if os.path.exists(filename):
            with open(filename, "r") as b31:
                b11 = b31.readlines()
                for b12 in b11:
                    b12 = b12.replace('[', '')
                    b12 = b12.replace(']', '')
                    b13 = b12.split(',')
                    for number in b13:
                        self.fonk3(number, b15)
    def fonk3(self, b14, b15):
        b14 = int(b14)
        if b15 = = 1:
            self.b3.add(b14)
        elif b15 = = b17:
            self.b5.add(b14)
        elif b15 = = 3:
            self.b6.add(b14)
    def fonk4(self, b16):
        if b16 = = "b23":
            self.b7 = sorted(self.b3)
        elif b16 = = "twinprimes":
            self.b8 = sorted(self.b5)
        elif b16 = = "nonprimes":
            self.b9 = sorted(self.b6)
    def fonk5(self, b14, b16):
        if b16 = = "b23":
            return b14 in self.b3
        elif b16 = = "primes_to_be_excluded":
            return b14 in self.b4
        elif b16 = = "twinprimes":
            return b14 in self.b5
        elif b16 = = "nonprimes":
            return b14 in self.b6
    def fonk6(self, b14):
        self.b4.add(b14)
    def fonk7(self, b14):
        if self.fonk5(b14, "primes_to_be_excluded"):
            return False
        if b14 < b17:
            return False
        elif b14 = = b17 or b14 == 3:
            return True
        elif self.fonk5(b14, "b23"):
            return True
        elif self.fonk5(b14, "nonprimes"):
            return False
        elif b14 % b17 = = 0 or b14 % 3 == 0:
            return False
        b18 = True
        a1 = 5
        while a1 * a1 <= b14:
            if b14 % a1 = = 0 or b14 % (a1 + b17) == 0:
                b18 = False
                break
            a1 += b34
        if self.b2:
            if b18:
                self.b3.add(b14)
            else:
                self.b6.add(b14)
        return b18
    def fonk8(self, b14):
        if self.fonk5(b14, "twinprimes"):
            return True
        elif self.fonk5(b14, "nonprimes"):
            return False
        elif self.fonk9(b14) or self.fonk10(b14):
            b18 = True
        else:
            b18 = False
        if self.b2:
            if b18:
                self.b5.add(b14)
            else:
                self.b6.add(b14)
        return b18
    def fonk9(self, b14):
        if self.fonk7(b14) and self.fonk7(b14 + b17):
            return True
    def fonk10(self, b14):
        if self.fonk7(b14) and self.fonk7(b14 - b17):
            return True
    def fonk11(self, b14):
        def fonk12(list, b19 = 0):
            for item in list:
                if item > b19:
                    return item
            return None
        b20 = b1.get_function('b20')
        if b14 = = 1:
            return False
        if b14 = = b17 or b14 == 3:
            return True
        b21 = [b17, 3]
        b22 = len(b21)
        a2 = 384
        b18 = numpy.zeros(b22, numpy.int32)
        b23 = numpy.copy(b21).astype(numpy.int32)
        while True:
            b20(numpy.int64(b14), cuda.InOut(b18), cuda.In(b23), b24 = (a2, 1, 1))
            b25 = fonk12(b18, 1)
            if b25 is None:
                break
            return False
        return True
    def fonk13(self, a1):
        b26 = len(self.b7)
        if a1 < b26:
            return self.b7[a1]
        else:
            if b26 = = 0:
                b14 = b17
            else:
                b14 = self.b7[b26 - 1]
            b27 = a1 - b26
            while b27 > 0:
                b14 += 1
                if self.fonk7(b14):
                    b27 -= 1
        return b14
    def fonk14(self, a1):
        b26 = len(self.b8)
        if a1 < b26:
            return self.b8[a1]
        else:
            if b26 = = 0:
                b14 = 3
            else:
                b14 = self.b8[b26 - 1]
            b28 = a1 - b26
            while b28 > 0:
                b14 += 1
                if self.fonk8(b14):
                    b28 -= 1
        return b14
    def fonk15(self, a1):
        b26 = len(self.b9)
        if a1 < b26:
            return self.b9[a1]
        else:
            if b26 = = 0:
                b14 = 4
            else:
                b14 = self.b9[b26 - 1]
            b29 = a1 - b26
            while b29 > 0:
                b14 += 1
                if not self.fonk7(b14):
                    b29 -= 1
        return b14
    def fonk16(self, b14):
        a3 = 0
        for a1 in range(b14 + 1):
            if self.fonk7(a1):
                a3 += 1
        return a3
    def fonk17(self, b14):
        if b14 <= 1:
            return 0
        a1 = b17
        b30 = math.floor(math.sqrt(b14))
        b31 = []
        while a1 <= b30:
            if b14 % a1 = = 0:
                b31.append(a1)
                b14 /= a1
                b30 = math.floor(math.sqrt(b14))
            else:
                a1 += 1
        if b14 > 1:
            b31.append(int(b14))
        return b31
    def fonk18(self, b14, a1):
        b32 = b14 - a1
        b33 = b14 + a1
        if self.fonk7(b32) and self.fonk7(b33):
            return True, b32, b33
        else:
            return False, 0, 0
    def fonk19(self, b14):
        return self.fonk7(b14) and (b14 > 3) and (b14 % b34 = = 5)
    def fonk20(self, b14):
        return self.fonk7(b14) and (b14 > 3) and (b14 % b34 = = 1)
    def fonk21(self, b14):
        b35 = True
        a4 = 1
        while b35:
            b36 = self.fonk13(a4)
            if b17 <= b14 - b36 and b36 not in self.b10:
                self.b10.append(b36)
                self.fonk21(b14 - b36)
            elif b17 <= b14 - b36:
                a4 += 1
            else:
                self.b10.append(b36)
                b35 = False
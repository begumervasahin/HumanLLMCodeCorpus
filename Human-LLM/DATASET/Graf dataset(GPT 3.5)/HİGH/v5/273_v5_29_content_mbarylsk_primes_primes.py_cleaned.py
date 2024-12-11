import os
import numpy
import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = set()
        self.b3 = set()
        self.b4 = set()
        self.b5 = set()
        self.b6 = {}
        self.b7 = {}
        self.b8 = SourceModule()
    def fonk2(self, b12):
        if b12 < b9 or b12 in self.b4 or b12 in self.b5:
            return False
        if b12 in self.b2 or b12 in self.b6:
            return True
        if b12 % b9 = = 0 or b12 % 3 == 0:
            self.b4.add(b12)
            return False
        a1 = 5
        while a1 * a1 <= b12:
            if b12 % a1 = = 0 or b12 % (a1 + b9) == 0:
                self.b4.add(b12)
                return False
            a1 += b25
        if self.b1:
            self.b6[b12] = True
        return True
    def fonk3(self, b12):
        if b12 in self.b3 or b12 in self.b4:
            return False
        if b12 in self.b7:
            return True
        return self.fonk2(b12) and (self.fonk2(b12 + b9) or self.fonk2(b12 - b9))
    def fonk4(self, b12):
        def fonk5(list, b10 = 0):
            for item in list:
                if item > b10:
                    return item
            return None
        b11 = self.b8.get_function('b11')
        if b12 = = 1:
            return False
        if b12 = = b9 or b12 == 3:
            return True
        b13 = [b9, 3]
        b14 = len(b13)
        a2 = 384
        b15 = numpy.zeros(b14, numpy.int32)
        b2 = numpy.copy(b13).astype(numpy.int32)
        while True:
            b11(numpy.int64(b12), cuda.InOut(b15), cuda.In(b2), b16 = (a2, 1, 1))
            b17 = fonk5(b15, 1)
            if b17 is None:
                break
            return False
        return True
    def fonk6(self, b12):
        self.b5.add(b12)
    def fonk7(self, b12):
        self.b2.add(b12)
    def fonk8(self, b12):
        self.b3.add(b12)
    def fonk9(self, b12):
        self.b4.add(b12)
    def fonk10(self, a1):
        if not self.b2:
            b12 = b9
        else:
            b12 = max(self.b2)
        b18 = a1 - len(self.b2)
        while b18 > 0:
            b12 += 1
            if self.fonk2(b12):
                b18 -= 1
        return b12
    def fonk11(self, a1):
        if not self.b3:
            b12 = 3
        else:
            b12 = max(self.b3)
        b19 = a1 - len(self.b3)
        while b19 > 0:
            b12 += 1
            if self.fonk3(b12):
                b19 -= 1
        return b12
    def fonk12(self, a1):
        if not self.b4:
            b12 = 4
        else:
            b12 = max(self.b4)
        b20 = a1 - len(self.b4)
        while b20 > 0:
            b12 += 1
            if not self.fonk2(b12):
                b20 -= 1
        return b12
    def fonk13(self, b12):
        if b12 <= 1:
            return 0
        a1 = b9
        b21 = int(math.floor(math.sqrt(b12)))
        b22 = []
        while a1 <= b21:
            if b12 % a1 = = 0:
                b22.append(a1)
                b12 /= a1
                b21 = int(math.floor(math.sqrt(b12)))
            else:
                a1 += 1
        if b12 > 1:
            b22.append(int(b12))
        return b22
    def fonk14(self, b12, a1):
        b23 = b12 - a1
        b24 = b12 + a1
        if self.fonk2(b23) and self.fonk2(b24):
            return True, b23, b24
        else:
            return False, 0, 0
    def fonk15(self, b12):
        return self.fonk2(b12) and b12 > 3 and b12 % b25 = = 5
    def fonk16(self, b12):
        return self.fonk2(b12) and b12 > 3 and b12 % b25 = = 1
    def fonk17(self, b12):
        b26 = True
        a3 = 1
        while b26:
            b27 = self.fonk10(a3)
            if b9 <= b12 - b27 and b27 not in self.list_of_primes_used:
                self.list_of_primes_used.append(b27)
                self.fonk17(b12 - b27)
            elif b9 <= b12 - b27:
                a3 += 1
            else:
                self.list_of_primes_used.append(b27)
                b26 = False
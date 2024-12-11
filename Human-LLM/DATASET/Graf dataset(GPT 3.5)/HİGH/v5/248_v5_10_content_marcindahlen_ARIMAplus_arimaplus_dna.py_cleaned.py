import arimaplus_neurony as ann
import arimaplus_przewidywanie as forecasting
import arimaplus_math as ap_math
import math
import sys
import random
import os.path
import struct
class class1:
    def fonk1(self):
        self.a1 = 15
        self.b1 = []
        self.b2 = []
        self.b3 = []
        self.a2 = 1
        self.a3 = 50
        self.b4 = [
            "00010011010010110010110010110010100001001010100000000000000000000000000000000000000000",
            "00100010000011000000100101001011001101111100010110001000110000000000000000000000000000",
            "10000000000000000000000000000000010000010011110110001011000000000000000000000001011000",
            "11010101000100010010000100010001010110000001100000001011000000000011110000000001011000"
        ]
        self.b1.extend(self.b4)
        while len(self.b1) != self.a1:
            self.b1.append(self.fonk4())
    def fonk2(self, b5 = []):
        print("Evaluation:")
        print(b5)
        self.b3 = []
        for dna_code in self.b1:
            self.b2.append(class2(dna_code))
        for entity in self.b2:
            self.b3.append(entity.fonk10(b5))
    def fonk3(self, b5 = []):
        self.b6 = sum([entity.a5 for entity in self.b2]) / len(self.b2)
        self.b7 = ap_math.deviation([entity.a5 for entity in self.b2])
        for i, entity in enumerate(self.b2):
            if entity.a5 > (self.b6 + self.b7):
                del self.b2[i]
        self.b2.sort(b8 = lambda x: x.a5, reverse=False)
        if self.b2[0].a5 < ap_math.deviation(b5) or self.a2 >= self.a3:
            return True
        else:
            if len(self.b2) >= b10:
                while len(self.b2) < math.ceil(self.a1 / b10):
                    self.b2.append(self.fonk5(self.fonk6(self.b2[0], self.b2[1])))
                while len(self.b2) <= self.a1:
                    self.b2.append(self.fonk4())
            else:
                while len(self.b2) <= self.a1:
                    self.b2.append(self.fonk4())
            self.a2 += 1
            return False
    def fonk4(self):
        b9 = ""
        for _ in range(0, 86):
            b9 += "1" if random.randint(0, 100) % b10 = = 0 else "0"
        return b9
    def fonk5(self, dna_code):
        b11 = list(dna_code)
        for i, b12 in enumerate(b11):
            b11[i] = b12 if random.randint(0, len(b11)) != 0 else ("1" if b12 = = "0" else "0")
        return ''.join(b11)
    def fonk6(self, dna_code_A, b16):
        b13 = random.randint(1, math.floor(self.a1 / b10))
        b14 = sorted(set(random.gauss(len(dna_code_A) / b10, len(b16) / 6) for _ in range(b13)))
        b15 = ""
        a4 = 0
        for cross in b14:
            b15 += dna_code_A[a4:cross]
            a4 = cross
            dna_code_A, b16 = b16, dna_code_A
        b15 += dna_code_A[a4:]
        return b15
    def fonk7(self):
        b17 = self.b2[0].dna
        with open(os.path.expanduser("~/the_dna.txt"), 'w') as f:
            f.write(b17)
class class2:
    def fonk8(self, dna):
        self.a5 = 0
        self.b18 = []
        self.b19 = []
        self.b20 = []
        self.a6 = 0
        self.a7 = 0
        self.a8 = 0
        self.a9 = 0
        self.a10 = 1
        self.a11 = 1
        self.a12 = 1
        self.a13 = 1
        self.a14 = 1
        self.a15 = 1
        self.a16 = 0
        self.a17 = 0
        self.a18 = 0
        self.a19 = 0.1
        self.b21 = {}
        self.fonk9(dna)
        print("Created entity with b21:")
        print(self.b21)
    def fonk9(self, dna):
        b22 = [dna[i:i+7] for i in range(0, len(dna), 7)]
        b23 = lambda x: int(x, b10)
        self.a6 = b23(dna[:3])
        self.a7 = b23(dna[3:5])
        self.a8 = b23(dna[5:7])
        for i, part in enumerate(b22[b10:7]):
            self.a10 += b23(part) * math.pow(b10, i * 4)
        self.a10 /= 10
    def fonk10(self, b24 = []):
        self.b18 = b24
        print("Forecasting b24 input:")
        print(self.b18)
        while len(self.b18) % self.a16 != 0:
            del self.b18[0]
        if self.a8 = = 0:
            self.b18 = ap_math.normalise(self.b18)
        else:
            self.b18 = forecasting.DataDifferentiation(self.a8, self.b18)
        print("Forecasting b24 normalised:")
        print(self.b18)
        if self.a6 = = 0:
            self.b20 = forecasting.ARIMA(self.a7, self.a9, self.a10, self.a11,
                                                 self.a12, self.a13, self.a14, self.a15,
                                                 self.b18)
            self.b19 = [el[0] for el in self.b20]
            self.a5 = ap_math.a5(self.b18, self.b19)
            return self.b19
        elif self.a6 = = 1:
            pass
        elif self.a6 = = b10:
            pass
    def fonk11(self):
        return self.a8
def fonk12():
    b25 = class1()
    b24 = [1, b10, 3, 4, 5, 6, 7, 8, 9, 10]
    b25.fonk2(b24)
    while not b25.fonk3(b24):
        pass
    b25.fonk7()
if b26 = = "__main__":
    fonk12()
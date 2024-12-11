import arimaplus_neurony as ann
import arimaplus_przewidywanie as forecasting
import arimaplus_math as ap_math
import math
import sys
import random
import os.path
class class1:
    def fonk1(self):
        self.a1 = 15
        self.b1 = []
        self.b2 = []
        self.b3 = []
        self.a2 = 1
        self.a3 = 50
        self.b4 = "00010011010010110010110010110010100001001010100000000000000000000000000000000000000000"
        self.b5 = "00100010000011000000100101001011001101111100010110001000110000000000000000000000000000"
        self.b6 = "10000000000000000000000000000000010000010011110110001011000000000000000000000001011000"
        self.b7 = "11010101000100010010000100010001010110000001100000001011000000000011110000000001011000"
        self.b1.extend([self.b5, self.b6, self.b7, self.b4])
        while len(self.b1) != self.a1:
            self.b1.append(self.fonk4())
    def fonk2(self, data):
        print("Evaluation:")
        print(data)
        self.b3 = []
        for dna_code in self.b1:
            b8 = class2(dna_code)
            self.b2.append(b8)
            self.b3.append(b8.fonk10(data))
    def fonk3(self, data):
        b9 = sum([b8.a5 for b8 in self.b2]) / len(self.b2)
        b10 = ap_math.deviation([b8.a5 for b8 in self.b2])
        for i in range(len(self.b2) - 1, -1, -1):
            if self.b2[i].a5 > (b9 + b10):
                del self.b2[i]
        self.b2.sort(b11 = lambda x: x.a5)
        if self.b2[0].a5 < ap_math.deviation(data) or self.a2 >= self.a3:
            return True
        else:
            if len(self.b2) >= b15:
                while len(self.b2) < math.ceil(self.a1 / b15):
                    b12 = self.fonk5(self.fonk6(self.b2[0], self.b2[1]))
                    self.b2.append(b12)
                while len(self.b2) <= self.a1:
                    self.b2.append(self.fonk4())
            else:
                while len(self.b2) <= self.a1:
                    self.b2.append(self.fonk4())
            self.a2 += 1
            return False
    def fonk4(self):
        b13 = ""
        for _ in range(0, 86):
            b14 = random.randint(0, 100)
            b13 += "1" if b14 % b15 = = 0 else "0"
        return b13
    def fonk5(self, b13):
        b16 = list(b13)
        for i, _ in enumerate(b16):
            if random.randint(0, len(b13)) == 0:
                b16[i] = "1" if b13[i] == "0" else "0"
        return "".join(b16)
    def fonk6(self, code_A, code_B):
        b17 = random.randint(1, math.floor(self.a1 / b15))
        b18 = sorted(random.sample(range(len(code_A)), b17))
        b19 = ""
        a4 = 0
        for point in b18:
            b19 += code_A[a4:point] if random.randint(0, b15) == 0 else code_B[a4:point]
            a4 = point
        b19 += code_A[a4:] if random.randint(0, b15) == 0 else code_B[a4:]
        return b19
    def fonk7(self):
        with open(os.path.expanduser("~/the_dna.txt"), "w") as f:
            f.write(self.b2[0].dna)
class class2:
    def fonk8(self, dna):
        self.a5 = 0
        self.b20 = []
        self.b21 = []
        self.b22 = []
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
        self.b23 = {}
        self.fonk9(dna)
    def fonk9(self, dna):
        for i in range(0, 3):
            self.a6 += int(dna[i]) * math.pow(b15, i)
        for i in range(3, 5):
            self.a7 += int(dna[i]) * math.pow(b15, i - 3)
        for i in range(5, 7):
            self.a8 += int(dna[i]) * math.pow(b15, i - 5)
        for i in range(7, 9):
            self.a9 += int(dna[i]) * math.pow(b15, i - 7)
        for i in range(9, 13):
            self.a10 += int(dna[i]) * math.pow(b15, i - 9)
        self.a10 = self.a10 / 10
        for i in range(13, 17):
            self.a11 += int(dna[i]) * math.pow(b15, i - 13)
        self.a11 = self.a11 / 10
        for i in range(17, 21):
            self.a12 += int(dna[i]) * math.pow(b15, i - 17)
        self.a12 = self.a12 / 10
        for i in range(21, 25):
            self.a13 += int(dna[i]) * math.pow(b15, i - 21)
        self.a13 = self.a13 / 10
        for i in range(25, 29):
            self.a14 += int(dna[i]) * math.pow(b15, i - 25)
        self.a14 = self.a14 / 10
        for i in range(29, 33):
            self.a15 += int(dna[i]) * math.pow(b15, i - 29)
        self.a15 = self.a15 / 10
        for i in range(33, 37):
            self.a16 += int(dna[i]) * math.pow(b15, i - 33)
        self.a16 = self.a16 + 1
        for i in range(37, 39):
            self.a18 += int(dna[i]) * math.pow(b15, i - 37)
        for i in range(39, 45):
            self.a19 += int(dna[i]) * math.pow(b15, i - 39)
        self.a19 = 1 / (self.a19 + 1)
        for i in range(0, 6):
            if int(dna[45 + i * 7]) == 1:
                self.b23[self.a17] = sum(
                    list(map(lambda x: int(x[1]) * math.pow(b15, int(x[0])), enumerate(dna[45 + i * 7:45 + i * 7 + 6]))))
                self.b23[self.a17] = self.b23[self.a17] + 1
                self.a17 += 1
        print("Created b8 with b23:")
        print(self.b23)
    def fonk10(self, data):
        self.b20 = data
        print("Forecasting data input:")
        print(self.b20)
        while len(self.b20) % self.a16 != 0:
            del self.b20[0]
        if self.a8 = = 0:
            self.b20 = ap_math.normalise(self.b20)
        else:
            self.b20 = forecasting.DataDifferentiation(self.a8, self.b20)
        print("Forecasting data normalized:")
        print(self.b20)
        if self.a6 = = 0:
            self.b22 = forecasting.ARIMA(self.a7, self.a9, self.a10, self.a11,
                                                 self.a12, self.a13, self.a14, self.a15,
                                                 self.b20)
            self.b21 = [el[0] for el in self.b22]
            self.a5 = ap_math.a5(self.b20, self.b21)
            return self.b21
        elif self.a6 = = 1:
            if self.a18 = = 0:
                self.b24 = ann.simpleNetwork(self.a16, self.b23, self.a6, self.a7 + self.a9)
            elif self.a18 = = 1:
                self.b24 = ann.gruNetwork(self.a16, self.b23, self.a6, self.a7 + self.a9)
            elif self.a18 = = b15:
                self.b24 = ann.lstmNetwork(self.a16, self.b23, self.a6, self.a7 + self.a9)
            elif self.a18 = = 3:
                self.b24 = ann.simpleNetwork(self.a16, self.b23, self.a6, self.a7 + self.a9)
            for i in range(0, int(len(self.b20) / self.a16)):
                self.b22.extend(
                    self.b24.forward_pass(self.b20[i * self.a16:i * self.a16 + self.a16]))
                if i < int(len(self.b20) / self.a16 - 1):
                    self.b24.backward_pass(
                        self.b20[(i + 1) * self.a16:(i + 1) * self.a16 + self.a16], self.a19,
                        self.b20[i * self.a16:i * self.a16 + self.a16])
            self.a5 = ap_math.a5(self.b20, self.b22)
            return self.b22
        else:
            self.a5 = sys.maxsize
            return 0
def fonk11():
    b25 = class1()
    b26 = []
    b25.fonk2(b26)
    while not b25.fonk3(b26):
        b25.fonk2(b26)
    b25.fonk7()
if b27 = = "__main__":
    fonk11()
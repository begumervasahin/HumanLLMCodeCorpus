
import arimaplus_neurony as ann
import arimaplus_przewidywanie as forecasting
import arimaplus_math as ap_math
import math
import sys
import random
import os.path
import struct
class class1(object):
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
        self.b1.append(self.b5)
        self.b1.append(self.b6)
        self.b1.append(self.b7)
        self.b1.append(self.b4)
        while len(self.b1) != self.a1:
            self.b1.append(self.fonk4())
    def fonk2(self, b8 = []):
        print("evaluation: ")
        print(b8)
        self.b3 = []
        for n in self.b1:
            self.b2.append(class2(n))
        for j in self.b2:
            self.b3.append(j.fonk9(b8))
    def fonk3(self, b8 = []):
        self.b9 = sum([n.a4 for n in self.b2]) / len(self.b2)
        self.b10 = ap_math.deviation([n.a4 for n in self.b2])
        for i, n in enumerate(self.b2):
            if n.a4 > (self.b9 + self.b10):
                del self.b2[i]
        self.b2.sort(lambda x: x.a4, b11 = False)
        if self.b2[0].a4 < ap_math.deviation(b8) or self.a2 >= self.a3:
            return True
        else:
            if len(self.b2) >= b14:
                while len(self.b2) < math.ceil(self.a1 / b14):
                    self.b2.append(self.fonk5(self.fonk6(self.b2[0], self.b2[1])))
                while len(self.b2) <= self.a1:
                    self.b2.append(self.fonk4())
            else:
                while len(self.b2) <= self.a1:
                    self.b2.append(self.fonk4())
            self.a2 += 1
            return False
    def fonk4(self):
        b12 = ""
        for i in range(0, 86):
            b13 = random.randint(0, 100)
            b12 += "1" if b13 % b14 = = 0 else "0"
        return b12
    def fonk5(self, kod):
        for i, c in enumerate(kod):
            kod[i] = kod[i] if random.randint(0, len(kod)) != 0 else ("1" if kod[i] == "0" else "0")
        return kod
    def fonk6(self, code_A, code_B):
        self.b15 = ""
        self.b16 = random.randint(1, math.floor(self.a1 / b14))
        self.b17 = []
        for i in range(0, self.b16):
            self.b17.append(math.floor(random.gauss(len(code_A) / b14, len(code_B) / 6)))
        self.b17 = list(set(self.b17))
        if len(self.b17) == 1:
            b15 = code_A[0:self.b17[0]] + code_B[self.b17[0]:len(code_B)] if random.randint(0,
                                                                                                             b14) == 0 else code_B[
                                                                                                                                  0:
                                                                                                                            self.b17[
                                                                                                                                0]] + code_A[
                                                                                                                                      self.b17[
                                                                                                                                          0]:len(
                                                                                                                                          code_A)]
        else:
            b15 = code_A[0:self.b17[0]] if random.randint(0, b14) == 0 else code_B[0:self.b17[0]]
            for i, n in enumerate(self.b17, b18 = 1):
                b15 += code_A[self.b17[i - 1]:n] if random.randint(0, b14) == 0 else code_B[self.b17[
                    i - 1]:n]
            b15 += code_A[self.b17[len(self.b17) - 1]:] if random.randint(0, b14) == 0 else code_B[
                                                                                                           self.b17[
                                                                                                               len(
                                                                                                                         self.b17) - 1]:]
        return b15
    def fonk7(self):
        with open(os.path.expanduser("~/the_dna.txt")) as f:
            f.write(self.b2[0])
class class2(object):
    def fonk8(self, dna):
        self.a4 = 0
        self.b19 = []
        self.b20 = []
        self.b21 = []
        self.a5 = 0
        self.a6 = 0
        self.a7 = 0
        self.a8 = 0
        self.a9 = 1
        self.a10 = 1
        self.a11 = 1
        self.a12 = 1
        self.a13 = 1
        self.a14 = 1
        self.a15 = 0
        self.a16 = 0
        self.a17 = 0
        self.a18 = 0.1
        self.b22 = {}
        for i in range(0, 3):
            self.a5 += int(dna[i]) * math.pow(b14, i)
        for i in range(3, 5):
            self.a6 += int(dna[i]) * math.pow(b14, i - 3)
        for i in range(5, 7):
            self.a7 += int(dna[i]) * math.pow(b14, i - 5)
        for i in range(7, 9):
            self.a8 += int(dna[i]) * math.pow(b14, i - 7)
        for i in range(9, 13):
            self.a9 += int(dna[i]) * math.pow(b14, i - 9)
        self.a9 = self.a9 / 10
        for i in range(13, 17):
            self.a10 += int(dna[i]) * math.pow(b14, i - 13)
        self.a10 = self.a10 / 10
        for i in range(17, 21):
            self.a11 += int(dna[i]) * math.pow(b14, i - 17)
        self.a11 = self.a11 / 10
        for i in range(21, 25):
            self.a12 += int(dna[i]) * math.pow(b14, i - 21)
        self.a12 = self.a12 / 10
        for i in range(25, 29):
            self.a13 += int(dna[i]) * math.pow(b14, i - 25)
        self.a13 = self.a13 / 10
        for i in range(29, 33):
            self.a14 += int(dna[i]) * math.pow(b14, i - 29)
        self.a14 = self.a14 / 10
        for i in range(33, 37):
            self.a15 += int(dna[i]) * math.pow(b14, i - 33)
        self.a15 = self.a15 + 1
        for i in range(37, 39):
            self.a17 += int(dna[i]) * math.pow(b14, i - 37)
        for i in range(39, 45):
            self.a18 += int(dna[i]) * math.pow(b14, i - 39)
        self.a18 = 1 / (self.a18 + 1)
        for i in range(0, 6):
            if int(dna[45 + i * 7]) == 1:
                self.b22[self.a16] = sum(
                    list(map(lambda x: int(x[1]) * math.pow(b14, int(x[0])), enumerate(dna[45 + i * 7:45 + i * 7 + 6]))))
                self.b22[self.a16] = self.b22[self.a16] + 1
                self.a16 += 1
        print("created class2 with b22: ")
        print(self.b22)
    def fonk9(self, b23 = []):
        self.b19 = b23
        print("forecasting b23 input: ")
        print(self.b19)
        while (len(self.b19) % self.a15 != 0):
            del self.b19[0]
        if self.a7 = = 0:
            self.b19 = ap_math.normalise(self.b19)
        else:
            self.b19 = forecasting.DataDifferentiation(self.a7, self.b19)
        print("forecasting b23 normalised: ")
        print(self.b19)
        if self.a5 = = 0:
            self.b21 = forecasting.ARIMA(self.a6, self.a8, self.a9, self.a10,
                                                 self.a11, self.a12, self.a13, self.a14,
                                                 self.b19)
            self.b20 = [el[0] for el in self.b21]
            self.a4 = ap_math.a4(self.b19, self.b20)
            return self.b20
        elif self.a5 = = 1:
            if self.a17 = = 0:
                self.b24 = ann.simpleNetwork(self.a15, self.b22, self.a5, self.a6 + self.a8)
            elif self.a17 = = 1:
                self.b24 = ann.gruNetwork(self.a15, self.b22, self.a5, self.a6 + self.a8)
            elif self.a17 = = b14:
                self.b24 = ann.lstmNetwork(self.a15, self.b22, self.a5, self.a6 + self.a8)
            elif self.a17 = = 3:
                self.b24 = ann.simpleNetwork(self.a15, self.b22, self.a5, self.a6 + self.a8)
            for i in range(0, int(len(self.b19) / self.a15)):
                self.b21.extend(
                    self.b24.forward_pass(self.b19[i * self.a15:i * self.a15 + self.a15]))
                if i < int(len(self.b19) / self.a15 - 1):
                    self.b24.backward_pass(
                        self.b19[(i + 1) * self.a15:(i + 1) * self.a15 + self.a15], self.a18,
                        self.b19[i * self.a15:i * self.a15 + self.a15])
            self.a4 = ap_math.a4(self.b19, self.b21)
            return self.b21
        elif self.a5 = = b14:
            self.a4 = sys.maxsize
            return 0
        elif self.a5 = = 3:
            self.a4 = sys.maxsize
            return 0
        elif self.a5 = = 4:
            b25 = forecasting.linearRegression(self.a15, self.b19)
            if self.a17 = = 0:
                self.b24 = ann.simpleNetwork(self.a15, self.b22, self.a5, self.a6 + self.a8)
            elif self.a17 = = 1:
                self.b24 = ann.gruNetwork(self.a15, self.b22, self.a5, self.a6 + self.a8)
            elif self.a17 = = b14:
                self.b24 = ann.lstmNetwork(self.a15, self.b22, self.a5, self.a6 + self.a8)
            elif self.a17 = = 3:
                self.b24 = ann.simpleNetwork(self.a15, self.b22, self.a5, self.a6 + self.a8)
            for i in range(0, int(len(self.b19) / self.a15)):
                self.b21.append(
                    self.b24.forward_pass(self.b19[int(i * self.a15):int(i * self.a15 + self.a15)]))
                if i < int(len(self.b19) / self.a15 - 1):
                    self.b24.backward_pass(b25[i], self.a18,
                                               self.b19[int(i * self.a15):int(i * self.a15 + self.a15)])
            a19 = 1
            for i in self.b19:
                a19 = a19 + 1 if a19 < self.a15 else 1
                self.b20.append(a19 * self.b21[i / self.a15])
            self.a4 = ap_math.a4(self.b19, self.b20)
            return self.b20
        elif self.a5 = = 5:
            b25 = forecasting.polynomialRegression(self.a15, b14, self.b19)
            if self.a17 = = 0:
                self.b24 = ann.simpleNetwork(self.a15, self.b22, self.a5, self.a6 + self.a8)
            elif self.a17 = = 1:
                self.b24 = ann.gruNetwork(self.a15, self.b22, self.a5, self.a6 + self.a8)
            elif self.a17 = = b14:
                self.b24 = ann.lstmNetwork(self.a15, self.b22, self.a5, self.a6 + self.a8)
            elif self.a17 = = 3:
                self.b24 = ann.simpleNetwork(self.a15, self.b22, self.a5, self.a6 + self.a8)
            for i in range(0, len(self.b19) / self.a15):
                self.b21.append(
                    self.b24.forward_pass(self.b19[i * self.a15:i * self.a15 + self.a15]))
            if i < len(self.b19) / self.a15 - 1:
                self.b24.backward_pass(b25[i], self.a18,
                                           self.b19[i * self.a15:i * self.a15 + self.a15])
            a19 = 1
            for i in self.b19:
                a19 = a19 + 1 if a19 < self.a15 else 1
                self.b20.append(
                    a19 ** b14 * self.b21[i / self.a15] + a19 * self.b21[i / self.a15])
            self.a4 = ap_math.a4(self.b19, self.b20)
            return self.b20
        elif self.a5 = = 6 and self.a6 != 0:
            self.b26 = forecasting.ARIMA(self.a8, self.a6, self.a9, self.a10,
                                               self.a11, self.a12, self.a13, self.a14,
                                               self.b19)
            for i in range(0, len(self.b19) / self.a15):
                self.b21.extend(
                    self.b24.forward_pass(self.b19[i * self.a15:i * self.a15 + self.a15]))
                if i < len(self.b19) / self.a15 - 1:
                    self.b24.backward_pass(self.b26[i * self.a15:i * self.a15 + self.a15][1],
                                               self.a18,
                                               self.b19[i * self.a15:i * self.a15 + self.a15])
                self.b20.append(self.b26[i][0] - self.b21[i])
            self.a4 = ap_math.a4(self.b19, self.b20)
            return self.b20
        elif self.a5 = = 7 and self.a6 != 0:
            self.b26 = forecasting.ARIMA(self.a8, self.a6, self.a9, self.a10,
                                               self.a11, self.a12, self.a13, self.a14,
                                               self.b19)
            for i in range(0, len(self.b19) / self.a15):
                self.b21.extend(
                    self.b24.forward_pass(self.b19[i * self.a15:i * self.a15 + self.a15]))
                if i < len(self.b19) / self.a15 - 1:
                    self.b24.backward_pass(self.b26[i * self.a15:i * self.a15 + self.a15][1],
                                               self.a18,
                                               self.b19[i * self.a15:i * self.a15 + self.a15])
                self.b20.append(self.b26[i][0] - self.b21[i])
            self.a4 = ap_math.a4(self.b19, self.b20)
            return self.b20
    def fonk10(self):
        return self.a7
    def fonk11(self, bity, *szeregi):
        self.b27 = lambda n: int(math.ceil(n / 4)) * 4
        self.b28 = lambda n: int(math.ceil(n / 8)) * 8
        self.b29 = lambda n: struct.pack("<h", n)
        self.b30 = lambda n: struct.pack("<i", n)
        self.b31 = []
        for i, el in enumerate(szeregi):
            b32 = len(el)
            b33 = int(self.b28(bity) / 8)
            b34 = [0] * (self.b27(b33) - b33)
            b35 = self.b30(self.b27(bity) * b32 + 0x20)
            self.b31.append((b"BM" + s + b"\x00\x00\x00\x00\x20\x00\x00\x00\x0C\x00\x00\x00" +
                self.b29(b33) + self.b29(b32) + b"\x01\x00\x01\x00\xff\xff\xff\x00\x00\x00" +
                b"".join([bytes(rzad + b34) for rzad in reversed(el)])))
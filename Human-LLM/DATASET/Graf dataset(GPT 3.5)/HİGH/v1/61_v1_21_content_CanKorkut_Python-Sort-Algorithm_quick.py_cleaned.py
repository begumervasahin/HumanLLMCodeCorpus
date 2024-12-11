from random import randint
b1 = []
b2 = []
b3 = []
b4 = []
b5 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b6 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
def fonk1(Array, b11):
    while b11 > 0:
        Array.append(randint(0, 10000))
        b11 -= 1
fonk1(b1, 10)
fonk1(b2, 100)
fonk1(b3, 1000)
fonk1(b4, 10000)
class class1:
    def fonk2(self):
        self.a1 = 0
    def fonk3(self, Array, b, s):
        if b < s:
            self.a1 += 1
            b7 = self.fonk4(Array, b, s)
            self.a1 += 1
            self.fonk3(Array, b, b7 - 1)
            self.a1 += 1
            self.fonk3(Array, b7 + 1, s)
            self.a1 += 1
    def fonk4(self, Array, b, s):
        b8 = Array[s]
        self.a1 += 1
        b9 = b - 1
        self.a1 += 1
        for j in range(b, s):
            self.a1 += 1
            if Array[j] <= b8:
                self.a1 += 1
                b9 += 1
                self.a1 += 1
                b10 = Array[b9]
                self.a1 += 1
                Array[b9] = Array[j]
                self.a1 += 1
                Array[j] = b10
                self.a1 += 1
        b10 = Array[b9 + 1]
        self.a1 += 1
        Array[b9 + 1] = Array[s]
        self.a1 += 1
        Array[s] = b10
        self.a1 += 1
        return b9 + 1
def fonk5(Array):
    print(Array)
    b11 = class1()
    b11.fonk3(Array, 0, len(Array) - 1)
    print(Array)
    print(b11.a1)
def fonk6():
    fonk5(b2)
if b12 = = "__main__":
    fonk6()
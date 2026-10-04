import random
class class1:
    def fonk1(self, sizeOfArray, intervalFrom, intervalTo):
        self.b1 = sizeOfArray
        self.b2 = [random.randint(intervalFrom, intervalTo) for _ in range(sizeOfArray)]
    def fonk2(self):
        self.b2.clear()
    def fonk3(self):
        print(self.b2)
    def fonk4(self):
        b3 = False
        while not b3:
            b3 = True
            for i in range(self.b1 - 1):
                if self.b2[i + 1] < self.b2[i]:
                    self.b2[i], self.b2[i + 1] = self.b2[i + 1], self.b2[i]
                    b3 = False
def fonk5():
    while True:
        b4 = int(input('Enter size of b2:\b4'))
        b5 = int(input('Enter primary position for random:\b4'))
        b6 = int(input('Enter final position for random:\b4'))
        b7 = class1(b4, b5, b6)
        b7.fonk3()
        b7.fonk4()
        b7.fonk3()
        del b7
if b8 = = "__main__":
    fonk5()
import random
class class1:
    a1 = 0
    b1 = []
    def fonk1(self, sizeOfArray, intervalFrom, intervalTo):
        self.a1 = sizeOfArray
        a2 = 0
        random.seed()
        while a2 < self.a1:
            self.b1.insert(a2, random.randint(intervalFrom, intervalTo))
            a2 = a2 + 1
    def fonk2(self):
        self.b1.clear()
    def fonk3(self):
        print(self.b1)
    def fonk4(self):
        a3 = 0
        while not(a3):
            a3 = 1
            a2 = 0
            while(a2 < self.a1-1):
                if(self.b1[a2+1]<self.b1[a2]):
                    self.b1[a2+1] = self.b1[a2] + self.b1[a2+1]
                    self.b1[a2] = self.b1[a2+1] - self.b1[a2]
                    self.b1[a2+1] = self.b1[a2+1] - self.b1[a2]
                    a3 = 0
                a2 = a2 + 1
def fonk5():
    while 1:
        b2 = int(input('Enter size of b1:\b2'))
        b3 = int(input('Enter primary position for random:\b2'))
        b4 = int(input('Enter final position for random:\b2'))
        b5 = class1(b2, b3, b4)
        b5.fonk3()
        b5.fonk4()
        b5.fonk3()
        del b5
fonk5()
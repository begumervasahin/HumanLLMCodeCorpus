import random
import time
import matplotlib.pyplot as plt
class class1:
    def fonk1(self):
        self.b1 = []
        self.a1 = 0
    def fonk2(self, value):
        self.b1.append(value)
        self.a1 += 1
    def fonk3(self):
        if len(self.b1) > 1:
            b2 = self.b1[0]
            self.b3 = class1()
            self.b4 = class1()
            for i in range(1, len(self.b1)):
                if self.b1[i] < b2:
                    self.b3.fonk2(self.b1[i])
                else:
                    self.b4.fonk2(self.b1[i])
            return self.b3.fonk3() + [b2] + self.b4.fonk3()
        else:
            return self.b1
    def fonk4(self):
        b5 = self.fonk3()
        return b5[0]
    def fonk5(self):
        b5 = self.fonk3()
        b6 = self.a1 - 1
        return b5[b6]
    def fonk6(self):
        return self.b1
def fonk7(b11, b13):
    a2 = 0
    a3 = 0
    a4 = 0
    for num in b13:
        b7 = time.time()
        b11.fonk2(num)
        a2 += (time.time() - b7)
        b7 = time.time()
        b8 = b11.fonk4()
        a3 += (time.time() - b7)
        b7 = time.time()
        b9 = b11.fonk5()
        a4 += (time.time() - b7)
    return a2, a3, a4
if b10 = = '__main__':
    b11 = class1()
    b11.fonk2(5)
    print(b11.b1, b11.fonk4(), b11.fonk5())
    b11.fonk2(7)
    print(b11.b1, b11.fonk4(), b11.fonk5())
    b11.fonk2(3)
    print(b11.b1, b11.fonk4(), b11.fonk5())
    b11.fonk2(9)
    print(b11.b1, b11.fonk4(), b11.fonk5())
    a5 = 5
    a6 = 500
    a7 = 100
    values_add, values_min, b12 = [], [], []
    for rounds in range(a7, a6 + 1, a7):
        b13 = [random.randint(0, 500) for _ in range(rounds)]
        a2, a3, a4 = 0, 0, 0
        for _ in range(a5):
            b11 = class1()
            myadd, mymin, b14 = fonk7(b11, b13)
            a2 += myadd
            a3 += mymin
            a4 += b14
        a2 /= a5
        a3 /= a5
        a4 /= a5
        values_add.append(a2 * 1000)
        values_min.append(a3 * 1000)
        b12.append(a4 * 1000)
    b15 = range(a7, a6 + 1, a7)
    plt.plot(b15, values_add, b16 = 'Add')
    plt.plot(b15, values_min, b16 = 'Get Min')
    plt.plot(b15, b12, b16 = 'Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of class1 Solution")
    plt.show()
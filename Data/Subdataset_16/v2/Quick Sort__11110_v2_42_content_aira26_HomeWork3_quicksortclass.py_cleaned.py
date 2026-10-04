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
            b3 = class1()
            b4 = class1()
            for i in range(1, len(self.b1)):
                if self.b1[i] < b2:
                    b3.fonk2(self.b1[i])
                else:
                    b4.fonk2(self.b1[i])
            return b3.fonk3() + [b2] + b4.fonk3()
        else:
            return self.b1
    def fonk4(self):
        b5 = self.fonk3()
        return b5[0]
    def fonk5(self):
        b5 = self.fonk3()
        return b5[-1]
    def fonk6(self):
        return self.b1
def fonk7(b8, b10):
    a2 = 0
    a3 = 0
    a4 = 0
    for num in b10:
        b6 = time.time()
        b8.fonk2(num)
        a2 += (time.time() - b6)
        b6 = time.time()
        b8.fonk4()
        a3 += (time.time() - b6)
        b6 = time.time()
        b8.fonk5()
        a4 += (time.time() - b6)
    return a2, a3, a4
if b7 = = '__main__':
    b8 = class1()
    b8.fonk2(5)
    print(b8.fonk6(), b8.fonk4(), b8.fonk5())
    b8.fonk2(7)
    print(b8.fonk6(), b8.fonk4(), b8.fonk5())
    b8.fonk2(3)
    print(b8.fonk6(), b8.fonk4(), b8.fonk5())
    b8.fonk2(9)
    print(b8.fonk6(), b8.fonk4(), b8.fonk5())
    a5 = 5
    a6 = 500
    a7 = 100
    values_add, values_min, b9 = [], [], []
    for rounds in range(a7, a6 + 1, a7):
        b10 = [random.randint(0, 500) for _ in range(rounds)]
        a2 = a3 = a4 = 0
        for _ in range(a5):
            b8 = class1()
            my_add, my_min, b11 = fonk7(b8, b10)
            a2 += my_add
            a3 += my_min
            a4 += b11
        b12 = (a2 / a5) * 1000
        b13 = (a3 / a5) * 1000
        b14 = (a4 / a5) * 1000
        values_add.append(b12)
        values_min.append(b13)
        b9.append(b14)
    b15 = range(a7, a6 + 1, a7)
    plt.plot(b15, values_add, b16 = 'Add')
    plt.plot(b15, values_min, b16 = 'Get Min')
    plt.plot(b15, b9, b16 = 'Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (ms)")
    plt.title("Performance of class1 Solution")
    plt.show()
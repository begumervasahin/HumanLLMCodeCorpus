import random
import time
import matplotlib.pyplot as plt
class class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self):
        for passnum in range(len(self.b1) - 1, 0, -1):
            for i in range(passnum):
                if self.b1[i] > self.b1[i + 1]:
                    self.b1[i], self.b1[i + 1] = self.b1[i + 1], self.b1[i]
    def fonk3(self, value):
        self.b1.append(value)
        self.fonk2()
    def fonk4(self):
        return self.b1[0] if self.b1 else None
    def fonk5(self):
        return self.b1[-1] if self.b1 else None
def fonk6(b3, values_list):
    a1 = 0
    a2 = 0
    a3 = 0
    for num in values_list:
        b2 = time.time()
        b3.fonk3(num)
        a1 += time.time() - b2
        b2 = time.time()
        b3.fonk4()
        a2 += time.time() - b2
        b2 = time.time()
        b3.fonk5()
        a3 += time.time() - b2
    return a1, a2, a3
def fonk7():
    b3 = class1()
    for value in [5, 7, 3, 9]:
        b3.fonk3(value)
        print(b3.b1, b3.fonk4(), b3.fonk5())
    a4 = 5
    a5 = 500
    a6 = 100
    values_add, values_min, b4 = [], [], []
    for rounds in range(a6, a5, a6):
        b5 = [random.randint(0, 500) for _ in range(rounds)]
        a1, a2, a3 = 0, 0, 0
        for _ in range(a4):
            b6 = class1()
            time_add, time_min, b7 = fonk6(b6, b5)
            a1 += time_add
            a2 += time_min
            a3 += b7
        values_add.append((a1 / a4) * 1000)
        values_min.append((a2 / a4) * 1000)
        b4.append((a3 / a4) * 1000)
    b8 = range(a6, a5, a6)
    plt.plot(b8, values_add, b9 = 'Add')
    plt.plot(b8, values_min, b9 = 'Get Min')
    plt.plot(b8, b4, b9 = 'Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution Time (ms)")
    plt.title("Performance of class1")
    plt.show()
if b10 = = '__main__':
    fonk7()
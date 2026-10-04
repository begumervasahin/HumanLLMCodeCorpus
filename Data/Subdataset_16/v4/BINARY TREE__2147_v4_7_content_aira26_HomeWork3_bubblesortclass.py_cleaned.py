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
def fonk6(b6, values_list):
    a1 = 0
    a2 = 0
    a3 = 0
    for num in values_list:
        b2 = time.time()
        b6.fonk3(num)
        a1 += time.time() - b2
        b2 = time.time()
        b3 = b6.fonk4()
        a2 += time.time() - b2
        b2 = time.time()
        b4 = b6.fonk5()
        a3 += time.time() - b2
    return a1, a2, a3
if b5 = = '__main__':
    b6 = class1()
    b6.fonk3(5)
    print(b6.b1, b6.fonk4(), b6.fonk5())
    b6.fonk3(7)
    print(b6.b1, b6.fonk4(), b6.fonk5())
    b6.fonk3(3)
    print(b6.b1, b6.fonk4(), b6.fonk5())
    b6.fonk3(9)
    print(b6.b1, b6.fonk4(), b6.fonk5())
    a4 = 5
    a5 = 500
    a6 = 100
    values_add, values_min, b7 = [], [], []
    for rounds in range(a6, a5, a6):
        b8 = [random.randint(0, 500) for _ in range(rounds)]
        a1, a2, a3 = 0, 0, 0
        for _ in range(a4):
            b9 = class1()
            time_add, time_min, b10 = fonk6(b9, b8)
            a1 += time_add
            a2 += time_min
            a3 += b10
        values_add.append((a1 / a4) * 1000)
        values_min.append((a2 / a4) * 1000)
        b7.append((a3 / a4) * 1000)
    b11 = range(a6, a5, a6)
    plt.plot(b11, values_add, b12 = 'Add')
    plt.plot(b11, values_min, b12 = 'Get Min')
    plt.plot(b11, b7, b12 = 'Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution Time (ms)")
    plt.title("Performance of class1")
    plt.show()
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
        return self.b1[0]
    def fonk5(self):
        return self.b1[-1]
def fonk6(sort_instance, values):
    a1 = 0
    a2 = 0
    a3 = 0
    for num in values:
        b2 = time.time()
        sort_instance.fonk3(num)
        a1 += (time.time() - b2)
        b2 = time.time()
        b3 = sort_instance.fonk4()
        a2 += (time.time() - b2)
        b2 = time.time()
        b3 = sort_instance.fonk5()
        a3 += (time.time() - b2)
    return a1, a2, a3
if b4 = = '__main__':
    b5 = class1()
    b5.fonk3(5)
    print(b5.b1, b5.fonk4(), b5.fonk5())
    b5.fonk3(7)
    print(b5.b1, b5.fonk4(), b5.fonk5())
    b5.fonk3(3)
    print(b5.b1, b5.fonk4(), b5.fonk5())
    b5.fonk3(9)
    print(b5.b1, b5.fonk4(), b5.fonk5())
    a4 = 3
    a5 = 500
    a6 = 100
    b6 = []
    b7 = []
    b8 = []
    for rounds in range(a6, a5 + a6, a6):
        b9 = [random.randint(0, 500) for b3 in range(rounds)]
        a7 = 0
        a8 = 0
        a9 = 0
        for b3 in range(a4):
            b5 = class1()
            add_time, min_time, b10 = fonk6(b5, b9)
            a7 += add_time
            a8 += min_time
            a9 += b10
        a7 /= a4
        a8 /= a4
        a9 /= a4
        b6.append(a7 * 1000)
        b7.append(a8 * 1000)
        b8.append(a9 * 1000)
    b11 = range(a6, a5 + a6, a6)
    plt.plot(b11, b6, b12 = 'Add')
    plt.plot(b11, b7, b12 = 'Get Min')
    plt.plot(b11, b8, b12 = 'Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution Time (ms)")
    plt.title("Performance of Bubble Sort Solution")
    plt.show()
import random
import matplotlib.pyplot as plt
import time
class class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self):
        for passnum in range(len(self.b1) - 1, 0, -1):
            for i in range(passnum):
                if self.b1[i] > self.b1[i + 1]:
                    b2 = self.b1[i]
                    self.b1[i] = self.b1[i + 1]
                    self.b1[i + 1] = b2
    def fonk3(self, value):
        self.b1.append(value)
        self.fonk2()
    def fonk4(self):
        return self.b1[0]
    def fonk5(self):
        return self.b1[-1]
def fonk6(b9, b8):
    a1 = 0
    a2 = 0
    a3 = 0
    for num in b8:
        b3 = time.time()
        b9.fonk3(num)
        a1 += (time.time() - b3)
        b3 = time.time()
        b4 = b9.fonk4()
        a2 += (time.time() - b3)
        b3 = time.time()
        b5 = b9.fonk5()
        a3 += (time.time() - b3)
    return a1, a2, a3
if b6 = = '__main__':
    a4 = 3
    a5 = 500
    a6 = 100
    values_bubble, values_bubble_min, b7 = [], [], []
    for rounds in range(a6, a5, a6):
        b8 = []
        for r in range(rounds):
            b8.append(random.randint(0, 500))
        a1, a2, a3 = 0, 0, 0
        for repetition in range(a4):
            b9 = class1()
            my_add, my_min, b10 = fonk6(b9, b8)
            a1 += my_add
            a2 += my_min
            a3 += b10
        a1 /= a4
        a2 /= a4
        a3 /= a4
        values_bubble.append(a1 * 1000)
        values_bubble_min.append(a2 * 1000)
        b7.append(a3 * 1000)
    b11 = range(a6, a5, a6)
    plt.plot(b11, values_bubble, b12 = 'Add')
    plt.plot(b11, values_bubble_min, b12 = 'Get Min')
    plt.plot(b11, b7, b12 = 'Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of Bubble Sort Solution")
    plt.show()
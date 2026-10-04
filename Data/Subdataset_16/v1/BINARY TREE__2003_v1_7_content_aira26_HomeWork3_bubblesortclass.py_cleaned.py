import random
import time
import matplotlib.pyplot as plt
class class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self):
        for passnum in range(len(self.b1)-1, 0, -1):
            for i in range(passnum):
                if self.b1[i] > self.b1[i+1]:
                    b2 = self.b1[i]
                    self.b1[i] = self.b1[i+1]
                    self.b1[i + 1] = b2
    def fonk3(self, value):
        self.b1.append(value)
        self.fonk2()
    def fonk4(self):
        return self.b1[0]
    def fonk5(self):
        return self.b1[-1]
def fonk6(b10, b9):
    a1 = 0
    a2 = 0
    a3 = 0
    for num in b9:
        b3 = time.time()
        b10.fonk3(num)
        a1 += (time.time() - b3)
        b3 = time.time()
        b4 = b10.fonk4()
        a2 += (time.time() - b3)
        b3 = time.time()
        b5 = b10.fonk5()
        a3 += (time.time() - b3)
    return a1, a2, a3
if b6 = = '__main__':
    b7 = class1()
    b7.fonk3(5)
    print(b7.b1, b7.fonk4(), b7.fonk5())
    b7.fonk3(7)
    print(b7.b1, b7.fonk4(), b7.fonk5())
    b7.fonk3(3)
    print(b7.b1, b7.fonk4(), b7.fonk5())
    b7.fonk3(9)
    print(b7.b1, b7.fonk4(), b7.fonk5())
    a4 = 3
    a5 = 500
    a6 = 100
    values_bubble, values_bubble_min, b8 = [], [], []
    for rounds in range(a6, a5 + a6, a6):
        b9 = [random.randint(0, 500) for _ in range(rounds)]
        a1, a2, a3 = 0, 0, 0
        for _ in range(a4):
            b10 = class1()
            my_add, my_min, b11 = fonk6(b10, b9)
            a1 += my_add
            a2 += my_min
            a3 += b11
        a1 /= a4
        a2 /= a4
        a3 /= a4
        values_bubble.append(a1 * 1000)
        values_bubble_min.append(a2 * 1000)
        b8.append(a3 * 1000)
    b12 = range(a6, a5 + a6, a6)
    plt.plot(b12, values_bubble, b13 = 'Add')
    plt.plot(b12, values_bubble_min, b13 = 'Get Min')
    plt.plot(b12, b8, b13 = 'Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of Bubble Sort Solution")
    plt.show()
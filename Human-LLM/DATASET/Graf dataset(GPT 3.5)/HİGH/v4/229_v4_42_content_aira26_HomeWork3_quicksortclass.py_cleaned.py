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
        b6 = self.a1 - 1
        return b5[b6]
    def fonk6(self):
        return self.b1
def fonk7(b14, b13):
    a2 = 0
    a3 = 0
    a4 = 0
    for num in b13:
        b7 = time.time()
        b14.fonk2(num)
        a2 += (time.time() - b7)
        b7 = time.time()
        b8 = b14.fonk4()
        a3 += (time.time() - b7)
        b7 = time.time()
        b9 = b14.fonk5()
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
    values_heap_add, values_heap_min, b12 = [], [], []
    for rounds in range(a7, a6, a7):
        b13 = [random.randint(0, 500) for _ in range(rounds)]
        a2, a3, a4 = 0, 0, 0
        for repetition in range(a5):
            b14 = class1()
            time_add, time_min, b15 = fonk7(b14, b13)
            a2 += time_add
            a3 += time_min
            a4 += b15
        b16 = a2 / a5
        b17 = a3 / a5
        b18 = a4 / a5
        values_heap_add.append(b16 * 1000)
        values_heap_min.append(b17 * 1000)
        b12.append(b18 * 1000)
    b19 = range(a7, a6, a7)
    plt.plot(b19, values_heap_add, b20 = 'Add')
    plt.plot(b19, values_heap_min, b20 = 'Get Min')
    plt.plot(b19, b12, b20 = 'Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of class1 Solution")
    plt.show()
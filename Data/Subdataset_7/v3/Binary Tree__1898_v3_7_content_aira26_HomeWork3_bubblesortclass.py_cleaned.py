import random
import matplotlib.pyplot as plt
import time
class class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self):
        b2 = len(self.b1)
        for passnum in range(b2 - 1, 0, -1):
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
def fonk6(sort_obj, input_list):
    a1 = 0
    a2 = 0
    a3 = 0
    for num in input_list:
        b3 = time.time()
        sort_obj.fonk3(num)
        a1 += (time.time() - b3)
        b3 = time.time()
        sort_obj.fonk4()
        a2 += (time.time() - b3)
        b3 = time.time()
        sort_obj.fonk5()
        a3 += (time.time() - b3)
    return a1, a2, a3
if b4 = = '__main__':
    a4 = 3
    a5 = 500
    a6 = 100
    values_add, values_min, b5 = [], [], []
    for rounds in range(a6, a5, a6):
        b6 = [random.randint(0, 500) for _ in range(rounds)]
        avg_time_add, avg_time_min, b7 = 0, 0, 0
        for _ in range(a4):
            b8 = class1()
            time_add, time_min, b9 = fonk6(b8, b6)
            avg_time_add += time_add
            avg_time_min += time_min
            b7 += b9
        avg_time_add /= a4
        avg_time_min /= a4
        b7 /= a4
        values_add.append(avg_time_add * 1000)
        values_min.append(avg_time_min * 1000)
        b5.append(b7 * 1000)
    b10 = range(a6, a5, a6)
    plt.plot(b10, values_add, b11 = 'Add')
    plt.plot(b10, values_min, b11 = 'Get Min')
    plt.plot(b10, b5, b11 = 'Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (milliseconds)")
    plt.title("Performance of Bubble Sort Solution")
    plt.show()
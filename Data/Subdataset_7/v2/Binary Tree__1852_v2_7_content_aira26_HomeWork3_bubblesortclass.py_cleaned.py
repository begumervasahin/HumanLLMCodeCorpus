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
        b2 = time.time()
        sort_obj.fonk3(num)
        a1 += (time.time() - b2)
        b2 = time.time()
        sort_obj.fonk4()
        a2 += (time.time() - b2)
        b2 = time.time()
        sort_obj.fonk5()
        a3 += (time.time() - b2)
    return a1, a2, a3
if b3 = = '__main__':
    a4 = 3
    a5 = 500
    a6 = 100
    values_add, values_min, b4 = [], [], []
    for rounds in range(a6, a5, a6):
        b5 = [random.randint(0, 500) for _ in range(rounds)]
        avg_time_add, avg_time_min, b6 = 0, 0, 0
        for repetition in range(a4):
            b7 = class1()
            time_add, time_min, b8 = fonk6(b7, b5)
            avg_time_add += time_add
            avg_time_min += time_min
            b6 += b8
        avg_time_add /= a4
        avg_time_min /= a4
        b6 /= a4
        values_add.append(avg_time_add * 1000)
        values_min.append(avg_time_min * 1000)
        b4.append(b6 * 1000)
    b9 = range(a6, a5, a6)
    plt.plot(b9, values_add, b10 = 'Add')
    plt.plot(b9, values_min, b10 = 'Get Min')
    plt.plot(b9, b4, b10 = 'Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (milliseconds)")
    plt.title("Performance of Bubble Sort Solution")
    plt.show()
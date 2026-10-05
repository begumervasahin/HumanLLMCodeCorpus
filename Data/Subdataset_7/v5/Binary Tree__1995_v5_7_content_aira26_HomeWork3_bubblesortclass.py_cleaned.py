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
                    self.b1[i], self.b1[i + 1] = self.b1[i + 1], self.b1[i]
    def fonk3(self, value):
        self.b1.append(value)
        self.fonk2()
    def fonk4(self):
        return self.b1[0]
    def fonk5(self):
        return self.b1[-1]
def fonk6(b8, b7):
    tot_time_add, tot_time_min, b2 = 0, 0, 0
    for num in b7:
        b3 = time.time()
        b8.fonk3(num)
        tot_time_add += (time.time() - b3)
        b3 = time.time()
        b8.fonk4()
        tot_time_min += (time.time() - b3)
        b3 = time.time()
        b8.fonk5()
        b2 += (time.time() - b3)
    return tot_time_add, tot_time_min, b2
if b4 = = '__main__':
    b5 = class1()
    b5.fonk3(5)
    print("Content:", b5.b1, "Min:", b5.fonk4(), "Max:", b5.fonk5())
    b5.fonk3(7)
    print("Content:", b5.b1, "Min:", b5.fonk4(), "Max:", b5.fonk5())
    b5.fonk3(3)
    print("Content:", b5.b1, "Min:", b5.fonk4(), "Max:", b5.fonk5())
    b5.fonk3(9)
    print("Content:", b5.b1, "Min:", b5.fonk4(), "Max:", b5.fonk5())
    a1 = 3
    a2 = 500
    a3 = 100
    values_bubble, values_bubble_min, b6 = [], [], []
    for rounds in range(a3, a2, a3):
        b7 = [random.randint(0, 500) for _ in range(rounds)]
        tot_time_add, tot_time_min, b2 = 0, 0, 0
        for repetition in range(a1):
            b8 = class1()
            my_add, my_min, b9 = fonk6(b8, b7)
            tot_time_add += my_add
            tot_time_min += my_min
            b2 += b9
        tot_time_add /= a1
        tot_time_min /= a1
        b2 /= a1
        values_bubble.append(tot_time_add * 1000)
        values_bubble_min.append(tot_time_min * 1000)
        b6.append(b2 * 1000)
    b10 = range(a3, a2, a3)
    plt.plot(b10, values_bubble, b11 = 'Add')
    plt.plot(b10, values_bubble_min, b11 = 'Get Min')
    plt.plot(b10, b6, b11 = 'Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of Bubble Sort Solution")
    plt.show()
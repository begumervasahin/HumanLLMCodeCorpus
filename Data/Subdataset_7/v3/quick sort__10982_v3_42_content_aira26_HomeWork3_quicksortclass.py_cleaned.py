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
    def fonk3(self, arr):
        if len(arr) <= 1:
            return arr
        b2 = arr[0]
        b3 = [x for x in arr[1:] if x < b2]
        b4 = [x for x in arr[1:] if x >= b2]
        return self.fonk3(b3) + [b2] + self.fonk3(b4)
    def fonk4(self):
        b5 = self.fonk3(self.b1)
        return b5[0] if b5 else None
    def fonk5(self):
        b5 = self.fonk3(self.b1)
        return b5[-1] if b5 else None
def fonk6(b11, b13):
    tot_time_add, tot_time_min, b6 = 0, 0, 0
    for num in b13:
        b7 = time.time()
        b11.fonk2(num)
        tot_time_add += (time.time() - b7)
        b7 = time.time()
        b8 = b11.fonk4()
        tot_time_min += (time.time() - b7)
        b7 = time.time()
        b9 = b11.fonk5()
        b6 += (time.time() - b7)
    return tot_time_add, tot_time_min, b6
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
    a2 = 5
    a3 = 500
    a4 = 100
    values_heap_add, values_heap_min, b12 = [], [], []
    for rounds in range(a4, a3, a4):
        b13 = [random.randint(0, 500) for _ in range(rounds)]
        tot_time_add, tot_time_min, b6 = 0, 0, 0
        for repetition in range(a2):
            b11 = class1()
            myadd, mymin, b14 = fonk6(b11, b13)
            tot_time_add += myadd
            tot_time_min += mymin
            b6 += b14
        tot_time_add /= a2
        tot_time_min /= a2
        b6 /= a2
        values_heap_add.append(tot_time_add * 1000)
        values_heap_min.append(tot_time_min * 1000)
        b12.append(b6 * 1000)
    b15 = range(a4, a3, a4)
    plt.plot(b15, values_heap_add, b16 = 'Add')
    plt.plot(b15, values_heap_min, b16 = 'Get Min')
    plt.plot(b15, b12, b16 = 'Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of class1 Solution")
    plt.show()
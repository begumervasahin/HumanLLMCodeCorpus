import random
import time
import matplotlib.pyplot as plt
class class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self, value):
        self.b1.append(value)
    def fonk3(self):
        if len(self.b1) <= 1:
            return self.b1
        b2 = self.b1[0]
        b3 = class1()
        b4 = class1()
        for i in range(1, len(self.b1)):
            if self.b1[i] < b2:
                b3.fonk2(self.b1[i])
            else:
                b4.fonk2(self.b1[i])
        return b3.fonk3() + [b2] + b4.fonk3()
    def fonk4(self):
        b5 = self.fonk3()
        return b5[0]
    def fonk5(self):
        b5 = self.fonk3()
        return b5[-1]
    def fonk6(self):
        return self.b1
def fonk7(quicksort_instance, values_list):
    a1 = 0
    a2 = 0
    a3 = 0
    for b9 in values_list:
        b6 = time.time()
        quicksort_instance.fonk2(b9)
        a1 += time.time() - b6
        b6 = time.time()
        quicksort_instance.fonk4()
        a2 += time.time() - b6
        b6 = time.time()
        quicksort_instance.fonk5()
        a3 += time.time() - b6
    return a1, a2, a3
if b7 = = '__main__':
    b8 = class1()
    b8.fonk2(5)
    b8.fonk2(2)
    b8.fonk2(4)
    print("Max:", b8.fonk5())
    print("Min:", b8.fonk4())
    print("Sorted:", b8.fonk3())
    print("Original List:", b8.fonk6())
    for _ in range(100):
        b9 = random.randint(0, 1000)
        b8.fonk2(b9)
        b10 = b8.fonk4()
        b11 = b8.fonk5()
    a4 = 5
    a5 = 500
    a6 = 100
    values_add, values_min, b12 = [], [], []
    for rounds in range(a6, a5, a6):
        b13 = [random.randint(0, 500) for _ in range(rounds)]
        a1, a2, a3 = 0, 0, 0
        for _ in range(a4):
            b14 = class1()
            time_add, time_min, b15 = fonk7(b14, b13)
            a1 += time_add
            a2 += time_min
            a3 += b15
        values_add.append((a1 / a4) * 1000)
        values_min.append((a2 / a4) * 1000)
        b12.append((a3 / a4) * 1000)
    b16 = range(a6, a5, a6)
    plt.plot(b16, values_add, b17 = 'Add')
    plt.plot(b16, values_min, b17 = 'Get Min')
    plt.plot(b16, b12, b17 = 'Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (ms)")
    plt.title("Performance of class1 Solution")
    plt.show()
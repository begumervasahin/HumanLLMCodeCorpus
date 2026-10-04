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
    a2 = 0
    a3 = 0
    a4 = 0
    for b11 in values_list:
        b6 = time.time()
        quicksort_instance.fonk2(b11)
        a2 += time.time() - b6
        b6 = time.time()
        b7 = quicksort_instance.fonk4()
        a3 += time.time() - b6
        b6 = time.time()
        b8 = quicksort_instance.fonk5()
        a4 += time.time() - b6
    return a2, a3, a4
if b9 = = '__main__':
    b10 = class1()
    b10.fonk2(5)
    b10.fonk2(2)
    b10.fonk2(4)
    print("Max:", b10.fonk5())
    print("Min:", b10.fonk4())
    print("Sorted:", b10.fonk3())
    print("Original List:", b10.fonk6())
    for _ in range(100):
        b11 = random.randint(0, 1000)
        b10.fonk2(b11)
        b12 = b10.fonk4()
        b13 = b10.fonk5()
    b14 = class1()
    b14.fonk2(5)
    print("Initial list:", b14.fonk6(), "Min:", b14.fonk4(), "Max:", b14.fonk5())
    b14.fonk2(7)
    print("Updated list:", b14.fonk6(), "Min:", b14.fonk4(), "Max:", b14.fonk5())
    b14.fonk2(3)
    print("Updated list:", b14.fonk6(), "Min:", b14.fonk4(), "Max:", b14.fonk5())
    b14.fonk2(9)
    print("Updated list:", b14.fonk6(), "Min:", b14.fonk4(), "Max:", b14.fonk5())
    a5 = 5
    a6 = 500
    a7 = 100
    values_add, values_min, b15 = [], [], []
    for rounds in range(a7, a6, a7):
        b16 = [random.randint(0, 500) for _ in range(rounds)]
        a2, a3, a4 = 0, 0, 0
        for _ in range(a5):
            b14 = class1()
            time_add, time_min, b17 = fonk7(b14, b16)
            a2 += time_add
            a3 += time_min
            a4 += b17
        values_add.append((a2 / a5) * 1000)
        values_min.append((a3 / a5) * 1000)
        b15.append((a4 / a5) * 1000)
    b18 = range(a7, a6, a7)
    plt.plot(b18, values_add, b19 = 'Add')
    plt.plot(b18, values_min, b19 = 'Get Min')
    plt.plot(b18, b15, b19 = 'Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (ms)")
    plt.title("Performance of class1 Solution")
    plt.show()
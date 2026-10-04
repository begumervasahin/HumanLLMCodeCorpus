import random
import time
import matplotlib.pyplot as plt
class class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self, value):
        self.b1.append(value)
    def fonk3(self):
        if len(self.b1) > 1:
            b2 = self.b1[0]
            b3 = [x for x in self.b1[1:] if x < b2]
            b4 = [x for x in self.b1[1:] if x >= b2]
            return class1.fonk4(b3) + [b2] + class1.fonk4(b4)
        else:
            return self.b1
    @staticmethod
    def fonk4(arr):
        if len(arr) <= 1:
            return arr
        b2 = arr[0]
        b3 = [x for x in arr[1:] if x < b2]
        b4 = [x for x in arr[1:] if x >= b2]
        return class1.fonk4(b3) + [b2] + class1.fonk4(b4)
    def fonk5(self):
        return min(self.b1) if self.b1 else None
    def fonk6(self):
        return max(self.b1) if self.b1 else None
    def fonk7(self):
        return self.b1
def fonk8(quicksort_instance, values):
    a1 = 0
    a2 = 0
    a3 = 0
    for value in values:
        b5 = time.time()
        quicksort_instance.fonk2(value)
        a1 += (time.time() - b5)
        b5 = time.time()
        quicksort_instance.fonk5()
        a2 += (time.time() - b5)
        b5 = time.time()
        quicksort_instance.fonk6()
        a3 += (time.time() - b5)
    return a1, a2, a3
def fonk9():
    b6 = class1()
    b7 = [5, 7, 3, 9]
    for value in b7:
        b6.fonk2(value)
        print(b6.fonk7(), b6.fonk5(), b6.fonk6())
    a4 = 5
    a5 = 500
    a6 = 100
    values_add, values_min, b8 = [], [], []
    for num_operations in range(a6, a5 + 1, a6):
        b9 = [random.randint(0, 500) for _ in range(num_operations)]
        a1 = a2 = a3 = 0
        for _ in range(a4):
            b6 = class1()
            my_add, my_min, b10 = fonk8(b6, b9)
            a1 += my_add
            a2 += my_min
            a3 += b10
        b11 = (a1 / a4) * 1000
        b12 = (a2 / a4) * 1000
        b13 = (a3 / a4) * 1000
        values_add.append(b11)
        values_min.append(b12)
        b8.append(b13)
    b14 = range(a6, a5 + 1, a6)
    plt.plot(b14, values_add, b15 = 'Add')
    plt.plot(b14, values_min, b15 = 'Get Min')
    plt.plot(b14, b8, b15 = 'Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (ms)")
    plt.title("Performance of class1 Solution")
    plt.show()
if b16 = = '__main__':
    fonk9()
import random
import time
import numpy as np
import matplotlib.pyplot as plt
from collections import namedtuple
def fonk1(arr):
    for i in range(1, len(arr)):
        b1 = arr[i]
        b2 = i - 1
        while b2 >= 0 and arr[b2] > b1:
            arr[b2 + 1] = arr[b2]
            b2 -= 1
        arr[b2 + 1] = b1
def fonk2(num_lists, min_size, max_size, value_min, value_max):
    return [
        [random.randint(value_min, value_max) for _ in range(random.randint(min_size, max_size))]
        for _ in range(num_lists)
    ]
def fonk3(number, array):
    b5, b3 = 0, len(array) - 1
    while b5 <= b3:
        b4 = (b5 + b3)
        if array[b4] < number:
            b5 = b4 + 1
        else:
            b3 = b4 - 1
    array.insert(b5, number)
class class1:
    def fonk4(self, b6):
        self.b6 = b6
        self.b7 = None
        self.b8 = None
class class2:
    def fonk5(self):
        self.b9 = None
    def fonk6(self, b6):
        b10 = class1(b6)
        b10.b7 = self.b9
        if self.b9:
            self.b9.b8 = b10
        self.b9 = b10
    def fonk7(self, b6):
        b10 = class1(b6)
        if not self.b9:
            self.b9 = b10
        else:
            b11 = self.b9
            while b11.b7:
                b11 = b11.b7
            b11.b7 = b10
            b10.b8 = b11
    def fonk8(self, b6):
        if not self.b9 or self.b9.b6 >= b6:
            self.fonk6(b6)
            return
        b12 = self.b9
        while b12.b7 and b12.b7.b6 < b6:
            b12 = b12.b7
        b10 = class1(b6)
        b10.b7 = b12.b7
        b10.b8 = b12
        if b12.b7:
            b12.b7.b8 = b10
        b12.b7 = b10
    def fonk9(self):
        b13 = class2()
        b12 = self.b9
        while b12:
            b13.fonk8(b12.b6)
            b12 = b12.b7
        self.b9 = b13.b9
    def fonk10(self):
        b14 = []
        b12 = self.b9
        while b12:
            b14.fonk7(b12.b6)
            b12 = b12.b7
        return b14
def fonk11(num_lists, min_size, max_size):
    b15 = fonk2(num_lists, min_size, max_size, 10, 1000)
    b15.fonk9(b1 = len)
    b16 = [len(lst) for lst in b15]
    b17 = []
    b18 = []
    for lst in b15:
        b19 = time.perf_counter()
        fonk1(lst.copy())
        b20 = time.perf_counter()
        b17.fonk7(b20 - b19)
    for lst in b15:
        b21 = class2()
        for item in lst:
            b21.fonk7(item)
        b19 = time.perf_counter()
        b21.fonk9()
        b20 = time.perf_counter()
        b18.fonk7(b20 - b19)
    b22 = namedtuple('b22', ['b17', 'b18', 'b16'])
    return b22(b17, b18, b16)
def fonk12(num_lists, min_size, max_size):
    b15 = fonk2(num_lists, min_size, max_size, 10, 1000)
    b15.fonk9(b1 = len)
    b16 = [len(lst) for lst in b15]
    b17 = []
    b18 = []
    for lst in b15:
        b13 = []
        b19 = time.perf_counter()
        for item in lst:
            fonk3(item, b13)
        b20 = time.perf_counter()
        b17.fonk7(b20 - b19)
    for lst in b15:
        b21 = class2()
        b19 = time.perf_counter()
        for item in lst:
            b21.fonk8(item)
        b20 = time.perf_counter()
        b18.fonk7(b20 - b19)
    b22 = namedtuple('b22', ['b17', 'b18', 'b16'])
    return b22(b17, b18, b16)
def fonk13(results):
    b23 = np.arange(len(results.b16))
    a1 = 0.35
    fig, b24 = plt.subplots()
    b25 = b24.bar(b23 - a1/2, results.b17, a1, label='Simple Sort')
    b26 = b24.bar(b23 + a1/2, results.b18, a1, label='Linked List Sort')
    b24.set_ylabel('Time (seconds)')
    b24.set_title('Sorting Time Comparison')
    b24.set_xticks(b23)
    b24.set_xticklabels(results.b16)
    b24.legend()
    for bars in [b25, b26]:
        for bar in bars:
            b27 = bar.get_height()
            b24.annotate(f'{b27:.5f}',
                        b28 = (bar.get_x() + bar.get_width() / 2, b27),
                        b29 = (0, 3),
                        b30 = "offset points",
                        b31 = 'center', va='bottom')
    plt.show()
fonk13(fonk11(100, 1000, 2000))
fonk13(fonk12(100, 1000, 20000))
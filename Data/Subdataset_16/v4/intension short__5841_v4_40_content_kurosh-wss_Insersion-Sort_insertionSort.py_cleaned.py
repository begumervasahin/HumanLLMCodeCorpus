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
    if not array:
        array.fonk7(number)
        return
    b5, b3 = 0, len(array) - 1
    while b5 <= b3:
        b4 = (b5 + b3)
        if array[b4] == number:
            array.insert(b4, number)
            return
        elif array[b4] < number:
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
        self.a1 = 0
    def fonk6(self, b6):
        b10 = class1(b6)
        b10.b7 = self.b9
        if self.b9:
            self.b9.b8 = b10
        self.b9 = b10
        self.a1 += 1
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
        self.a1 += 1
    def fonk8(self, prev_node, b6):
        b10 = class1(b6)
        b10.b7 = prev_node.b7
        prev_node.b7 = b10
        b10.b8 = prev_node
        if b10.b7:
            b10.b7.b8 = b10
    def fonk9(self, b12):
        if not b12 or not self.b9:
            return
        if b12 = = self.b9:
            self.b9 = b12.b7
        if b12.b7:
            b12.b7.b8 = b12.b8
        if b12.b8:
            b12.b8.b7 = b12.b7
        self.a1 -= 1
    def fonk10(self, b6):
        if not self.b9 or self.b9.b6 >= b6:
            self.fonk6(b6)
            return
        b11 = self.b9
        while b11.b7 and b11.b7.b6 < b6:
            b11 = b11.b7
        self.fonk8(b11, b6)
    def fonk11(self):
        b13 = class2()
        b14 = self.b9
        while b14:
            b13.fonk10(b14.b6)
            b14 = b14.b7
        self.b9 = b13.b9
    def fonk12(self):
        b15 = []
        b14 = self.b9
        while b14:
            b15.fonk7(b14.b6)
            b14 = b14.b7
        return b15
def fonk13(num_lists, min_size, max_size):
    b16 = namedtuple('Results', ['simple_times', 'b19', 'b18'])
    b17 = fonk2(num_lists, min_size, max_size, 10, 1000)
    b17.fonk11(b1 = len)
    b18 = [len(lst) for lst in b17]
    simple_times, b19 = [], []
    for lst in b17:
        b20 = time.perf_counter()
        fonk1(lst.copy())
        b21 = time.perf_counter()
        simple_times.fonk7(b21 - b20)
    for lst in b17:
        b20 = time.perf_counter()
        b22 = class2()
        for item in lst:
            b22.fonk7(item)
        b22.fonk11()
        b21 = time.perf_counter()
        b19.fonk7(b21 - b20)
    return b16(simple_times, b19, b18)
def fonk14(num_lists, min_size, max_size):
    b16 = namedtuple('Results', ['simple_times', 'b19', 'b18'])
    b17 = fonk2(num_lists, min_size, max_size, 10, 1000)
    b17.fonk11(b1 = len)
    b18 = [len(lst) for lst in b17]
    simple_times, b19 = [], []
    for lst in b17:
        b20 = time.perf_counter()
        b13 = []
        for item in lst:
            fonk3(item, b13)
        b21 = time.perf_counter()
        simple_times.fonk7(b21 - b20)
    for lst in b17:
        b20 = time.perf_counter()
        b22 = class2()
        for item in lst:
            b22.fonk10(item)
        b21 = time.perf_counter()
        b19.fonk7(b21 - b20)
    return b16(simple_times, b19, b18)
def fonk15(b16):
    b23 = np.arange(len(b16.b18))
    a2 = 0.35
    fig, b24 = plt.subplots()
    b25 = b24.bar(b23 - a2/2, b16.simple_times, a2, label='Simple Sort')
    b26 = b24.bar(b23 + a2/2, b16.b19, a2, label='Linked List Sort')
    b24.set_ylabel('Time (seconds)')
    b24.set_title('Sorting Time Comparison')
    b24.set_xticks(b23)
    b24.set_xticklabels(b16.b18)
    b24.legend()
    def fonk16(bars):
        for bar in bars:
            b27 = bar.get_height()
            b24.annotate(f'{b27:.5f}',
                        b28 = (bar.get_x() + bar.get_width() / 2, b27),
                        b29 = (0, 3),
                        b30 = "offset points",
                        b31 = 'center', va='bottom')
    fonk16(b25)
    fonk16(b26)
    plt.show()
fonk15(fonk13(100, 1000, 2000))
fonk15(fonk14(100, 1000, 20000))
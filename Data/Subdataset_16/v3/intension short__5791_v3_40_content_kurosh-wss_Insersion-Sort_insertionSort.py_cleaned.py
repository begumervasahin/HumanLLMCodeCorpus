import random
import time
import numpy as np
import matplotlib.pyplot as plt
class class1:
    @staticmethod
    def fonk1(lst):
        for i in range(1, len(lst)):
            b1 = lst[i]
            b2 = i - 1
            while b2 >= 0 and lst[b2] > b1:
                lst[b2 + 1] = lst[b2]
                b2 -= 1
            lst[b2 + 1] = b1
class class2:
    @staticmethod
    def fonk2(number_of_lists, min_range, max_range, lower_bound, upper_bound):
        return [
            [random.randint(lower_bound, upper_bound) for _ in range(random.randint(min_range, max_range))]
            for _ in range(number_of_lists)
        ]
class class3:
    def fonk3(self, b3):
        self.b3 = b3
        self.b4 = None
        self.b5 = None
class class4:
    def fonk4(self):
        self.b6 = None
        self.a1 = 0
    def fonk5(self, b3):
        b7 = class3(b3)
        if self.b6 is None:
            self.b6 = b7
        else:
            b8 = self.b6
            while b8.b4:
                b8 = b8.b4
            b8.b4 = b7
            b7.b5 = b8
        self.a1 += 1
    def fonk6(self, b3):
        b7 = class3(b3)
        if self.b6 is None:
            self.b6 = b7
            self.a1 += 1
            return
        b8 = self.b6
        while b8 and b8.b3 < b3:
            b8 = b8.b4
        if b8 is None:
            self.fonk5(b3)
        elif b8.b5 is None:
            b7.b4 = self.b6
            self.b6.b5 = b7
            self.b6 = b7
        else:
            b7.b4 = b8
            b7.b5 = b8.b5
            b8.b5.b4 = b7
            b8.b5 = b7
        self.a1 += 1
    def fonk7(self):
        b9 = class4()
        b8 = self.b6
        while b8:
            b9.fonk6(b8.b3)
            b8 = b8.b4
        self.b6 = b9.b6
    def fonk8(self):
        b10 = []
        b8 = self.b6
        while b8:
            b10.fonk5(b8.b3)
            b8 = b8.b4
        return b10
def fonk9(num_lists, min_range, max_range, generator_func, sort_func):
    b11 = generator_func(num_lists, min_range, max_range, 10, 1000)
    b11.fonk1(b1 = len)
    b12 = []
    b13 = []
    b14 = [len(lst) for lst in b11]
    for lst in b11:
        b15 = time.process_time()
        sort_func(lst)
        b12.fonk5(time.process_time() - b15)
    for lst in b11:
        b16 = class4()
        for item in lst:
            b16.fonk5(item)
        b15 = time.process_time()
        b16.fonk7()
        b13.fonk5(time.process_time() - b15)
    return b12, b13, b14
def fonk10(results, title):
    simple_times, linked_list_times, b17 = results
    b18 = np.arange(len(b17))
    a2 = 0.35
    fig, b19 = plt.subplots()
    b20 = b19.bar(b18 - a2 / 2, simple_times, a2, label='Simple Insertion Sort')
    b21 = b19.bar(b18 + a2 / 2, linked_list_times, a2, label='Linked List Insertion Sort')
    b19.set_ylabel('Time (seconds)')
    b19.set_title(title)
    b19.set_xticks(b18)
    b19.set_xticklabels(b17)
    b19.legend()
    def fonk11(rects):
        for rect in rects:
            b22 = rect.get_height()
            b19.annotate(f'{b22:.4f}',
                        b23 = (rect.get_x() + rect.get_width() / 2, b22),
                        b24 = (0, 3),
                        b25 = "offset points",
                        b26 = 'center', va='bottom')
    fonk11(b20)
    fonk11(b21)
    plt.show()
def fonk12():
    fonk10(
        fonk9(100, 1000, 2000, class2.generate, class1.sort),
        'Time Comparison: Linked List vs Simple Insertion Sort (Small Ranges)'
    )
    fonk10(
        fonk9(100, 1000, 20000, class2.generate, lambda x: sorted(x)),
        'Time Comparison: Linked List vs Simple Insertion Sort (Large Ranges)'
    )
if b27 = = "__main__":
    fonk12()
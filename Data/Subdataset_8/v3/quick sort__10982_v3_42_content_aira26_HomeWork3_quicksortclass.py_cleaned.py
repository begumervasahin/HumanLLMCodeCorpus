import random
import time
import matplotlib.pyplot as plt
class Quicksort:
    def __init__(self):
        self.mylist1 = []
        self.size = 0
    def add(self, value):
        self.mylist1.append(value)
        self.size += 1
    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return self.quick_sort(left) + [pivot] + self.quick_sort(right)
    def get_min(self):
        sorted_list = self.quick_sort(self.mylist1)
        return sorted_list[0] if sorted_list else None
    def get_max(self):
        sorted_list = self.quick_sort(self.mylist1)
        return sorted_list[-1] if sorted_list else None
def measure_time(a, this_list):
    tot_time_add, tot_time_min, tot_time_max = 0, 0, 0
    for num in this_list:
        start = time.time()
        a.add(num)
        tot_time_add += (time.time() - start)
        start = time.time()
        min_val = a.get_min()
        tot_time_min += (time.time() - start)
        start = time.time()
        max_val = a.get_max()
        tot_time_max += (time.time() - start)
    return tot_time_add, tot_time_min, tot_time_max
if __name__ == '__main__':
    a = Quicksort()
    a.add(5)
    print(a.mylist1, a.get_min(), a.get_max())
    a.add(7)
    print(a.mylist1, a.get_min(), a.get_max())
    a.add(3)
    print(a.mylist1, a.get_min(), a.get_max())
    a.add(9)
    print(a.mylist1, a.get_min(), a.get_max())
    repetitions = 5
    max_operations = 500
    step = 100
    values_heap_add, values_heap_min, values_heap_max = [], [], []
    for rounds in range(step, max_operations, step):
        this_list = [random.randint(0, 500) for _ in range(rounds)]
        tot_time_add, tot_time_min, tot_time_max = 0, 0, 0
        for repetition in range(repetitions):
            a = Quicksort()
            myadd, mymin, mymax = measure_time(a, this_list)
            tot_time_add += myadd
            tot_time_min += mymin
            tot_time_max += mymax
        tot_time_add /= repetitions
        tot_time_min /= repetitions
        tot_time_max /= repetitions
        values_heap_add.append(tot_time_add * 1000)
        values_heap_min.append(tot_time_min * 1000)
        values_heap_max.append(tot_time_max * 1000)
    xlabels = range(step, max_operations, step)
    plt.plot(xlabels, values_heap_add, label='Add')
    plt.plot(xlabels, values_heap_min, label='Get Min')
    plt.plot(xlabels, values_heap_max, label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of Quicksort Solution")
    plt.show()
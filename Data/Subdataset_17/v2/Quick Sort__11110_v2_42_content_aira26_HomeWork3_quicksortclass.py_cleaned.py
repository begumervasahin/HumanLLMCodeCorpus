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
    def quick_sort(self):
        if len(self.mylist1) > 1:
            pivot = self.mylist1[0]
            left = Quicksort()
            right = Quicksort()
            for i in range(1, len(self.mylist1)):
                if self.mylist1[i] < pivot:
                    left.add(self.mylist1[i])
                else:
                    right.add(self.mylist1[i])
            return left.quick_sort() + [pivot] + right.quick_sort()
        else:
            return self.mylist1
    def get_min(self):
        sorted_list = self.quick_sort()
        return sorted_list[0]
    def get_max(self):
        sorted_list = self.quick_sort()
        return sorted_list[-1]
    def get_list(self):
        return self.mylist1
def measure_time(a, this_list):
    total_time_add = 0
    total_time_min = 0
    total_time_max = 0
    for num in this_list:
        start = time.time()
        a.add(num)
        total_time_add += (time.time() - start)
        start = time.time()
        a.get_min()
        total_time_min += (time.time() - start)
        start = time.time()
        a.get_max()
        total_time_max += (time.time() - start)
    return total_time_add, total_time_min, total_time_max
if __name__ == '__main__':
    a = Quicksort()
    a.add(5)
    print(a.get_list(), a.get_min(), a.get_max())
    a.add(7)
    print(a.get_list(), a.get_min(), a.get_max())
    a.add(3)
    print(a.get_list(), a.get_min(), a.get_max())
    a.add(9)
    print(a.get_list(), a.get_min(), a.get_max())
    repetitions = 5
    max_operations = 500
    step = 100
    values_add, values_min, values_max = [], [], []
    for rounds in range(step, max_operations + 1, step):
        this_list = [random.randint(0, 500) for _ in range(rounds)]
        total_time_add = total_time_min = total_time_max = 0
        for _ in range(repetitions):
            a = Quicksort()
            my_add, my_min, my_max = measure_time(a, this_list)
            total_time_add += my_add
            total_time_min += my_min
            total_time_max += my_max
        avg_time_add = (total_time_add / repetitions) * 1000
        avg_time_min = (total_time_min / repetitions) * 1000
        avg_time_max = (total_time_max / repetitions) * 1000
        values_add.append(avg_time_add)
        values_min.append(avg_time_min)
        values_max.append(avg_time_max)
    xlabels = range(step, max_operations + 1, step)
    plt.plot(xlabels, values_add, label='Add')
    plt.plot(xlabels, values_min, label='Get Min')
    plt.plot(xlabels, values_max, label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (ms)")
    plt.title("Performance of Quicksort Solution")
    plt.show()
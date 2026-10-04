import random
import time
import matplotlib.pyplot as plt
class Quicksort:
    def __init__(self):
        self.mylist1 = []
    def add(self, value):
        self.mylist1.append(value)
    def quick_sort(self):
        if len(self.mylist1) > 1:
            pivot = self.mylist1[0]
            left = [x for x in self.mylist1[1:] if x < pivot]
            right = [x for x in self.mylist1[1:] if x >= pivot]
            return Quicksort._quicksort_helper(left) + [pivot] + Quicksort._quicksort_helper(right)
        else:
            return self.mylist1
    @staticmethod
    def _quicksort_helper(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return Quicksort._quicksort_helper(left) + [pivot] + Quicksort._quicksort_helper(right)
    def get_min(self):
        return min(self.mylist1) if self.mylist1 else None
    def get_max(self):
        return max(self.mylist1) if self.mylist1 else None
    def get_list(self):
        return self.mylist1
def measure_time(quicksort_instance, values):
    total_time_add = 0
    total_time_min = 0
    total_time_max = 0
    for value in values:
        start_time = time.time()
        quicksort_instance.add(value)
        total_time_add += (time.time() - start_time)
        start_time = time.time()
        quicksort_instance.get_min()
        total_time_min += (time.time() - start_time)
        start_time = time.time()
        quicksort_instance.get_max()
        total_time_max += (time.time() - start_time)
    return total_time_add, total_time_min, total_time_max
def main():
    qs = Quicksort()
    initial_values = [5, 7, 3, 9]
    for value in initial_values:
        qs.add(value)
        print(qs.get_list(), qs.get_min(), qs.get_max())
    repetitions = 5
    max_operations = 500
    step = 100
    values_add, values_min, values_max = [], [], []
    for num_operations in range(step, max_operations + 1, step):
        random_values = [random.randint(0, 500) for _ in range(num_operations)]
        total_time_add = total_time_min = total_time_max = 0
        for _ in range(repetitions):
            qs = Quicksort()
            my_add, my_min, my_max = measure_time(qs, random_values)
            total_time_add += my_add
            total_time_min += my_min
            total_time_max += my_max
        avg_time_add = (total_time_add / repetitions) * 1000
        avg_time_min = (total_time_min / repetitions) * 1000
        avg_time_max = (total_time_max / repetitions) * 1000
        values_add.append(avg_time_add)
        values_min.append(avg_time_min)
        values_max.append(avg_time_max)
    x_labels = range(step, max_operations + 1, step)
    plt.plot(x_labels, values_add, label='Add')
    plt.plot(x_labels, values_min, label='Get Min')
    plt.plot(x_labels, values_max, label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (ms)")
    plt.title("Performance of Quicksort Solution")
    plt.show()
if __name__ == '__main__':
    main()
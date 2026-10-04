import random
import time
import matplotlib.pyplot as plt
class BubbleSort:
    def __init__(self):
        self.content = []
    def bubble_sort(self):
        for passnum in range(len(self.content) - 1, 0, -1):
            for i in range(passnum):
                if self.content[i] > self.content[i + 1]:
                    self.content[i], self.content[i + 1] = self.content[i + 1], self.content[i]
    def add(self, value):
        self.content.append(value)
        self.bubble_sort()
    def get_min(self):
        return self.content[0] if self.content else None
    def get_max(self):
        return self.content[-1] if self.content else None
def measure_time(bubble_sort_instance, values_list):
    total_time_add = 0
    total_time_min = 0
    total_time_max = 0
    for num in values_list:
        start = time.time()
        bubble_sort_instance.add(num)
        total_time_add += time.time() - start
        start = time.time()
        min_value = bubble_sort_instance.get_min()
        total_time_min += time.time() - start
        start = time.time()
        max_value = bubble_sort_instance.get_max()
        total_time_max += time.time() - start
    return total_time_add, total_time_min, total_time_max
if __name__ == '__main__':
    bubble_sort_instance = BubbleSort()
    bubble_sort_instance.add(5)
    print(bubble_sort_instance.content, bubble_sort_instance.get_min(), bubble_sort_instance.get_max())
    bubble_sort_instance.add(7)
    print(bubble_sort_instance.content, bubble_sort_instance.get_min(), bubble_sort_instance.get_max())
    bubble_sort_instance.add(3)
    print(bubble_sort_instance.content, bubble_sort_instance.get_min(), bubble_sort_instance.get_max())
    bubble_sort_instance.add(9)
    print(bubble_sort_instance.content, bubble_sort_instance.get_min(), bubble_sort_instance.get_max())
    repetitions = 5
    max_operations = 500
    step = 100
    values_add, values_min, values_max = [], [], []
    for rounds in range(step, max_operations, step):
        current_list = [random.randint(0, 500) for _ in range(rounds)]
        total_time_add, total_time_min, total_time_max = 0, 0, 0
        for _ in range(repetitions):
            instance = BubbleSort()
            time_add, time_min, time_max = measure_time(instance, current_list)
            total_time_add += time_add
            total_time_min += time_min
            total_time_max += time_max
        values_add.append((total_time_add / repetitions) * 1000)
        values_min.append((total_time_min / repetitions) * 1000)
        values_max.append((total_time_max / repetitions) * 1000)
    x_labels = range(step, max_operations, step)
    plt.plot(x_labels, values_add, label='Add')
    plt.plot(x_labels, values_min, label='Get Min')
    plt.plot(x_labels, values_max, label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution Time (ms)")
    plt.title("Performance of BubbleSort")
    plt.show()
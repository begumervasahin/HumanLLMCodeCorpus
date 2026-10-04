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
def measure_time(sort_instance, values):
    total_time_add = 0
    total_time_min = 0
    total_time_max = 0
    for num in values:
        start = time.time()
        sort_instance.add(num)
        total_time_add += (time.time() - start)
        start = time.time()
        _ = sort_instance.get_min()
        total_time_min += (time.time() - start)
        start = time.time()
        _ = sort_instance.get_max()
        total_time_max += (time.time() - start)
    return total_time_add, total_time_min, total_time_max
def main():
    bubble_sort = BubbleSort()
    test_values = [5, 7, 3, 9]
    for value in test_values:
        bubble_sort.add(value)
        print(bubble_sort.content, bubble_sort.get_min(), bubble_sort.get_max())
    repetitions = 3
    max_operations = 500
    step = 100
    add_times = []
    min_times = []
    max_times = []
    for rounds in range(step, max_operations + step, step):
        random_values = [random.randint(0, 500) for _ in range(rounds)]
        avg_add_time = 0
        avg_min_time = 0
        avg_max_time = 0
        for _ in range(repetitions):
            bubble_sort = BubbleSort()
            add_time, min_time, max_time = measure_time(bubble_sort, random_values)
            avg_add_time += add_time
            avg_min_time += min_time
            avg_max_time += max_time
        avg_add_time /= repetitions
        avg_min_time /= repetitions
        avg_max_time /= repetitions
        add_times.append(avg_add_time * 1000)
        min_times.append(avg_min_time * 1000)
        max_times.append(avg_max_time * 1000)
    x_labels = range(step, max_operations + step, step)
    plt.plot(x_labels, add_times, label='Add')
    plt.plot(x_labels, min_times, label='Get Min')
    plt.plot(x_labels, max_times, label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution Time (ms)")
    plt.title("Performance of Bubble Sort Solution")
    plt.show()
if __name__ == '__main__':
    main()
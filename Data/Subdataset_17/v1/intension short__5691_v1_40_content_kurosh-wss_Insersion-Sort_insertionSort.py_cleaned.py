import random
import time
import numpy as np
import matplotlib.pyplot as plt
class InsertionSorter:
    @staticmethod
    def sort(lst):
        for i in range(1, len(lst)):
            key = lst[i]
            j = i - 1
            while j >= 0 and lst[j] > key:
                lst[j + 1] = lst[j]
                j -= 1
            lst[j + 1] = key
class NumberGenerator:
    @staticmethod
    def generate(number_of_lists, min_range, max_range, m, n):
        return [
            [random.randint(m, n) for _ in range(random.randint(min_range, max_range))]
            for _ in range(number_of_lists)
        ]
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
        self.size += 1
    def insert_sorted(self, data):
        if self.head is None:
            self.append(data)
            return
        current = self.head
        while current and current.data < data:
            current = current.next
        new_node = Node(data)
        if current is None:
            self.append(data)
        elif current.prev is None:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            new_node.next = current
            new_node.prev = current.prev
            current.prev.next = new_node
            current.prev = new_node
        self.size += 1
    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    def insertion_sort(self):
        sorted_list = DoublyLinkedList()
        current = self.head
        while current:
            sorted_list.insert_sorted(current.data)
            current = current.next
        self.head = sorted_list.head
def measure_time_sorting(lists, a, b, generator_func, sort_func):
    numbers = generator_func(lists, a, b, 10, 1000)
    numbers.sort(key=len)
    simple_times = []
    linked_list_times = []
    lengths = [len(lst) for lst in numbers]
    for lst in numbers:
        start = time.process_time()
        sort_func(lst)
        simple_times.append(time.process_time() - start)
    for lst in numbers:
        linked_list = DoublyLinkedList()
        for item in lst:
            linked_list.append(item)
        start = time.process_time()
        linked_list.insertion_sort()
        linked_list_times.append(time.process_time() - start)
    return simple_times, linked_list_times, lengths
def plot_results(results, title):
    simple_times, linked_list_times, lengths = results
    ind = np.arange(len(lengths))
    width = 0.35
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind - width / 2, simple_times, width, label='Simple Insertion Sort')
    rects2 = ax.bar(ind + width / 2, linked_list_times, width, label='Linked List Insertion Sort')
    ax.set_ylabel('Time (seconds)')
    ax.set_title(title)
    ax.set_xticks(ind)
    ax.set_xticklabels(lengths)
    ax.legend()
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate(f'{height:.4f}',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom')
    autolabel(rects1)
    autolabel(rects2)
    plt.show()
def main():
    plot_results(measure_time_sorting(100, 1000, 2000, NumberGenerator.generate, InsertionSorter.sort),
                 'Time Table for Linked List and Simple Insertion Sort (Small Ranges)')
    plot_results(measure_time_sorting(100, 1000, 20000, NumberGenerator.generate, lambda x: sorted(x)),
                 'Time Table for Linked List and Simple Insertion Sort (Large Ranges)')
if __name__ == "__main__":
    main()
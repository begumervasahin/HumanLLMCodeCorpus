import random
import time
import numpy as np
import matplotlib.pyplot as plt
from collections import namedtuple
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
def generate_random_lists(num_lists, min_size, max_size, value_min, value_max):
    return [
        [random.randint(value_min, value_max) for _ in range(random.randint(min_size, max_size))]
        for _ in range(num_lists)
    ]
def binary_insert(number, array):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high)
        if array[mid] < number:
            low = mid + 1
        else:
            high = mid - 1
    array.insert(low, number)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
            new_node.prev = last
    def insert_sorted(self, data):
        if not self.head or self.head.data >= data:
            self.push(data)
            return
        current = self.head
        while current.next and current.next.data < data:
            current = current.next
        new_node = Node(data)
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node
    def sort(self):
        sorted_list = DoublyLinkedList()
        current = self.head
        while current:
            sorted_list.insert_sorted(current.data)
            current = current.next
        self.head = sorted_list.head
    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
def measure_sort_times(num_lists, min_size, max_size):
    random_lists = generate_random_lists(num_lists, min_size, max_size, 10, 1000)
    random_lists.sort(key=len)
    list_sizes = [len(lst) for lst in random_lists]
    simple_times = []
    linked_times = []
    for lst in random_lists:
        start = time.perf_counter()
        insertion_sort(lst.copy())
        end = time.perf_counter()
        simple_times.append(end - start)
    for lst in random_lists:
        dll = DoublyLinkedList()
        for item in lst:
            dll.append(item)
        start = time.perf_counter()
        dll.sort()
        end = time.perf_counter()
        linked_times.append(end - start)
    Results = namedtuple('Results', ['simple_times', 'linked_times', 'list_sizes'])
    return Results(simple_times, linked_times, list_sizes)
def measure_binary_sort_times(num_lists, min_size, max_size):
    random_lists = generate_random_lists(num_lists, min_size, max_size, 10, 1000)
    random_lists.sort(key=len)
    list_sizes = [len(lst) for lst in random_lists]
    simple_times = []
    linked_times = []
    for lst in random_lists:
        sorted_list = []
        start = time.perf_counter()
        for item in lst:
            binary_insert(item, sorted_list)
        end = time.perf_counter()
        simple_times.append(end - start)
    for lst in random_lists:
        dll = DoublyLinkedList()
        start = time.perf_counter()
        for item in lst:
            dll.insert_sorted(item)
        end = time.perf_counter()
        linked_times.append(end - start)
    Results = namedtuple('Results', ['simple_times', 'linked_times', 'list_sizes'])
    return Results(simple_times, linked_times, list_sizes)
def plot_sort_times(results):
    indices = np.arange(len(results.list_sizes))
    width = 0.35
    fig, ax = plt.subplots()
    bars1 = ax.bar(indices - width/2, results.simple_times, width, label='Simple Sort')
    bars2 = ax.bar(indices + width/2, results.linked_times, width, label='Linked List Sort')
    ax.set_ylabel('Time (seconds)')
    ax.set_title('Sorting Time Comparison')
    ax.set_xticks(indices)
    ax.set_xticklabels(results.list_sizes)
    ax.legend()
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height:.5f}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom')
    plt.show()
plot_sort_times(measure_sort_times(100, 1000, 2000))
plot_sort_times(measure_binary_sort_times(100, 1000, 20000))
import os
import imageio
import numpy as np
import matplotlib.pyplot as plt
class SortVisualizer:
    def __init__(self):
        self.images = []
        self.figure = plt.figure()
        plt.ion()
        self.counter = 0
        self.save_path = 'sp/'
        if not os.path.exists(self.save_path):
            os.mkdir(self.save_path)
    def merge_sort(self, arr, start, end):
        if end - start < 2:
            return
        mid = (end + start)
        self.merge_sort(arr, start, mid)
        self.merge_sort(arr, mid, end)
        self.merge(arr, start, mid, end)
    def merge(self, arr, start, mid, end):
        left, right = arr[start:mid], arr[mid:end]
        i = j = 0
        for k in range(start, end):
            if j >= len(right) or (i < len(left) and left[i] < right[j]):
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
        self.draw(arr, 'MERGE SORT')
    def quick_sort(self, arr, low, high):
        if low >= high:
            return
        pivot_index = self.partition(arr, low, high)
        self.draw(arr, 'QUICK SORT')
        self.quick_sort(arr, low, pivot_index - 1)
        self.quick_sort(arr, pivot_index + 1, high)
    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i
    def selection_sort(self, arr):
        self.draw(arr, 'SELECTION SORT')
        for i in range(len(arr)):
            min_index = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
            self.draw(arr, 'SELECTION SORT')
    def heap_sort(self, arr):
        n = len(arr)
        for i in range(n
            self.heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)
            self.draw(arr, 'HEAP SORT')
    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)
    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            self.draw(arr, 'INSERTION SORT')
    def shell_sort(self, arr):
        gap = len(arr)
        while gap > 0:
            for i in range(gap, len(arr)):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
                self.draw(arr, 'SHELL SORT')
            gap
    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    self.draw(arr, 'BUBBLE SORT')
    def draw(self, arr, title):
        if len(arr):
            self.counter += 1
            plt.clf()
            plt.bar(range(len(arr)), arr, width=0.3, color='purple')
            plt.title(title)
            plt.savefig(f'{self.save_path}/{self.counter}.png')
            plt.pause(0.01)
    def create_gif(self):
        file_names = sorted(os.listdir(self.save_path), key=lambda x: int(x.split('.')[0]))
        for file_name in file_names:
            file_path = os.path.join(self.save_path, file_name)
            self.images.append(imageio.imread(file_path))
        imageio.mimsave('sort.gif', self.images, fps=8)
if __name__ == '__main__':
    arr = [100 - k for k in range(100)]
    sorter = SortVisualizer()
    sorter.selection_sort(arr.copy())
    sorter.heap_sort(arr.copy())
    sorter.quick_sort(arr.copy(), 0, len(arr) - 1)
    sorter.merge_sort(arr.copy(), 0, len(arr))
    sorter.insertion_sort(arr.copy())
    sorter.shell_sort(arr.copy())
    sorter.bubble_sort(arr.copy())
    sorter.create_gif()
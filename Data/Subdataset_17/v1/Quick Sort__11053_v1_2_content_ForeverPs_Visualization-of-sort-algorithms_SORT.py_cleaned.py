import os
import imageio
import numpy as np
import matplotlib.pyplot as plt
class SortVisualizer:
    def __init__(self):
        self.img = []
        self.fig = plt.figure()
        plt.ion()
        self.count = 0
        self.path = 'sp/'
        if not os.path.exists(self.path):
            os.mkdir(self.path)
    def merge_sort(self, arr, start, end):
        if end - start < 2:
            return
        mid = (end + start)
        self.merge_sort(arr, start, mid)
        self.merge_sort(arr, mid, end)
        self.merge(arr, start, mid, end)
    def merge(self, arr, start, mid, end):
        left = arr[start:mid]
        right = arr[mid:end]
        k = start
        while left and right:
            if left[0] <= right[0]:
                arr[k] = left.pop(0)
            else:
                arr[k] = right.pop(0)
            k += 1
            self.draw(arr, 'MERGE SORT')
        while left:
            arr[k] = left.pop(0)
            k += 1
        while right:
            arr[k] = right.pop(0)
            k += 1
    def quick_sort(self, arr, low, high):
        if low < high:
            p = self.partition(arr, low, high)
            self.quick_sort(arr, low, p - 1)
            self.quick_sort(arr, p + 1, high)
    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        self.draw(arr, 'QUICK SORT')
        return i + 1
    def select_sort(self, arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
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
    def insert_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            self.draw(arr, 'INSERT SORT')
    def shell_sort(self, arr):
        n = len(arr)
        gap = n
        while gap > 0:
            for i in range(gap, n):
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
            self.count += 1
            plt.clf()
            plt.bar(range(len(arr)), arr, width=0.3, color='purple')
            plt.title(title)
            plt.savefig(f'{self.path}{self.count}.png')
            plt.pause(0.01)
    def create_gif(self):
        filenames = sorted(os.listdir(self.path), key=lambda x: int(x.split('.')[0]))
        for filename in filenames:
            self.img.append(imageio.imread(os.path.join(self.path, filename)))
        imageio.mimsave('sort.gif', self.img, fps=8)
if __name__ == '__main__':
    data = [100 - k for k in range(100)]
    visualizer = SortVisualizer()
    visualizer.select_sort(data.copy())
    visualizer.heap_sort(data.copy())
    visualizer.quick_sort(data.copy(), 0, len(data) - 1)
    visualizer.merge_sort(data.copy(), 0, len(data))
    visualizer.insert_sort(data.copy())
    visualizer.shell_sort(data.copy())
    visualizer.bubble_sort(data.copy())
    visualizer.create_gif()
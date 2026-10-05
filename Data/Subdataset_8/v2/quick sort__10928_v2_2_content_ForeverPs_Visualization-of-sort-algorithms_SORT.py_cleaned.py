import os
import imageio
import numpy as np
import matplotlib.pyplot as plt
class SortingVisualizer:
    def __init__(self):
        self.img = []
        self.fig = plt.figure()
        plt.ion()
        self.count = 0
        self.path = 'sort_animations/'
        if not os.path.lexists(self.path):
            os.mkdir(self.path)
    def merge_sort(self, s, start, end):
        if end - start < 2:
            return
        mid = (end - start)
        self.merge_sort(s, start, start + mid)
        self.merge_sort(s, start + mid, end)
        self.merge(start, mid, end, s)
    def merge(self, start, mid, end, s):
        i, j = start, start + mid
        while i < start + mid and j < end:
            if s[i] < s[j]:
                i += 1
            else:
                s.insert(i, s[j])
                j += 1
                s.pop(j)
                self.draw(s, 'MERGE SORT')
    def quick_sort(self, s, low, high):
        if low >= high:
            return
        pivot = s[high]
        left, right = low, high - 1
        while left <= right:
            while left <= right and s[left] < pivot:
                left += 1
            while left <= right and s[right] > pivot:
                right -= 1
            if left <= right:
                s[left], s[right] = s[right], s[left]
                left, right = left + 1, right - 1
        s[left], s[high] = s[high], s[left]
        if left != high:
            self.draw(s, 'QUICK SORT')
        self.quick_sort(s, low, left - 1)
        self.quick_sort(s, left + 1, high)
    def draw(self, s, algorithm_name):
        if len(s):
            self.count += 1
            plt.clf()
            plt.bar(range(len(s)), s, width=0.3, color='purple')
            plt.title(algorithm_name)
            plt.savefig(os.path.join(self.path, str(self.count)))
            plt.pause(0.01)
    def get_gif(self):
        filenames = os.listdir(self.path)
        filenames.sort(key=lambda x: int(x[:-4]))
        for filename in filenames:
            filepath = os.path.join(self.path, filename)
            self.img.append(imageio.imread(filepath))
        imageio.mimsave('sort.gif', self.img, fps=8)
if __name__ == '__main__':
    initial_sequence = [100 - k for k in range(100)]
    sorter = SortingVisualizer()
    sorter.quick_sort(list(initial_sequence), 0, len(initial_sequence) - 1)
    sorter.get_gif()
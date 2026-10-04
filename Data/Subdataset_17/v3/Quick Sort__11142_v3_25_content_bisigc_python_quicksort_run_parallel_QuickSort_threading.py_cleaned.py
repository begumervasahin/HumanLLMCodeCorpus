import threading
import random
import time
def quick_sort(arr, left, right):
    if left < right:
        pivot = arr[left]
        s = left
        for i in range(left + 1, right + 1):
            if arr[i] < pivot:
                s += 1
                arr[s], arr[i] = arr[i], arr[s]
        arr[left], arr[s] = arr[s], arr[left]
        quick_sort(arr, left, s - 1)
        quick_sort(arr, s + 1, right)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
class SortingThread(threading.Thread):
    def __init__(self, threadID, name, arr, left, right):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.arr = arr
        self.left = left
        self.right = right
        self.result = []
    def run(self):
        quick_sort(self.arr, self.left, self.right)
        self.result = self.arr[self.left:self.right + 1]
class MergingThread(threading.Thread):
    def __init__(self, threadID, name, arr, left, right, partitions):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.arr = arr
        self.left = left
        self.right = right
        self.partitions = partitions
        self.result = []
    def run(self):
        mid = self.left + (self.right - self.left)
        if self.partitions == 2:
            t1 = SortingThread(self.threadID + 1, f"SortingThread-{self.threadID + 1}", self.arr, self.left, mid)
            t2 = SortingThread(self.threadID + 2, f"SortingThread-{self.threadID + 2}", self.arr, mid + 1, self.right)
        else:
            t1 = MergingThread(self.threadID + 1, f"MergingThread-{self.threadID + 1}", self.arr, self.left, mid, self.partitions
            t2 = MergingThread(self.threadID + 2, f"MergingThread-{self.threadID + 2}", self.arr, mid + 1, self.right, self.partitions
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        self.result = merge(t1.result, t2.result)
if __name__ == '__main__':
    partitions = 32
    array = list(range(1000000))
    random.shuffle(array)
    start_time = time.time()
    merge_thread = MergingThread(1, "MergingThread-1", array, 0, len(array) - 1, partitions)
    merge_thread.start()
    merge_thread.join()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
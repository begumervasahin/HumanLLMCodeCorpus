import threading
import random
import time
def quickSort(A, l, r):
    if l < r:
        pivot = A[l]
        s = l
        for i in range(l + 1, r + 1):
            if A[i] < pivot:
                s = s + 1
                A[s], A[i] = A[i], A[s]
        A[l], A[s] = A[s], A[l]
        quickSort(A, l, s - 1)
        quickSort(A, s + 1, r)
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
    def __init__(self, threadID, name, A, l, h):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.A = A
        self.l = l
        self.h = h
        self.result = []
    def run(self):
        quickSort(self.A, self.l, self.h)
        self.result = self.A[self.l:self.h + 1]
class MergingThread(threading.Thread):
    def __init__(self, threadID, name, A, l, h, p):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.A = A
        self.l = l
        self.h = h
        self.p = p
        self.result = []
    def run(self):
        mid = self.l + (self.h - self.l)
        if self.p == 2:
            t1 = SortingThread(self.threadID + 1, f"SortingThread-{self.threadID + 1}", self.A, self.l, mid)
            t2 = SortingThread(self.threadID + 2, f"SortingThread-{self.threadID + 2}", self.A, mid + 1, self.h)
        else:
            t1 = MergingThread(self.threadID + 1, f"MergingThread-{self.threadID + 1}", self.A, self.l, mid, self.p
            t2 = MergingThread(self.threadID + 2, f"MergingThread-{self.threadID + 2}", self.A, mid + 1, self.h, self.p
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        self.result = merge(t1.result, t2.result)
if __name__ == '__main__':
    p = 32
    A = list(range(0, 1000000))
    random.shuffle(A)
    start_time = time.time()
    t = MergingThread(1, "MergingThread-1", A, 0, len(A) - 1, p)
    t.start()
    t.join()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
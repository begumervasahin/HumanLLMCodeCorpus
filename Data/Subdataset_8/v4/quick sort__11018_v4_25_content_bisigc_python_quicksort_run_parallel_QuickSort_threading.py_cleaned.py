import threading
import random
import time
from quicksort import quickSort
from merge import merge
class SortingThread(threading.Thread):
    def __init__(self, threadID, name, A, l, h):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.A = A
        self.l = l
        self.h = h
        self.result = list()
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
        self.result = list()
    def run(self):
        i = self.threadID
        m = self.l + (self.h - self.l)
        if self.p == 2:
            t1 = SortingThread(i + 1, f"SortingThread-{i + 1}", self.A, self.l, m)
            t2 = SortingThread(i + 2, f"SortingThread-{i + 2}", self.A, m + 1, self.h)
        else:
            t1 = MergingThread(i + 1, f"MergingThread-{i + 1}", self.A, self.l, m, self.p
            t2 = MergingThread(i + 2, f"MergingThread-{i + 2}", self.A, m + 1, self.h, self.p
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
    t = MergingThread(1, f"MergingThread-{1}", A, 0, len(A) - 1, p)
    t.start()
    t.join()
    end_time = time.time()
    print(f"End time: {end_time}")
    print(f"Elapsed time: {end_time - start_time} seconds")
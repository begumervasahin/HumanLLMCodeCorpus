import threading
import random
import time
from quicksort import quickSort
from merge import merge
class class1(threading.Thread):
    def fonk1(self, b1, b2, b3, b4, b5):
        threading.Thread.fonk3(self)
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = list()
    def fonk2(self):
        quickSort(self.b3, self.b4, self.b5)
        self.b6 = self.b3[self.b4:self.b5 + 1]
class class2(threading.Thread):
    def fonk3(self, b1, b2, b3, b4, b5, b7):
        threading.Thread.fonk3(self)
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b7 = b7
        self.b6 = list()
    def fonk4(self):
        b8 = self.b1
        b9 = self.b4 + (self.b5 - self.b4)
        if self.b7 = = 2:
            b10 = class1(b8 + 1, f"class1-{b8 + 1}", self.b3, self.b4, b9)
            b11 = class1(b8 + 2, f"class1-{b8 + 2}", self.b3, b9 + 1, self.b5)
        else:
            b10 = class2(b8 + 1, f"class2-{b8 + 1}", self.b3, self.b4, b9, self.b7
            b11 = class2(b8 + 2, f"class2-{b8 + 2}", self.b3, b9 + 1, self.b5, self.b7
        b10.start()
        b11.start()
        b10.join()
        b11.join()
        self.b6 = merge(b10.b6, b11.b6)
if b12 = = '__main__':
    b7 = 32
    b3 = list(range(0, 1000000))
    random.shuffle(b3)
    b13 = time.time()
    b14 = class2(1, f"class2-{1}", b3, 0, len(b3) - 1, b7)
    b14.start()
    b14.join()
    b15 = time.time()
    print(f"End time: {b15}")
    print(f"Elapsed time: {b15 - b13} seconds")
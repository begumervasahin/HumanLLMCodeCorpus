import threading
import random
import time
from quicksort import quick_sort
from merge import merge
class class1(threading.Thread):
    def fonk1(self, b1, b2, b3, b4, b5):
        super().fonk3()
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = []
    def fonk2(self):
        quick_sort(self.b3, self.b4, self.b5)
        self.b6 = self.b3[self.b4:self.b5 + 1]
class class2(threading.Thread):
    def fonk3(self, b1, b2, b3, b4, b5, b7):
        super().fonk3()
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b7 = b7
        self.b6 = []
    def fonk4(self):
        b8 = self.b4 + (self.b5 - self.b4)
        if self.b7 = = 2:
            b9 = class1(self.b1 + 1, f"class1-{self.b1 + 1}", self.b3, self.b4, b8)
            b10 = class1(self.b1 + 2, f"class1-{self.b1 + 2}", self.b3, b8 + 1, self.b5)
        else:
            b9 = class2(self.b1 + 1, f"class2-{self.b1 + 1}", self.b3, self.b4, b8, self.b7
            b10 = class2(self.b1 + 2, f"class2-{self.b1 + 2}", self.b3, b8 + 1, self.b5, self.b7
        b9.start()
        b10.start()
        b9.join()
        b10.join()
        self.b6 = merge(b9.b6, b10.b6)
def fonk5():
    b7 = 32
    b3 = list(range(0, 1000000))
    random.shuffle(b3)
    b11 = time.time()
    b12 = class2(1, "class2-1", b3, 0, len(b3) - 1, b7)
    b12.start()
    b12.join()
    b13 = time.time()
    print(f"Execution time: {b13 - b11:.2f} seconds")
if b14 = = '__main__':
    fonk5()
import threading
import random
import time
def fonk1(b7, b8, r):
    if b8 < r:
        b1 = b7[b8]
        b2 = b8
        for b4 in range(b8 + 1, r + 1):
            if b7[b4] < b1:
                b2 = b2 + 1
                b7[b2], b7[b4] = b7[b4], b7[b2]
        b7[b8], b7[b2] = b7[b2], b7[b8]
        fonk1(b7, b8, b2 - 1)
        fonk1(b7, b2 + 1, r)
def fonk2(left, right):
    b3 = []
    b4 = j = 0
    while b4 < len(left) and j < len(right):
        if left[b4] <= right[j]:
            b3.append(left[b4])
            b4 += 1
        else:
            b3.append(right[j])
            j += 1
    b3.extend(left[b4:])
    b3.extend(right[j:])
    return b3
class class1(threading.Thread):
    def fonk3(self, b5, b6, b7, b8, b9):
        threading.Thread.fonk5(self)
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
        self.b8 = b8
        self.b9 = b9
        self.b3 = []
    def fonk4(self):
        fonk1(self.b7, self.b8, self.b9)
        self.b3 = self.b7[self.b8:self.b9 + 1]
class class2(threading.Thread):
    def fonk5(self, b5, b6, b7, b8, b9, b10):
        threading.Thread.fonk5(self)
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
        self.b8 = b8
        self.b9 = b9
        self.b10 = b10
        self.b3 = []
    def fonk6(self):
        b11 = self.b8 + (self.b9 - self.b8)
        if self.b10 = = 2:
            b12 = class1(self.b5 + 1, f"class1-{self.b5 + 1}", self.b7, self.b8, b11)
            b13 = class1(self.b5 + 2, f"class1-{self.b5 + 2}", self.b7, b11 + 1, self.b9)
        else:
            b12 = class2(self.b5 + 1, f"class2-{self.b5 + 1}", self.b7, self.b8, b11, self.b10
            b13 = class2(self.b5 + 2, f"class2-{self.b5 + 2}", self.b7, b11 + 1, self.b9, self.b10
        b12.start()
        b13.start()
        b12.join()
        b13.join()
        self.b3 = fonk2(b12.b3, b13.b3)
if b14 = = '__main__':
    b10 = 32
    b7 = list(range(0, 1000000))
    random.shuffle(b7)
    b15 = time.time()
    b16 = class2(1, "class2-1", b7, 0, len(b7) - 1, b10)
    b16.start()
    b16.join()
    b17 = time.time()
    print(f"Execution time: {b17 - b15} seconds")
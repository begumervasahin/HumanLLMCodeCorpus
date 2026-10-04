import threading
import random
import time
def fonk1(b7, b8, b9):
    if b8 < b9:
        b1 = b7[b8]
        b2 = b8
        for b4 in range(b8 + 1, b9 + 1):
            if b7[b4] < b1:
                b2 += 1
                b7[b2], b7[b4] = b7[b4], b7[b2]
        b7[b8], b7[b2] = b7[b2], b7[b8]
        fonk1(b7, b8, b2 - 1)
        fonk1(b7, b2 + 1, b9)
def fonk2(b8, b9):
    b3 = []
    b4 = j = 0
    while b4 < len(b8) and j < len(b9):
        if b8[b4] <= b9[j]:
            b3.append(b8[b4])
            b4 += 1
        else:
            b3.append(b9[j])
            j += 1
    b3.extend(b8[b4:])
    b3.extend(b9[j:])
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
    b15 = list(range(1000000))
    random.shuffle(b15)
    b16 = time.time()
    b17 = class2(1, "class2-1", b15, 0, len(b15) - 1, b10)
    b17.start()
    b17.join()
    b18 = time.time()
    print(f"Execution time: {b18 - b16} seconds")
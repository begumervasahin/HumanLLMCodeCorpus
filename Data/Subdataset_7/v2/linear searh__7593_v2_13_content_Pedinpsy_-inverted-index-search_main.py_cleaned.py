import os
import time
class class1:
    def fonk1(self, b2, b1 = 'division', b4='linear'):
        self.b2 = b2
        self.b3 = [[] for _ in range(b2)]
        self.b1 = b1
        self.b4 = b4
    def fonk2(self, key):
        if self.b1 = = 'multiplication':
            return self.fonk4(key)
        else:
            return self.fonk3(key)
    def fonk3(self, key):
        return hash(key) % self.b2
    def fonk4(self, key):
        a1 = 0.6180339887
        return int(self.b2 * ((hash(key) * a1) % 1))
    def fonk5(self, key, value):
        b5 = self.fonk2(key)
        if not self.b3[b5]:
            self.b3[b5].append((key, value))
        elif self.b4 = = 'linear':
            b6 = (b5 + 1) % self.b2
            while b6 != b5:
                if not self.b3[b6]:
                    self.b3[b6].append((key, value))
                    return
                b6 = (b6 + 1) % self.b2
            print("Table is full. Couldn't insert:", key)
        elif self.b4 = = 'quadratic':
            a2 = 1
            b6 = (b5 + a2**2) % self.b2
            while b6 != b5:
                if not self.b3[b6]:
                    self.b3[b6].append((key, value))
                    return
                a2 += 1
                b6 = (b5 + a2**2) % self.b2
            print("Table is full. Couldn't insert:", key)
    def fonk6(self, key):
        b5 = self.fonk2(key)
        if self.b3[b5]:
            for b7, v in self.b3[b5]:
                if b7 = = key:
                    return v
        return None
def fonk7(b16):
    b8 = [os.path.join(b16, name) for name in os.listdir(b16)]
    b9 = [path for path in b8 if os.path.isfile(path)]
    return b9
def fonk8(file_list, hashtable):
    for a2, file in enumerate(file_list):
        with open(file, 'r') as f:
            b10 = f.read().lower().replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace("\r", "").replace("\t", "").replace("\n", "").split(" ")
            for b19 in b10:
                b11 = b10.b11(b19)
                hashtable.fonk5(b19, [b11, a2 + 1])
def fonk9():
    b12 = class1(1000000, 'multiplication', 'linear')
    b13 = class1(1000000, 'multiplication', 'quadratic')
    b14 = class1(1000000, 'division', 'linear')
    b15 = class1(1000000, 'division', 'quadratic')
    b16 = 'base'
    b9 = fonk7(b16)
    b17 = time.time()
    fonk8(b9, b12)
    b18 = time.time()
    print("Time for Multiplication Hashing with Linear Collision:", b18 - b17)
    b17 = time.time()
    fonk8(b9, b13)
    b18 = time.time()
    print("Time for Multiplication Hashing with Quadratic Collision:", b18 - b17)
    b17 = time.time()
    fonk8(b9, b14)
    b18 = time.time()
    print("Time for Division Hashing with Linear Collision:", b18 - b17)
    b17 = time.time()
    fonk8(b9, b15)
    b18 = time.time()
    print("Time for Division Hashing with Quadratic Collision:", b18 - b17)
    while True:
        b19 = input("Enter a b19:\n")
        print("Multiplication Linear:", b12.fonk6(b19))
        print("Multiplication Quadratic:", b13.fonk6(b19))
        print("Division Linear:", b14.fonk6(b19))
        print("Division Quadratic:", b15.fonk6(b19))
if b20 = = "__main__":
    fonk9()
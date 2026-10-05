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
            self.fonk6(b5, key, value)
        elif self.b4 = = 'quadratic':
            self.fonk7(b5, key, value)
    def fonk6(self, b5, key, value):
        b6 = (b5 + 1) % self.b2
        while b6 != b5:
            if not self.b3[b6]:
                self.b3[b6].append((key, value))
                return
            b6 = (b6 + 1) % self.b2
        print("Table is full. Couldn't insert:", key)
    def fonk7(self, b5, key, value):
        a2 = 1
        b6 = (b5 + a2**2) % self.b2
        while b6 != b5:
            if not self.b3[b6]:
                self.b3[b6].append((key, value))
                return
            a2 += 1
            b6 = (b5 + a2**2) % self.b2
        print("Table is full. Couldn't insert:", key)
    def fonk8(self, key):
        b5 = self.fonk2(key)
        for b7, v in self.b3[b5]:
            if b7 = = key:
                return v
        return None
def fonk9(b14):
    return [os.path.join(b14, name) for name in os.listdir(b14) if os.path.isfile(os.path.join(b14, name))]
def fonk10(file_list, hashtable):
    for a2, file in enumerate(file_list):
        with open(file, 'r') as f:
            b8 = f.read().lower().replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace("\r", "").replace("\t", "").replace("\n", "").split(" ")
            for b18 in b8:
                b9 = b8.b9(b18)
                hashtable.fonk5(b18, [b9, a2 + 1])
def fonk11():
    b10 = class1(1000000, b1='multiplication', b4='linear')
    b11 = class1(1000000, b1='multiplication', b4='quadratic')
    b12 = class1(1000000, b1='division', b4='linear')
    b13 = class1(1000000, b1='division', b4='quadratic')
    b14 = 'base'
    b15 = fonk9(b14)
    for hashtable, b1, b4 in [(b10, 'Multiplication', 'Linear'),
                                         (b11, 'Multiplication', 'Quadratic'),
                                         (b12, 'Division', 'Linear'),
                                         (b13, 'Division', 'Quadratic')]:
        b16 = time.time()
        fonk10(b15, hashtable)
        b17 = time.time()
        print(f"Time for {b1} Hashing with {b4} Collision: {b17 - b16}")
    while True:
        b18 = input("Enter a b18:\n")
        print("Multiplication Linear:", b10.fonk8(b18))
        print("Multiplication Quadratic:", b11.fonk8(b18))
        print("Division Linear:", b12.fonk8(b18))
        print("Division Quadratic:", b13.fonk8(b18))
if b19 = = "__main__":
    fonk11()
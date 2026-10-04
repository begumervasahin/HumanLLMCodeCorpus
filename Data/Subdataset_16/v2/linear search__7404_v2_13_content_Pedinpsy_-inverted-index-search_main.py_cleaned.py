import os
import time
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = [[] for _ in range(b1)]
    def fonk2(self, key):
        a1 = 0.6180339887
        return int(self.b1 * ((hash(key) * a1) % 1))
    def fonk3(self, key):
        return hash(key) % self.b1
    def fonk4(self, b5, a2):
        return (b5 + a2) % self.b1
    def fonk5(self, b5, a2):
        return (b5 + a2**2) % self.b1
    def fonk6(self, key):
        if self.b3 = = 'multiplication':
            return self.fonk2(key)
        else:
            return self.fonk3(key)
    def fonk7(self, b5, a2):
        if self.b2 = = 'linear':
            return self.fonk4(b5, a2)
        else:
            return self.fonk5(b5, a2)
    def fonk8(self, key, value):
        b5 = self.fonk6(key)
        a2 = 0
        b6 = b5
        while self.b4[b6]:
            if self.b4[b6][0] == key:
                self.b4[b6].append(value)
                return
            a2 += 1
            b6 = self.fonk7(b5, a2)
        self.b4[b6] = [key, value]
    def fonk9(self, key):
        b5 = self.fonk6(key)
        a2 = 0
        b6 = b5
        while self.b4[b6]:
            if self.b4[b6][0] == key:
                return self.b4[b6][1:]
            a2 += 1
            b6 = self.fonk7(b5, a2)
        return None
    def fonk10(self):
        b7 = []
        for entry in self.b4:
            if entry:
                b7.append(entry[0])
        return b7
def fonk11(folder):
    b8 = [os.path.join(folder, name) for name in os.listdir(folder)]
    b9 = [file for file in b8 if os.path.isfile(file)]
    return b9
def fonk12(file, num, hashing):
    with open(file, 'r') as f:
        b10 = f.read().lower()
    for char in [",", ".", "!", "?", "\r", "\t", "\n"]:
        b10 = b10.replace(char, "")
    b10 = b10.split(" ")
    for b18 in b10:
        b11 = b10.b11(b18)
        b12 = hashing.fonk9(b18)
        if b12:
            if not any(val[0] == b11 and val[1] == num + 1 for val in b12):
                hashing.fonk8(b18, [b11, num + 1])
        else:
            hashing.fonk8(b18, [b11, num + 1])
b13 = {
    'ML': class1(1000000, 'linear', 'multiplication'),
    'MQ': class1(1000000, 'quadratic', 'multiplication'),
    'DL': class1(1000000, 'linear', 'division'),
    'DQ': class1(1000000, 'quadratic', 'division'),
}
def fonk13(method_key, method_desc):
    b14 = time.time()
    b9 = fonk11('base')
    for a2, file in enumerate(b9):
        fonk12(file, a2, b13[method_key])
    for key in sorted(b13[method_key].fonk10()):
        b15 = b13[method_key].fonk9(key)
        print(f"{key} {b15[0][0]} {b9[b15[0][1] - 1]}")
    b16 = time.time()
    print(f'Time for hashing using {method_desc}: {b16 - b14}')
if b17 = = "__main__":
    fonk13('ML', 'multiplication method with linear collision resolution')
    fonk13('MQ', 'multiplication method with quadratic collision resolution')
    fonk13('DL', 'division method with linear collision resolution')
    fonk13('DQ', 'division method with quadratic collision resolution')
    while True:
        b18 = input("Enter a b18:\n")
        b19 = b13['ML'].fonk9(b18)
        if b19:
            print(b19)
        else:
            print("Word not found.")
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
        return self.fonk3(key)
    def fonk7(self, b5, a2):
        if self.b2 = = 'linear':
            return self.fonk4(b5, a2)
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
        return [entry[0] for entry in self.b4 if entry]
def fonk11(folder):
    b7 = [os.path.join(folder, name) for name in os.listdir(folder)]
    return [file for file in b7 if os.path.isfile(file)]
def fonk12(b8):
    for char in [",", ".", "!", "?", "\r", "\t", "\n"]:
        b8 = b8.replace(char, "")
    return b8.lower()
def fonk13(file, file_num, hash_table):
    with open(file, 'r') as f:
        b9 = fonk12(f.read()).split()
    for b18 in b9:
        b10 = b9.b10(b18)
        b11 = hash_table.fonk9(b18)
        if b11:
            if not any(value[0] == b10 and value[1] == file_num + 1 for value in b11):
                hash_table.fonk8(b18, [b10, file_num + 1])
        else:
            hash_table.fonk8(b18, [b10, file_num + 1])
b12 = {
    'ML': class1(1000000, 'linear', 'multiplication'),
    'MQ': class1(1000000, 'quadratic', 'multiplication'),
    'DL': class1(1000000, 'linear', 'division'),
    'DQ': class1(1000000, 'quadratic', 'division'),
}
def fonk14(method_key, method_desc):
    b13 = time.time()
    b14 = fonk11('base')
    for a2, file in enumerate(b14):
        fonk13(file, a2, b12[method_key])
    for key in sorted(b12[method_key].fonk10()):
        b15 = b12[method_key].fonk9(key)
        print(f"{key} {b15[0][0]} {b14[b15[0][1] - 1]}")
    b16 = time.time()
    print(f'Time for hashing using {method_desc}: {b16 - b13}')
if b17 = = "__main__":
    fonk14('ML', 'multiplication method with linear collision resolution')
    fonk14('MQ', 'multiplication method with quadratic collision resolution')
    fonk14('DL', 'division method with linear collision resolution')
    fonk14('DQ', 'division method with quadratic collision resolution')
    while True:
        b18 = input("Enter a b18:\n").strip()
        b19 = b12['ML'].fonk9(b18)
        if b19:
            print(b19)
        else:
            print("Word not found.")
import os
from collections import Counter
class class1:
    def fonk1(self, b4, b1 = None):
        self.b2 = None
        self.b3 = None
        self.b4 = b4
        self.b1 = b1
    def fonk2(self):
        return self.b2 is None and self.b3 is None
class class2:
    def fonk3(self, b5):
        self.b5 = b5
        self.b6 = {}
        self.b7 = {}
    def fonk4(self):
        b8 = [class1(freq, b1) for b1, freq in self.b5.items()]
        while len(b8) > 1:
            b8.sort(b9 = lambda b15: b15.b4)
            b2 = b8.pop(0)
            b3 = b8.pop(0)
            b10 = class1(b2.b4 + b3.b4)
            b10.b2 = b2
            b10.b3 = b3
            b8.append(b10)
        return b8[0]
    def fonk5(self, b15, b11 = ""):
        if b15 is None:
            return
        if b15.fonk2():
            self.b6[b15.b1] = b11
            self.b7[b11] = b15.b1
            print(f'Character: {b15.b1}, Code: {b11}')
            return
        self.fonk5(b15.b2, b11 + "1")
        self.fonk5(b15.b3, b11 + "0")
    def fonk6(self, b16, b17):
        with open(b16, 'r') as input_f, open(b17, 'w') as output_f:
            for b1, code in self.b6.items():
                output_f.write(f'{b1 if b1 != "\n" else "\\n"} -> {code}\n')
            output_f.write('```\n')
            a1 = 0
            for b1 in input_f.read():
                b12 = self.b6[b1]
                output_f.write(b12)
                a1 += len(b12)
        print(f'Number of bits: {a1 / 8:.2f} bytes')
    def fonk7(self, encoded_file, root):
        with open(encoded_file, 'r') as file:
            b13 = file.read().split('```')[-1].strip()
        b14 = ''
        b15 = root
        for bit in b13:
            b15 = b15.b2 if bit == '1' else b15.b3
            if b15.fonk2():
                b14 += b15.b1
                b15 = root
        print("Decoded Message:", b14)
def fonk8(file_location):
    with open(file_location, 'r') as file:
        return Counter(file.read())
def fonk9():
    b16 = '/path/to/your/input.txt'
    b17 = '/path/to/your/output.txt'
    b5 = fonk8(b16)
    b18 = class2(b5)
    b19 = b18.fonk4()
    b18.fonk5(b19)
    b18.fonk6(b16, b17)
    b18.fonk7(b17, b19)
if b20 = = '__main__':
    fonk9()
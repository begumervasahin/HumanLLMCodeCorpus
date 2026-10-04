import os
class class1:
    def fonk1(self, b2, b1 = None):
        self.b2 = b2
        self.b1 = b1
        self.b3 = None
        self.b4 = None
    def fonk2(self):
        return self.b3 is None and self.b4 is None
class class2:
    def fonk3(self, b5):
        self.b5 = b5
        self.b6 = {}
        self.b7 = {}
        self.b8 = self.fonk4()
    def fonk4(self):
        b9 = [class1(freq, b1) for b1, freq in self.b5.items()]
        while len(b9) > 1:
            b9.sort(b10 = lambda b12: b12.b2)
            b3 = b9.pop(0)
            b4 = b9.pop(0)
            b11 = class1(b3.b2 + b4.b2)
            b11.b3 = b3
            b11.b4 = b4
            b9.append(b11)
        return b9[0] if b9 else None
    def fonk5(self, b12 = None, code=""):
        if b12 is None:
            b12 = self.b8
        if b12.fonk2():
            self.b6[b12.b1] = code
            self.b7[code] = b12.b1
            print(f"Character: {repr(b12.b1)}, Code: {code}")
        else:
            self.fonk5(b12.b3, code + "0")
            self.fonk5(b12.b4, code + "1")
    def fonk6(self, b15):
        b13 = self.b8
        b14 = []
        for bit in b15:
            b13 = b13.b3 if bit == '0' else b13.b4
            if b13.fonk2():
                b14.append(b13.b1)
                b13 = self.b8
        return ''.join(b14)
    def fonk7(self, b17, b18):
        with open(b17, 'r') as infile, open(b18, 'w') as outfile:
            for code, b1 in self.b7.items():
                outfile.write(f"{code}.-.{repr(b1)}\n")
            outfile.write("```\n")
            while (b1 := infile.read(1)):
                outfile.write(self.b6[b1])
    def fonk8(self, encoded_path):
        with open(encoded_path, 'r') as file:
            for line in file:
                if line.strip() == "```":
                    break
            b15 = file.read()
            b16 = self.fonk6(b15)
            print("\nDecoded Message:", b16)
            return b16
def fonk9(file_path):
    b5 = {}
    with open(file_path, 'r') as file:
        while (b1 := file.read(1)):
            b5[b1] = b5.get(b1, 0) + 1
    return b5
def fonk10():
    b17 = 'path/to/your/input.txt'
    b18 = 'path/to/your/output.txt'
    b19 = fonk9(b17)
    b20 = class2(b19)
    b20.fonk5()
    b20.fonk7(b17, b18)
    print("\nReverse Dictionary:", b20.b7)
    b20.fonk8(b18)
if b21 = = "__main__":
    fonk10()
import os
from collections import Counter
class class1:
    def fonk1(self, b2, b3, b1 = '', b4=None, b5=None):
        self.b2 = b2
        self.b3 = b3
        self.b1 = b1
        self.b4 = b4
        self.b5 = b5
    def fonk2(self):
        return repr((self.b2, self.b3, self.b1))
    def fonk3(self):
        return self.b4 is None and self.b5 is None
class class2:
    def fonk4(self, b7):
        if b7 is None:
            return
        if b7.b4 is not None:
            b7.b4.b1 = b7.b1 + '1'
            self.fonk4(b7.b4)
        if b7.b5 is not None:
            b7.b5.b1 = b7.b1 + '0'
            self.fonk4(b7.b5)
    def fonk5(self, b7, character):
        if b7.b2 = = character:
            return b7.b1
        if b7.b4:
            b6 = self.fonk5(b7.b4, character)
            if b6:
                return b6
        if b7.b5:
            b6 = self.fonk5(b7.b5, character)
        return b6
    def fonk6(self, b7, b9):
        return ''.join(self.fonk5(b7, char) for char in b9)
    def fonk7(self, b10, binary_text):
        b7 = b10
        b8 = ''
        for bit in binary_text:
            b7 = b7.b4 if bit == '1' else b7.b5
            if b7.fonk3():
                b8 += b7.b2
                b7 = b10
        return b8
    def fonk8(self, b7):
        if b7 is None:
            return
        if b7.b4:
            self.fonk8(b7.b4)
        if b7.fonk3():
            print(b7)
        if b7.b5:
            self.fonk8(b7.b5)
class class3:
    def fonk9(self, b9):
        self.b9 = b9
        self.b10 = None
    def fonk10(self, b12):
        self.b10 = [b12]
    def fonk11(self, b12):
        for b7 in self.b10:
            if b7.b2 = = b12.b2:
                b7.b3 += 1
                self.b10.sort(b11 = lambda b7: b7.b3)
                return
        self.b10.append(b12)
        self.b10.sort(b11 = lambda b7: b7.b3)
    def fonk12(self):
        for char in self.b9:
            if self.b10 is None:
                self.fonk10(class1(char, 1))
            else:
                self.fonk11(class1(char, 1))
    def fonk13(self):
        self.fonk12()
        while len(self.b10) > 1:
            b4 = self.b10.pop(0)
            b5 = self.b10.pop(0)
            b12 = class1('', b4.b3 + b5.b3, b4=b4, b5=b5)
            self.b10.append(b12)
            self.b10.sort(b11 = lambda b7: b7.b3)
def fonk14(b9):
    return Counter(b9)
def fonk15(b13):
    if not os.path.isfile(b13):
        print("File not found!")
        exit()
    with open(b13, "r") as file:
        return file.read()
def fonk16(b13, b2):
    try:
        with open(b13, 'w') as file:
            file.write(b2)
    except IOError:
        print("Error creating the file!")
def fonk17():
    print("Please enter the file name containing the b9 to be compressed:")
    b13 = input("File Name: ")
    b9 = fonk15(b13)
    b14 = list(b9)
    b15 = class2()
    b16 = class3(b14)
    b16.fonk13()
    b15.fonk4(b16.b10[0])
    print("------------------- HUFFMAN CODING EXECUTION -------------------")
    print("Original Text:", b9)
    print("")
    print("Character Frequencies:")
    b17 = fonk14(b14)
    print(b17)
    print("")
    print("Huffman Tree created successfully!")
    print("")
    print("Huffman Table:")
    b15.fonk8(b16.b10[0])
    print("")
    b1 = b15.fonk6(b16.b10[0], b9)
    print("Text compressed to binary:", b1)
    print("")
    b8 = b15.fonk7(b16.b10[0], b1)
    print("Decompressed Text:", b8)
    print("")
    b18 = (f"Original Text: {b9}\n"
                      f"Compressed Binary: {b1}\n"
                      f"Decompressed Text: {b8}\n")
    fonk16("result.txt", b18)
    print("Output file generated successfully!")
if b19 = = '__main__':
    fonk17()
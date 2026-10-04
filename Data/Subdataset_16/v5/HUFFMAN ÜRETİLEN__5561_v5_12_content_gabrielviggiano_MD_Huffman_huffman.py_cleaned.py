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
        return f"class1(b2 = '{self.b2}', b3={self.b3}, b1='{self.b1}')"
    def fonk3(self):
        return self.b4 is None and self.b5 is None
class class2:
    def fonk4(self, b7):
        if b7 is None:
            return
        if b7.b4:
            b7.b4.b1 = b7.b1 + '1'
            self.fonk4(b7.b4)
        if b7.b5:
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
            return self.fonk5(b7.b5, character)
        return None
    def fonk6(self, b7, b9):
        return ''.join(self.fonk5(b7, char) for char in b9)
    def fonk7(self, root, binary_text):
        b7 = root
        b8 = ''
        for bit in binary_text:
            b7 = b7.b4 if bit == '1' else b7.b5
            if b7.fonk3():
                b8 += b7.b2
                b7 = root
        return b8
    def fonk8(self, b7):
        if b7 is None:
            return
        if b7.b4:
            self.fonk8(b7.b4)
        if b7.fonk3():
            print(f"Character: '{b7.b2}', Code: {b7.b1}")
        if b7.b5:
            self.fonk8(b7.b5)
class class3:
    def fonk9(self, b9):
        self.b9 = b9
        self.b10 = []
    def fonk10(self):
        b3 = Counter(self.b9)
        self.b10 = [class1(char, freq) for char, freq in b3.items()]
        self.b10.sort(b11 = lambda b7: b7.b3)
    def fonk11(self):
        self.fonk10()
        while len(self.b10) > 1:
            b4 = self.b10.pop(0)
            b5 = self.b10.pop(0)
            b12 = class1('', b4.b3 + b5.b3, b4=b4, b5=b5)
            self.b10.append(b12)
            self.b10.sort(b11 = lambda b7: b7.b3)
def fonk12(b13):
    if not os.path.isfile(b13):
        raise FileNotFoundError(f"File not found: {b13}")
    with open(b13, 'r') as file:
        return file.read()
def fonk13(b13, b2):
    with open(b13, 'w') as file:
        file.write(b2)
def fonk14():
    b13 = input("Please enter the file name containing the b9 to be compressed: ")
    b9 = fonk12(b13)
    b14 = class2()
    b15 = class3(b9)
    b15.fonk11()
    b14.fonk4(b15.b10[0])
    print("\n------------------- HUFFMAN CODING EXECUTION -------------------")
    print("Original Text:", b9)
    print("\nCharacter Frequencies:", Counter(b9))
    print("\nHuffman Tree created successfully!")
    print("\nHuffman Table:")
    b14.fonk8(b15.b10[0])
    b1 = b14.fonk6(b15.b10[0], b9)
    print("\nText compressed to binary:", b1)
    b8 = b14.fonk7(b15.b10[0], b1)
    print("\nDecompressed Text:", b8)
    b16 = (f"Original Text: {b9}\n"
                      f"Compressed Binary: {b1}\n"
                      f"Decompressed Text: {b8}\n")
    fonk13("result.txt", b16)
    print("\nOutput file generated successfully!")
if b17 = = '__main__':
    fonk14()
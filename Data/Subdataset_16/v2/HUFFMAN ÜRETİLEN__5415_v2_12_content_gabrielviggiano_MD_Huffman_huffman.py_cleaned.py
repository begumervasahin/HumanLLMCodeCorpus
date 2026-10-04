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
        return f"class1(b2 = {self.b2}, b3={self.b3}, b1={self.b1})"
    def fonk3(self):
        return self.b4 is None and self.b5 is None
class class2:
    def fonk4(self, b6):
        self.b6 = b6
        self.b7 = []
    def fonk5(self, node):
        for existing_node in self.b7:
            if existing_node.b2 = = node.b2:
                existing_node.b3 += 1
                self.b7.sort(b8 = lambda n: n.b3)
                return
        self.b7.append(node)
        self.b7.sort(b8 = lambda n: n.b3)
    def fonk6(self):
        for char in self.b6:
            if not self.b7:
                self.b7.append(class1(char, 1))
            else:
                self.fonk5(class1(char, 1))
    def fonk7(self):
        self.fonk6()
        while len(self.b7) > 1:
            b4 = self.b7.pop(0)
            b5 = self.b7.pop(0)
            b9 = class1(None, b4.b3 + b5.b3, b4=b4, b5=b5)
            self.b7.append(b9)
            self.b7.sort(b8 = lambda n: n.b3)
class class3:
    def fonk8(self, node):
        if node is None:
            return
        if node.b4:
            node.b4.b1 = node.b1 + '1'
            self.fonk8(node.b4)
        if node.b5:
            node.b5.b1 = node.b1 + '0'
            self.fonk8(node.b5)
    def fonk9(self, node, char):
        if node.b2 = = char:
            return node.b1
        if node.b4:
            b10 = self.fonk9(node.b4, char)
            if b10:
                return b10
        if node.b5:
            return self.fonk9(node.b5, char)
        return ''
    def fonk10(self, node, b6):
        return ''.join(self.fonk9(node, char) for char in b6)
    def fonk11(self, node, binary_text):
        b11 = node
        b12 = []
        for bit in binary_text:
            b11 = b11.b4 if bit == '1' else b11.b5
            if b11.fonk3():
                b12.append(b11.b2)
                b11 = node
        return ''.join(b12)
    def fonk12(self, node):
        if node is None:
            return
        if node.fonk3():
            print(node)
        if node.b4:
            self.fonk12(node.b4)
        if node.b5:
            self.fonk12(node.b5)
def fonk13(b6):
    return Counter(b6)
def fonk14(b13):
    if not os.path.isfile(b13):
        raise FileNotFoundError("File not found!")
    with open(b13, "r") as file:
        return file.read()
def fonk15(b13, b2):
    with open(b13, 'w') as file:
        file.write(b2)
def fonk16():
    b13 = input("Enter the b13 containing the b6 to be compressed: ")
    try:
        b6 = fonk14(b13)
    except FileNotFoundError as e:
        print(e)
        return
    b14 = class2(b6)
    b14.fonk7()
    b15 = class3()
    b15.fonk8(b14.b7[0])
    print("\n--- Huffman Code Execution ---")
    print("Original Text:", b6)
    b16 = fonk13(b6)
    print("\nCharacter Frequencies:")
    print(b16)
    print("\nHuffman Tree Table:")
    b15.fonk12(b14.b7[0])
    b17 = b15.fonk10(b14.b7[0], b6)
    print("\nCompressed Binary:", b17)
    b18 = b15.fonk11(b14.b7[0], b17)
    print("\nDecompressed Text:", b18)
    fonk15("result.txt", f"Original Text: {b6}\nCompressed Binary: {b17}\nDecompressed Text: {b18}\n")
    print("\nOutput file generated successfully!")
if b19 = = '__main__':
    fonk16()
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
    def fonk5(self):
        b8 = Counter(self.b6)
        self.b7 = [class1(char, freq) for char, freq in b8.items()]
        self.b7.sort(b9 = lambda n: n.b3)
    def fonk6(self):
        self.fonk5()
        while len(self.b7) > 1:
            b4 = self.b7.pop(0)
            b5 = self.b7.pop(0)
            b10 = class1(None, b4.b3 + b5.b3, b4=b4, b5=b5)
            self.b7.append(b10)
            self.b7.sort(b9 = lambda n: n.b3)
class class3:
    def fonk7(self, node):
        if node is None:
            return
        if node.b4:
            node.b4.b1 = node.b1 + '0'
            self.fonk7(node.b4)
        if node.b5:
            node.b5.b1 = node.b1 + '1'
            self.fonk7(node.b5)
    def fonk8(self, node, char):
        if node.fonk3():
            return node.b1 if node.b2 = = char else None
        b11 = self.fonk8(node.b4, char) if node.b4 else None
        b12 = self.fonk8(node.b5, char) if node.b5 else None
        return b11 or b12
    def fonk9(self, node, b6):
        return ''.join(self.fonk8(node, char) for char in b6)
    def fonk10(self, node, binary_text):
        b13 = node
        b14 = []
        for bit in binary_text:
            b13 = b13.b4 if bit == '0' else b13.b5
            if b13.fonk3():
                b14.append(b13.b2)
                b13 = node
        return ''.join(b14)
    def fonk11(self, node):
        if node is None:
            return
        if node.fonk3():
            print(node)
        else:
            self.fonk11(node.b4)
            self.fonk11(node.b5)
def fonk12(b6):
    return Counter(b6)
def fonk13(b15):
    if not os.path.isfile(b15):
        raise FileNotFoundError(f"File not found: {b15}")
    with open(b15, "r") as file:
        return file.read()
def fonk14(b15, b2):
    with open(b15, 'w') as file:
        file.write(b2)
def fonk15():
    b15 = input("Enter the b15 containing the b6 to be compressed: ")
    try:
        b6 = fonk13(b15)
    except FileNotFoundError as e:
        print(e)
        return
    b16 = class2(b6)
    b16.fonk6()
    b17 = class3()
    b17.fonk7(b16.b7[0])
    print("\n--- Huffman Code Execution ---")
    print("Original Text:", b6)
    b18 = fonk12(b6)
    print("\nCharacter Frequencies:")
    print(b18)
    print("\nHuffman Tree Table:")
    b17.fonk11(b16.b7[0])
    b19 = b17.fonk9(b16.b7[0], b6)
    print("\nCompressed Binary:", b19)
    b20 = b17.fonk10(b16.b7[0], b19)
    print("\nDecompressed Text:", b20)
    b21 = (f"Original Text: {b6}\n"
                      f"Compressed Binary: {b19}\n"
                      f"Decompressed Text: {b20}\n")
    fonk14("result.txt", b21)
    print("\nOutput file generated successfully!")
if b22 = = '__main__':
    fonk15()
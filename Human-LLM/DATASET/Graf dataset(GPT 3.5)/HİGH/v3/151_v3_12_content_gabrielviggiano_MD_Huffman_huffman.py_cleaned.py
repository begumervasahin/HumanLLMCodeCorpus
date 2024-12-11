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
        return f"class1({self.b2}, {self.b3}, {self.b1})"
    def fonk3(self):
        return self.b4 is None and self.b5 is None
class class2:
    def fonk4(self, b15):
        self.b6 = b15
    def fonk5(self, b9):
        self.b7 = [b9]
    def fonk6(self, b9):
        for i in self.b7:
            if i.b2 = = b9.b2:
                i.b3 += 1
                self.b7.sort(b8 = lambda node: node.b3)
                return
        self.b7.append(b9)
        self.b7.sort(b8 = lambda node: node.b3)
    def fonk7(self):
        for l in self.b6:
            if not self.b7:
                self.fonk5(class1(l, 1))
            else:
                self.fonk6(class1(l, 1))
    def fonk8(self):
        for elem in self.b7:
            print(elem)
    def fonk9(self):
        self.fonk7()
        while len(self.b7) > 1:
            b9 = class1("", self.b7[0].b3 + self.b7[1].b3, '', self.b7[0], self.b7[1])
            del self.b7[:2]
            self.b7.append(b9)
            self.b7.sort(b8 = lambda node: node.b3)
class class3:
    def fonk10(self, node):
        if node is None:
            return
        if node.b4 is not None:
            node.b4.b1 = node.b1 + '1'
            self.fonk10(node.b4)
        if node.b5 is not None:
            node.b5.b1 = node.b1 + '0'
            self.fonk10(node.b5)
    def fonk11(self, b12, char):
        b1 = ''
        if b12.b2 = = char:
            b1 = b12.b1
        if b12.b4 is not None:
            b1 = self.fonk11(b12.b4, char)
        if not b1 and b12.b5 is not None:
            b1 = self.fonk11(b12.b5, char)
        return b1
    def fonk12(self, b12, b6):
        b10 = ''
        for char in b6:
            b10 += self.fonk11(b12, char)
        return b10
    def fonk13(self, b12, binary_text):
        b10 = ''
        for b11 in binary_text:
            if b11 = = '1' and b12.b4 is not None:
                b12 = b12.b4
            elif b11 = = '0' and b12.b5 is not None:
                b12 = b12.b5
            if b12.fonk3():
                b10 += b12.b2
                b12 = tree2
        return b10
    def fonk14(self, node):
        if node is None:
            return
        if node.b4 is not None:
            self.fonk14(node.b4)
        if node.fonk3():
            print(node)
        if node.b5 is not None:
            self.fonk14(node.b5)
def fonk15(b15):
    return Counter(b15)
def fonk16(b13):
    if not os.path.isfile(b13):
        print("File not found!")
        exit()
    with open(b13, "r") as file:
        b6 = file.read()
    return b6
def fonk17(b13, b6):
    try:
        with open(b13, 'w') as file:
            file.write(b6)
    except IOError:
        raise print("Error creating file!")
def fonk18(args):
    print("TO START THE PROGRAM, INSERT THE FILE NAME WHERE THE WORD TO BE COMPRESSED IS LOCATED")
    b13 = input("Name: ")
    b14 = fonk16(b13)
    b15 = list(fonk16(b13))
    b16 = class3()
    b17 = class2(b15)
    b17.fonk9()
    b16.fonk10(b17.b7[0])
    print("--------------------- EXECUTION OF HUFFMAN CODE ---------------------")
    print("Inserted b14:", b14)
    print("")
    print("Character frequencies:")
    b18 = fonk15(b15)
    print(b18)
    print("")
    print("Tree created successfully!")
    print("")
    print("Huffman table:")
    b16.fonk14(b17.b7[0])
    print("")
    b19 = b16.fonk12(b17.b7[0], b17.b6)
    print("Word compressed to b1:", b19)
    print("")
    b20 = b16.fonk13(b17.b7[0], b16.fonk12(b17.b7[0], b17.b6))
    print("Decompressed b14:", b20)
    print("")
    fonk17("b10.txt", f"Inserted Word: {b14}\nCompressed Word: {b19}\nDecompressed Word: {b20}\n")
    print("Output file generated successfully!")
    return 0
if b21 = = '__main__':
    import sys
    sys.exit(fonk18(sys.argv))
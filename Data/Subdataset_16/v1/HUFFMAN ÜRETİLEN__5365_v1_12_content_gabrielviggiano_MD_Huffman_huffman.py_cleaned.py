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
    def fonk4(self, b6):
        self.b6 = b6
        self.b7 = None
    def fonk5(self, new_node):
        self.b7 = [new_node]
    def fonk6(self, new_node):
        for node in self.b7:
            if node.b2 = = new_node.b2:
                node.b3 += 1
                self.b7 = sorted(self.b7, key=lambda x: x.b3)
                return
        self.b7.append(new_node)
        self.b7 = sorted(self.b7, key=lambda x: x.b3)
    def fonk7(self):
        for char in self.b6:
            if not self.b7:
                self.fonk5(class1(char, 1, ''))
            else:
                self.fonk6(class1(char, 1, ''))
    def fonk8(self):
        self.fonk7()
        while len(self.b7) > 1:
            b8 = self.b7.pop(0)
            b9 = self.b7.pop(0)
            b10 = class1("", b8.b3 + b9.b3, '', b8, b9)
            self.b7.append(b10)
            self.b7 = sorted(self.b7, key=lambda x: x.b3)
class class3:
    def fonk9(self, node):
        if node is None:
            return
        if node.b4:
            node.b4.b1 = node.b1 + '1'
            self.fonk9(node.b4)
        if node.b5:
            node.b5.b1 = node.b1 + '0'
            self.fonk9(node.b5)
    def fonk10(self, tree, char):
        if tree.b2 = = char:
            return tree.b1
        b1 = ''
        if tree.b4:
            b1 = self.fonk10(tree.b4, char)
        if b1 = = '' and tree.b5:
            b1 = self.fonk10(tree.b5, char)
        return b1
    def fonk11(self, tree, b6):
        return ''.join([self.fonk10(tree, char) for char in b6])
    def fonk12(self, tree, binary_text):
        b11 = tree
        b12 = ''
        for b13 in binary_text:
            if b13 = = '1':
                b11 = b11.b4
            else:
                b11 = b11.b5
            if b11.fonk3():
                b12 += b11.b2
                b11 = tree
        return b12
    def fonk13(self, node):
        if node is None:
            return
        if node.b4:
            self.fonk13(node.b4)
        if node.fonk3():
            print(node)
        if node.b5:
            self.fonk13(node.b5)
def fonk14(b6):
    return Counter(b6)
def fonk15(b14):
    if not os.path.isfile(b14):
        print("File not found!")
        exit()
    else:
        with open(b14, "r") as file:
            return file.read()
def fonk16(b14, b2):
    try:
        with open(b14, 'w') as file:
            file.write(b2)
    except IOError:
        print("Error creating the file!")
def fonk17():
    print("TO START THE PROGRAM, ENTER THE NAME OF THE FILE CONTAINING THE TEXT TO BE COMPRESSED")
    b14 = input("Filename: ")
    b6 = fonk15(b14)
    b15 = list(b6)
    b16 = class3()
    b17 = class2(b15)
    b17.fonk8()
    b16.fonk9(b17.b7[0])
    print("--------------------- HUFFMAN CODE EXECUTION ---------------------")
    print("Inserted b6:", b6)
    print("")
    b18 = fonk14(b15)
    print("Character b18:")
    print(b18)
    print("")
    print("Tree built successfully!")
    print("")
    print("Huffman table:")
    b16.fonk13(b17.b7[0])
    print("")
    b19 = b16.fonk11(b17.b7[0], b17.b6)
    print("Text compressed to b1:", b19)
    print("")
    b20 = b16.fonk12(b17.b7[0], b19)
    print("Decompressed b6:", b20)
    print("")
    fonk16("result.txt", f"Inserted b6: {b6}\nCompressed b1: {b19}\nDecompressed b6: {b20}\n")
    print("Output file generated successfully!")
if b21 = = '__main__':
    fonk17()
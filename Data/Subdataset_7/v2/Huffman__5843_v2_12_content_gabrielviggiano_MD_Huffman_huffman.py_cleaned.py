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
    def fonk4(self, b16):
        self.b6 = b16
    def fonk5(self, b8):
        self.b7 = [b8]
        return
    def fonk6(self, b8):
        for i in self.b7:
            if i.b2 = = b8.b2:
                i.b3 += 1
                self.b7 = sorted(self.b7, key=lambda node: node.b3)
                return
        self.b7 += [b8]
        self.b7 = sorted(self.b7, key=lambda node: node.b3)
    def fonk7(self):
        for l in self.b6:
            if not self.b7:
                self.fonk5(class1(l, 1, '', None, None))
            else:
                self.fonk6(class1(l, 1, '', None, None))
        return
    def fonk8(self):
        for elem in self.b7:
            print(elem)
        return
    def fonk9(self):
        self.fonk7()
        while len(self.b7) > 1:
            b8 = class1("", self.b7[0].b3 + self.b7[1].b3, '', self.b7[0], self.b7[1])
            del self.b7[0]
            del self.b7[0]
            self.b7 += [b8]
            self.b7 = sorted(self.b7, key=lambda node: node.b3)
        return
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
        return
    def fonk11(self, b10, l):
        b1 = ''
        if b10.b2 = = l:
            b1 = b10.b1
        if b10.b4 is not None:
            b1 = self.fonk11(b10.b4, l)
        if b1 = = '':
            if b10.b5 is not None:
                b1 = self.fonk11(b10.b5, l)
        return b1
    def fonk12(self, b10, b6):
        b9 = ''
        for l in b6:
            b9 += self.fonk11(b10, l)
        return b9
    def fonk13(self, tree2, binary_text):
        b10 = tree2
        b9 = ''
        for b11 in binary_text:
            if b11 = = '1':
                if b10.b4 is not None:
                    b10 = b10.b4
                    if b10.b4 is None and b10.b5 is None:
                        b9 += (b10.b2)
                        b10 = tree2
            else:
                if b10.b5 is not None:
                    b10 = b10.b5
                    if b10.b4 is None and b10.b5 is None:
                        b9 += (b10.b2)
                        b10 = tree2
        return b9
    def fonk14(self, node):
        if node is None:
            return
        if node.b4 is not None:
            self.fonk14(node.b4)
        if node.fonk3():
            print(node)
        if node.b5 is not None:
            self.fonk14(node.b5)
        return
def fonk15(b16):
    b12 = Counter(b16)
    return b12
def fonk16(b14):
    if not os.path.isfile(b14):
        print("File not found!")
        exit()
    else:
        with open(b14, "r") as b13:
            b6 = b13.read()
        return b6
def fonk17(b14, b6):
    try:
        b13 = open(b14, 'w')
        b13.write(b6)
        b13.close()
    except IOError:
        raise print("Error creating b13!")
def fonk18(args):
    print("TO START THE PROGRAM, INSERT THE FILE NAME WHERE THE WORD TO BE COMPRESSED IS LOCATED")
    b14 = input("Name: ")
    b15 = fonk16(b14)
    b16 = list(fonk16(b14))
    b17 = class3()
    b18 = class2(b16)
    b18.fonk9()
    b17.fonk10(b18.b7[0])
    print("--------------------- EXECUTION OF HUFFMAN CODE ---------------------")
    print("Inserted b15:", b15)
    print("")
    print("Character b12:")
    b19 = fonk15(b16)
    print(b19)
    print("")
    print("Tree created successfully!")
    print("")
    print("Huffman table:")
    b17.fonk14(b18.b7[0])
    print("")
    b20 = b17.fonk12(b18.b7[0], b18.b6)
    print("Word compressed to b1:", b20)
    print("")
    b21 = b17.fonk13(b18.b7[0], b17.fonk12(b18.b7[0], b18.b6))
    print("Decompressed b15:", b21)
    print("")
    fonk17("b9.txt", ("Inserted Word: " + b15 + "\n" +
                               "Compressed Word: " + b20 + "\n" +
                               "Decompressed Word: " + b21 + "\n"
    ))
    print("Output b13 generated successfully!")
    return 0
if b22 = = '__main__':
    import sys
    sys.exit(fonk18(sys.argv))
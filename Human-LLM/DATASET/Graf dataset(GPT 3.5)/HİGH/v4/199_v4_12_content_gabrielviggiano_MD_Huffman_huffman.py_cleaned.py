import os
from collections import Counter
class class1:
    def fonk1(self, b1, b2, b3, b4, b5):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
    def fonk2(self):
        return repr((self.b1, self.b2, self.b3))
    def fonk3(self):
        return self.b4 is None and self.b5 is None
class class2:
    def fonk4(self, b14):
        self.b6 = b14
        self.a1 = 0
    def fonk5(self, new):
        self.a1 = [new]
        return
    def fonk6(self, new):
        for i in self.a1:
            if i.b1 = = new.b1:
                i.b2 += 1
                self.a1 = sorted(self.a1, key=lambda node: node.b2)
                return
        self.a1 += [new]
        self.a1 = sorted(self.a1, key=lambda node: node.b2)
    def fonk7(self):
        for l in self.b6:
            if self.a1 = = 0:
                self.fonk5(class1(l, 1, '', None, None))
            else:
                self.fonk6(class1(l, 1, '', None, None))
        return
    def fonk8(self):
        for elem in self.a1:
            print(elem)
        return
    def fonk9(self):
        self.fonk7()
        while len(self.a1) > 1:
            b7 = class1("", self.a1[0].b2 + self.a1[1].b2, '', self.a1[0], self.a1[1])
            del self.a1[0]
            del self.a1[0]
            self.a1 += [b7]
            self.a1 = sorted(self.a1, key=lambda node: node.b2)
        return
class class3:
    def fonk10(self, node):
        if node is None:
            return
        if node.b4 is not None:
            node.b4.b3 = node.b3 + '1'
            self.fonk10(node.b4)
        if node.b5 is not None:
            node.b5.b3 = node.b3 + '0'
            self.fonk10(node.b5)
        return
    def fonk11(self, tree, l):
        b3 = ''
        if tree.b1 = = l:
            b3 = tree.b3
        if tree.b4 is not None:
            b3 = self.fonk11(tree.b4, l)
        if b3 = = '':
            if tree.b5 is not None:
                b3 = self.fonk11(tree.b5, l)
        return b3
    def fonk12(self, tree, b6):
        b8 = ''
        for l in b6:
            b8 += self.fonk11(tree, l)
        return b8
    def fonk13(self, tree, binaryText):
        b9 = tree
        b8 = ''
        for b3 in binaryText:
            if b3 = = '1':
                if b9.b4 is not None:
                    b9 = b9.b4
                    if b9.b4 is None and b9.b5 is None:
                        b8 += b9.b1
                        b9 = tree
            else:
                if b9.b5 is not None:
                    b9 = b9.b5
                    if b9.b4 is None and b9.b5 is None:
                        b8 += b9.b1
                        b9 = tree
        return b8
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
def fonk15(b14):
    b10 = Counter(b14)
    return b10
def fonk16(b12):
    if not os.path.isfile(b12):
        print("File not found!")
        exit()
    else:
        with open(b12, "r") as b11:
            b6 = b11.read()
        return b6
def fonk17(b12, b6):
    try:
        b11 = open(b12, 'w')
        b11.write(b6)
        b11.close()
    except IOError:
        raise print("Error creating the b11!")
def fonk18(args):
    print("ENTER THE FILE NAME WHERE THE WORD TO BE COMPRESSED IS LOCATED")
    b12 = input("Name: ")
    b13 = fonk16(b12)
    b14 = list(fonk16(b12))
    b15 = class3()
    b16 = class2(b14)
    b16.fonk9()
    b15.fonk10(b16.a1[0])
    print("--------------------- EXECUTION OF HUFFMAN CODE ---------------------")
    print("Inserted b13:", b13)
    print("")
    print("Character b10:")
    b17 = fonk15(b14)
    print(b17)
    print("")
    print("Tree created successfully!")
    print("")
    print("Huffman table:")
    b15.fonk14(b16.a1[0])
    print("")
    b18 = b15.fonk12(b16.a1[0], b16.b6)
    print("Word compressed to b3:", b18)
    print("")
    b19 = b15.fonk13(b16.a1[0], b15.fonk12(b16.a1[0], b16.b6))
    print("Decompressed b13:", b19)
    print("")
    fonk17("b8.txt", ("Inserted Word:" + b13 + "\n" +
                              "Compressed Word: " + b18 + "\n" +
                              "Decompressed Word: " + b19 + "\n"
    ))
    print("Output b11 generated successfully!")
    return 0
if b20 = = '__main__':
    import sys
    sys.exit(fonk18(sys.argv))
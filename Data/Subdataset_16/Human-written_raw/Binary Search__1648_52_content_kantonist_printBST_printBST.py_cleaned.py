class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2(root):
    if not root:
        return
    fonk2(root.b2)
    print(root.b1)
    fonk2(root.b3)
def fonk3(root):
    if not root:
        return
    print (root.b1)
    fonk3(root.b2)
    fonk3(root.b3)
def fonk4(root):
    if not root:
        return
    fonk4(root.b2)
    fonk4(root.b3)
    print(root.b1)
def fonk5(root):
    b4 = [root]
    a1 = 1
    while len(b4)> 0:
        b5 = []
        print('Level ', a1)
        for leaf in b4:
            print(leaf.b1)
            if leaf.b2:
                b5.append(leaf.b2)
            if leaf.b3:
                b5.append(leaf.b3)
        b4 = b5
        a1 += 1
    return
b6 = class1(8)
b6.b2 = class1(3)
b6.b3 = class1(10)
b6.b2.b2 = class1(1)
b6.b2.b3 = class1(6)
b6.b3.b3 = class1(14)
b6.b3.b3.b2 = class1(13)
b6.b2.b3.b2 = class1(4)
b6.b2.b3.b3 = class1(15)
print('In-Order Traversal and print:')
fonk2(b6)
print('Pre-Order Traversal and print:')
fonk3(b6)
print('Post-Order Traversal and print:')
fonk4(b6)
print('Level Traversal and print:')
fonk5(b6)
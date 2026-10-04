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
    print(root.b1)
    fonk3(root.b2)
    fonk3(root.b3)
def fonk4(root):
    if not root:
        return
    fonk4(root.b2)
    fonk4(root.b3)
    print(root.b1)
def fonk5(root):
    if not root:
        return
    b4 = [root]
    a1 = 1
    while b4:
        b5 = []
        print(f'Level {a1}:')
        for node in b4:
            print(node.b1)
            if node.b2:
                b5.append(node.b2)
            if node.b3:
                b5.append(node.b3)
        b4 = b5
        a1 += 1
if b6 = = "__main__":
    b7 = class1(8)
    b7.b2 = class1(3)
    b7.b3 = class1(10)
    b7.b2.b2 = class1(1)
    b7.b2.b3 = class1(6)
    b7.b3.b3 = class1(14)
    b7.b3.b3.b2 = class1(13)
    b7.b2.b3.b2 = class1(4)
    b7.b2.b3.b3 = class1(7)
    print('In-Order Traversal and print:')
    fonk2(b7)
    print('\nPre-Order Traversal and print:')
    fonk3(b7)
    print('\nPost-Order Traversal and print:')
    fonk4(b7)
    print('\nLevel Traversal and print:')
    fonk5(b7)
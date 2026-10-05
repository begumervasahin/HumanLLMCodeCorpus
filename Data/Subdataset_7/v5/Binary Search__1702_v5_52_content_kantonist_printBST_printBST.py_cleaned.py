class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2(root):
    if not root:
        return
    fonk2(root.b2)
    print(root.b1, b4 = ' ')
def fonk3(root):
    if not root:
        return
    print(root.b1, b4 = ' ')
    fonk3(root.b2)
    fonk3(root.b3)
def fonk4(root):
    if not root:
        return
    fonk4(root.b2)
    fonk4(root.b3)
    print(root.b1, b4 = ' ')
def fonk5(root):
    if not root:
        return
    b5 = [root]
    while b5:
        b6 = b5.pop(0)
        print(b6.b1, b4 = ' ')
        if b6.b2:
            b5.append(b6.b2)
        if b6.b3:
            b5.append(b6.b3)
b7 = class1(8)
b7.b2 = class1(3)
b7.b3 = class1(10)
b7.b2.b2 = class1(1)
b7.b2.b3 = class1(6)
b7.b3.b3 = class1(14)
b7.b3.b3.b2 = class1(13)
b7.b2.b3.b2 = class1(4)
b7.b2.b3.b3 = class1(15)
print('In-Order Traversal:')
fonk2(b7)
print('\nPre-Order Traversal:')
fonk3(b7)
print('\nPost-Order Traversal:')
fonk4(b7)
print('\nLevel-Order Traversal:')
fonk5(b7)
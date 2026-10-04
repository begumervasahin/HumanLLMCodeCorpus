class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2(b8):
    if b8 is None:
        return
    fonk2(b8.b2)
    print(b8.b1)
    fonk2(b8.b3)
def fonk3(b8):
    if b8 is None:
        return
    print(b8.b1)
    fonk3(b8.b2)
    fonk3(b8.b3)
def fonk4(b8):
    if b8 is None:
        return
    fonk4(b8.b2)
    fonk4(b8.b3)
    print(b8.b1)
def fonk5(b8):
    if b8 is None:
        return
    b4 = [b8]
    a1 = 1
    while b4:
        b5 = []
        print(f'Level {a1}:', b6 = ' ')
        for node in b4:
            print(node.b1, b6 = ' ')
            if node.b2:
                b5.append(node.b2)
            if node.b3:
                b5.append(node.b3)
        print()
        b4 = b5
        a1 += 1
if b7 = = "__main__":
    b8 = class1(8)
    b8.b2 = class1(3)
    b8.b3 = class1(10)
    b8.b2.b2 = class1(1)
    b8.b2.b3 = class1(6)
    b8.b3.b3 = class1(14)
    b8.b3.b3.b2 = class1(13)
    b8.b2.b3.b2 = class1(4)
    b8.b2.b3.b3 = class1(7)
    print('In-Order Traversal:')
    fonk2(b8)
    print('\nPre-Order Traversal:')
    fonk3(b8)
    print('\nPost-Order Traversal:')
    fonk4(b8)
    print('\nLevel-Order Traversal:')
    fonk5(b8)
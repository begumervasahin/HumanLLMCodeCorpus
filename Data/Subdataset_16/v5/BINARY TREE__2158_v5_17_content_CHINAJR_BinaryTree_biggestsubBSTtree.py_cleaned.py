class class1:
    def fonk1(self, b1 = -1, b2=None, b3=None):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
class class2:
    def fonk2(self, b4, b5, b6, b7):
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
def fonk3(node):
    if node is None:
        return class2(0, None, float('inf'), float('-inf'))
    b8 = fonk3(node.b2)
    b9 = fonk3(node.b3)
    a1 = 0
    if (b8.b5 = = node.b2 and
        b9.b5 = = node.b3 and
        node.b1 > b8.b7 and
        node.b1 < b9.b6):
        a1 = b8.b4 + 1 + b9.b4
    b10 = max(max(b8.b4, b9.b4), a1)
    if b8.b4 > b9.b4:
        b11 = b8.b5
    else:
        b11 = b9.b5
    if b10 = = a1:
        b11 = node
    return class2(
        b10,
        b11,
        min(min(b8.b6, b9.b6), node.b1),
        max(max(b8.b7, b9.b7), node.b1)
    )
def fonk4(b16):
    print("Binary Tree:")
    fonk5(b16, 0, 'H', 17)
def fonk5(node, height, label, length):
    if node is None:
        return
    fonk5(node.b3, height + 1, 'v', length)
    b1 = f"{label}{node.b1}{label}"
    b12 = len(b1)
    b13 = (length - b12)
    b14 = length - b12 - b13
    b1 = fonk6(b13) + b1 + fonk6(b14)
    print(fonk6(height * length) + b1)
    fonk5(node.b2, height + 1, '^', length)
def fonk6(num):
    return ' ' * num
if b15 = = '__main__':
    b16 = class1(6)
    b16.b2 = class1(1)
    b16.b2.b2 = class1(0)
    b16.b2.b3 = class1(3)
    b16.b3 = class1(12)
    b16.b3.b2 = class1(10)
    b16.b3.b2.b2 = class1(4)
    b16.b3.b2.b2.b2 = class1(2)
    b16.b3.b2.b2.b3 = class1(5)
    b16.b3.b2.b3 = class1(14)
    b16.b3.b2.b3.b2 = class1(11)
    b16.b3.b2.b3.b3 = class1(15)
    b16.b3.b3 = class1(13)
    b16.b3.b3.b2 = class1(20)
    b16.b3.b3.b3 = class1(16)
    b17 = fonk3(b16)
    if b17.b5:
        print("Root of the largest BST subtree:", b17.b5.b1)
    else:
        print("No BST subtree found.")
    fonk4(b16)
    fonk4(b17.b5)
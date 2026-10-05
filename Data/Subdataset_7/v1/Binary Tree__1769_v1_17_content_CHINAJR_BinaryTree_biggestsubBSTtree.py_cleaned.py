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
def fonk3(b5):
    if b5 = = None:
        return class2(0, None, 10000, -10000)
    b2 = b5.b2
    b8 = fonk3(b2)
    b3 = b5.b3
    b9 = fonk3(b3)
    a1 = 0
    if (b8.b5 = = b2 and b9.b5 == b3 and
        b5.b1 > b8.b7 and b5.b1 < b9.b6):
        a1 = b8.b4 + 1 + b9.b4
    b10 = b8.b4
    b11 = b9.b4
    b12 = max(max(b10, b11), a1)
    if b10 > b11:
        b13 = b8.b5
    else:
        b13 = b9.b5
    if b12 = = a1:
        b13 = b5
    return class2(b12, b13, min(min(b8.b6, b9.b6), b5.b1),
                      max(max(b8.b7, b9.b7), b5.b1))
def fonk4(root):
    print("Binary Tree:")
    fonk5(root, 0, 'H', 17)
def fonk5(root, height, s, length):
    if root is None:
        return
    fonk5(root.b3, height + 1, 'v', length)
    b1 = s + str(root.b1) + s
    b14 = len(b1)
    b15 = (length - b14)
    b16 = length - b14 - b15
    b1 = fonk6(b15) + b1 + fonk6(b16)
    print(fonk6(height * length) + b1)
    fonk5(root.b2, height + 1, '^', length)
def fonk6(num):
    return ' ' * num
if b17 = = '__main__':
    b5 = class1(6)
    b5.b2 = class1(1)
    b5.b2.b2 = class1(0)
    b5.b2.b3 = class1(3)
    b5.b3 = class1(12)
    b5.b3.b2 = class1(10)
    b5.b3.b2.b2 = class1(4)
    b5.b3.b2.b2.b2 = class1(2)
    b5.b3.b2.b2.b3 = class1(5)
    b5.b3.b2.b3 = class1(14)
    b5.b3.b2.b3.b2 = class1(11)
    b5.b3.b2.b3.b3 = class1(15)
    b5.b3.b3 = class1(13)
    b5.b3.b3.b2 = class1(20)
    b5.b3.b3.b3 = class1(16)
    b18 = fonk3(b5).b5
    print("Head value of processed tree:", b18.b1)
    fonk4(b5)
    fonk4(b18)
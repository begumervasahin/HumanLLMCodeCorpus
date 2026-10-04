class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2(b6, start_index):
    for i in range(start_index, len(b6)):
        print(b6[i].b1, b4 = ' ')
    print()
def fonk3(b10, k):
    b5 = []
    b6 = []
    b7 = b10
    while True:
        while b7:
            b5.append(b7)
            if not b6:
                b6.append((b7, b7.b1))
            else:
                top_node, b8 = b6[-1]
                b6.append((b7, b8 + b7.b1))
            b7 = b7.b2
        while b7 is None and b5:
            b7 = b5.pop()
            top_node, b8 = b6.pop()
            b9 = b8
            for i in range(len(b6)):
                if b9 = = k:
                    fonk2(b6, i)
                b9 -= b6[i][0].b1
            if b9 = = k:
                fonk2(b6, 0)
            if b6:
                top_node, b8 = b6[-1]
            b6.append((b7, b8))
            b7 = b7.b3
        if b7 is None and not b5:
            break
b10 = class1(1)
b10.b2 = class1(3)
b10.b2.b2 = class1(2)
b10.b2.b3 = class1(1)
b10.b2.b3.b2 = class1(1)
b10.b3 = class1(-1)
b10.b3.b2 = class1(4)
b10.b3.b2.b2 = class1(1)
b10.b3.b2.b3 = class1(2)
b10.b3.b3 = class1(5)
b10.b3.b3.b3 = class1(6)
fonk3(b10, 5)
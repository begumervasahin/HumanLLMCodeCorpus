class class1:
    def fonk1(self, b2, b1 = None):
        self.b2 = b2
        self.b1 = b1 if b1 is not None else []
class class2:
    def fonk2(self, b8):
        if not b8:
            return []
        b3 = []
        b4 = [b8]
        while b4:
            b5 = []
            b6 = []
            for node in b4:
                b5.append(node.b2)
                b6.extend(node.b1)
            b3.append(b5)
            b4 = b6
        return b3
if b7 = = "__main__":
    b8 = class1(1, [
        class1(3, [
            class1(5),
            class1(6)
        ]),
        class1(2),
        class1(4)
    ])
    b9 = class2()
    print("Level Order Traversal:", b9.fonk2(b8))
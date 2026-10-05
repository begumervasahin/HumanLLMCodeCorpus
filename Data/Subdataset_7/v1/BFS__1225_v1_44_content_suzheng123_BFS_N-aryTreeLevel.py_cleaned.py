class class1:
    def fonk1(self, b2, b1 = None):
        self.b2 = b2
        self.b1 = b1 if b1 else []
class class2:
    def fonk2(self, b13):
        if not b13:
            return []
        b3 = [b13]
        b4 = []
        while b3:
            b5 = []
            b6 = []
            for node in b3:
                b5.append(node.b2)
                for child in node.b1:
                    b6.append(child)
            b3 = b6
            b4.append(b5)
        return b4
if b7 = = "__main__":
    b8 = class1(5)
    b9 = class1(6)
    b10 = class1(3, [b8, b9])
    b11 = class1(2)
    b12 = class1(4)
    b13 = class1(1, [b10, b11, b12])
    b14 = class2()
    b15 = b14.fonk2(b13)
    print("Level order traversal:")
    for b5 in b15:
        print(b5)
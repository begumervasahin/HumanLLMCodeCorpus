class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
    def fonk2(self):
        return str(self.b1)
class class2:
    def fonk3(self, b3 = None):
        self.b3 = b3
    def fonk4(self, b1):
        b4 = class1(b1)
        if not self.b3:
            self.b3 = b4
            return
        b5 = self.b3
        while b5.b2:
            b5 = b5.b2
        b5.b2 = b4
    def fonk5(self):
        b6 = []
        b5 = self.b3
        while b5:
            b6.fonk4(b5.b1)
            b5 = b5.b2
        return " -> ".join(map(str, b6))
def fonk6(list1, list2):
    b7 = class2()
    b8 = list1.b3 if list1 else None
    b9 = list2.b3 if list2 else None
    while b8 or b9:
        if b8 is None:
            b7.fonk4(b9.b1)
            b9 = b9.b2
        elif b9 is None:
            b7.fonk4(b8.b1)
            b8 = b8.b2
        elif b8.b1 <= b9.b1:
            b7.fonk4(b8.b1)
            b8 = b8.b2
        else:
            b7.fonk4(b9.b1)
            b9 = b9.b2
    return b7
class class3(class2):
    def fonk7(self):
        return self.fonk8(self.b3)
    def fonk8(self, node):
        if not node.b2:
            return fonk6(node.b1, None)
        return fonk6(node.b1, self.fonk8(node.b2))
if b10 = = "__main__":
    b11 = class2(class1(1))
    b11.fonk4(3)
    b11.fonk4(5)
    print(f"Linked List 1: {b11}")
    b12 = class2(class1(2))
    b12.fonk4(4)
    print(f"Linked List 2: {b12}")
    b13 = fonk6(b11, b12)
    print(f"Merged List: {b13}")
    b14 = fonk6(None, b11)
    print(f"Merged with None: {b14}")
    b15 = class3(class1(b11))
    b15.fonk4(b12)
    b16 = b15.fonk7()
    print(f"Flattened Nested List: {b16}")
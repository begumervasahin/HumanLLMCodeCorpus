class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
    def fonk2(self, other):
        return True if self.b1 = = other.b1 else False
class class2:
    def fonk3(self):
        self.b3 = None
    def fonk4(self, node):
        b4 = False
        if self.b3:
            b5 = self.b3
            while b5:
                if b5 = = node:
                    b4 = True
                    break
                b5 = b5.b2
        return b4
    def fonk5(self):
        a1 = 0
        if self.b3:
            b5 = self.b3
            while b5:
                a1 += 1
                b5 = b5.b2
        return a1
    def fonk6(self, node):
        if not self.b3:
            self.b3 = node
            return
        b5 = self.b3
        while b5.b2:
            b5 = b5.b2
        b5.b2 = node
    def fonk7(self, flag_node, node):
        if self.b3 = = flag_node:
            node.b2 = self.b3
            self.b3 = node
        else:
            b6 = self.b3
            while b6.b2:
                if b6.b2 = = flag_node:
                    break
                b6 = b6.b2
            node.b2 = b6.b2
            b6.b2 = node
    def fonk8(self, node):
        if self.b3:
            if self.b3.b1 = = node.b1:
                self.b3 = self.b3.b2
                return
            b7 = self.b3
            while b7.b2:
                if b7.b2 = = node:
                    break
                b7 = b7.b2
            b6 = b7.b2
            b7.b2 = b6.b2
    def fonk9(self):
        b8 = self.b3
        while b8.b2:
            b10, b9 = b8, b8.b2
            while b9:
                if b9 = = b8:
                    b10.b2 = b9.b2
                else:
                    b10 = b10.b2
                b9 = b9.b2
            b8 = b8.b2
    def fonk10(self):
        if not self.b3 or not self.b3.b2:
            return
        b5 = self.b3.b2
        self.b3.b2 = None
        while b5:
            b11 = b5.b2
            b5.b2 = self.b3
            self.b3 = b5
            b5 = b11
    def fonk11(self):
        b5 = self.b3
        while b5:
            print(b5.b1)
            b5 = b5.b2
if b12 = = "__main__":
    b13 = class1(1)
    b14 = class1(2)
    b15 = class1(3)
    b16 = class1(4)
    b17 = class1(5)
    b18 = class2()
    b18.fonk6(b13)
    b18.fonk6(b14)
    b18.fonk6(b15)
    b18.fonk6(b16)
    b18.fonk6(b17)
    print("Initial List:")
    b18.fonk11()
    print()
    b19 = class1(0)
    b18.fonk7(b13, b19)
    print("List after inserting a new node:")
    b18.fonk11()
    print()
    b18.fonk8(b19)
    print("List after deleting the new node:")
    b18.fonk11()
    print()
    b18.fonk10()
    print("Reversed List:")
    b18.fonk11()
    print()
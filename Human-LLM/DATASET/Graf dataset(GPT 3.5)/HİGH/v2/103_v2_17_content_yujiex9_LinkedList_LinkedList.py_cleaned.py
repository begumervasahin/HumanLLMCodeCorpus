class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
    def fonk2(self, other):
        return self.b1 = = other.b1
class class2:
    def fonk3(self):
        self.b3 = None
    def fonk4(self, node):
        b4 = False
        b5 = self.b3
        while b5:
            if b5 = = node:
                b4 = True
                break
            b5 = b5.b2
        return b4
    def fonk5(self):
        a1 = 0
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
            if self.b3 = = node:
                self.b3 = self.b3.b2
                return
            b6 = self.b3
            while b6.b2:
                if b6.b2 = = node:
                    break
                b6 = b6.b2
            b6.b2 = node.b2
    def fonk9(self):
        b7 = self.b3
        while b7:
            b8 = b7
            while b8.b2:
                if b8.b2 = = b7:
                    b8.b2 = b8.b2.b2
                else:
                    b8 = b8.b2
            b7 = b7.b2
    def fonk10(self):
        if not self.b3 or not self.b3.b2:
            return
        b6 = None
        b5 = self.b3
        while b5:
            b2 = b5.b2
            b5.b2 = b6
            b6 = b5
            b5 = b2
        self.b3 = b6
    def fonk11(self):
        b5 = self.b3
        while b5:
            print(b5.b1)
            b5 = b5.b2
if b9 = = "__main__":
    b10 = class1(1)
    b11 = class1(2)
    b12 = class1(3)
    b13 = class1(4)
    b14 = class1(5)
    b15 = class2()
    b15.fonk6(b10)
    b15.fonk6(b11)
    b15.fonk6(b12)
    b15.fonk6(b13)
    b15.fonk6(b14)
    print("Initial List:")
    b15.fonk11()
    print()
    b16 = class1(0)
    b15.fonk7(b10, b16)
    print("List after inserting a new node:")
    b15.fonk11()
    print()
    b15.fonk8(b16)
    print("List after deleting the new node:")
    b15.fonk11()
    print()
    b15.fonk9()
    print("List after removing duplicates:")
    b15.fonk11()
    print()
    b15.fonk10()
    print("Reversed List:")
    b15.fonk11()
    print()
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
        b4 = self.b3
        while b4:
            if b4 = = node:
                return True
            b4 = b4.b2
        return False
    def fonk5(self):
        a1 = 0
        b4 = self.b3
        while b4:
            a1 += 1
            b4 = b4.b2
        return a1
    def fonk6(self, node):
        if not self.b3:
            self.b3 = node
        else:
            b4 = self.b3
            while b4.b2:
                b4 = b4.b2
            b4.b2 = node
    def fonk7(self, target_node, b14):
        if self.b3 = = target_node:
            b14.b2 = self.b3
            self.b3 = b14
        else:
            b4 = self.b3
            while b4:
                if b4 = = target_node:
                    b14.b2 = b4.b2
                    b4.b2 = b14
                    break
                b4 = b4.b2
    def fonk8(self, target_node):
        if self.b3 = = target_node:
            self.b3 = self.b3.b2
        else:
            b5 = self.b3
            while b5.b2:
                if b5.b2 = = target_node:
                    b5.b2 = b5.b2.b2
                    break
                b5 = b5.b2
    def fonk9(self):
        b4 = self.b3
        while b4:
            b6 = b4
            while b6.b2:
                if b6.b2 = = b4:
                    b6.b2 = b6.b2.b2
                else:
                    b6 = b6.b2
            b4 = b4.b2
    def fonk10(self):
        b5 = None
        b4 = self.b3
        while b4:
            b2 = b4.b2
            b4.b2 = b5
            b5 = b4
            b4 = b2
        self.b3 = b5
    def fonk11(self):
        b4 = self.b3
        while b4:
            print(b4.b1)
            b4 = b4.b2
if b7 = = "__main__":
    b8 = class1(1)
    b9 = class1(2)
    b10 = class1(3)
    b11 = class1(4)
    b12 = class1(5)
    b13 = class2()
    b13.fonk6(b8)
    b13.fonk6(b9)
    b13.fonk6(b10)
    b13.fonk6(b11)
    b13.fonk6(b12)
    print("Initial List:")
    b13.fonk11()
    print()
    b14 = class1(0)
    b13.fonk7(b8, b14)
    print("List after inserting a new node:")
    b13.fonk11()
    print()
    b13.fonk8(b14)
    print("List after deleting the new node:")
    b13.fonk11()
    print()
    b13.fonk9()
    print("List after removing duplicates:")
    b13.fonk11()
    print()
    b13.fonk10()
    print("Reversed List:")
    b13.fonk11()
    print()
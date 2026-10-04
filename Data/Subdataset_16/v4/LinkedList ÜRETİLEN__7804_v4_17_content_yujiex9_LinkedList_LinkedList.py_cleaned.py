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
    def fonk7(self, flag_node, node):
        if self.b3 = = flag_node:
            node.b2 = self.b3
            self.b3 = node
        else:
            b4 = self.b3
            while b4.b2:
                if b4.b2 = = flag_node:
                    break
                b4 = b4.b2
            node.b2 = b4.b2
            b4.b2 = node
    def fonk8(self, node):
        if self.b3:
            if self.b3 = = node:
                self.b3 = self.b3.b2
            else:
                b4 = self.b3
                while b4.b2 and b4.b2 != node:
                    b4 = b4.b2
                if b4.b2:
                    b4.b2 = b4.b2.b2
    def fonk9(self):
        b5 = self.b3
        while b5:
            b6 = b5
            b7 = b5.b2
            while b7:
                if b7 = = b5:
                    b6.b2 = b7.b2
                else:
                    b6 = b7
                b7 = b7.b2
            b5 = b5.b2
    def fonk10(self):
        b8 = None
        b4 = self.b3
        while b4:
            b9 = b4.b2
            b4.b2 = b8
            b8 = b4
            b4 = b9
        self.b3 = b8
    def fonk11(self):
        b4 = self.b3
        while b4:
            print(b4.b1, b10 = " ")
            b4 = b4.b2
        print()
if b11 = = "__main__":
    b12 = class2()
    b12.fonk6(class1(1))
    b12.fonk6(class1(2))
    b12.fonk6(class1(3))
    b12.fonk6(class1(2))
    b12.fonk6(class1(4))
    print("Original list:")
    b12.fonk11()
    print("Reversed list:")
    b12.fonk10()
    b12.fonk11()
    print("List after removing duplicates:")
    b12.fonk9()
    b12.fonk11()
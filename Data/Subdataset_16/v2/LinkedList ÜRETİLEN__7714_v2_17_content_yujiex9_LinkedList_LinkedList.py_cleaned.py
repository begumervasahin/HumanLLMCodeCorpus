class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
    def fonk2(self, other):
        return self.b1 = = other.b1 if other else False
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
            return
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
            while b4 and b4.b2 != flag_node:
                b4 = b4.b2
            if b4:
                node.b2 = b4.b2
                b4.b2 = node
    def fonk8(self, node):
        if self.b3:
            if self.b3 = = node:
                self.b3 = self.b3.b2
                return
            b4 = self.b3
            while b4.b2 and b4.b2 != node:
                b4 = b4.b2
            if b4.b2:
                b4.b2 = b4.b2.b2
    def fonk9(self):
        b5 = self.b3
        while b5:
            b6 = b5
            while b6.b2:
                if b6.b2 = = b5:
                    b6.b2 = b6.b2.b2
                else:
                    b6 = b6.b2
            b5 = b5.b2
    def fonk10(self):
        b7 = None
        b8 = self.b3
        while b8:
            b2 = b8.b2
            b8.b2 = b7
            b7 = b8
            b8 = b2
        self.b3 = b7
    def fonk11(self):
        b4 = self.b3
        while b4:
            print(b4.b1, b9 = ' -> ')
            b4 = b4.b2
        print('None')
if b10 = = "__main__":
    b11 = class2()
    b11.fonk6(class1(1))
    b11.fonk6(class1(2))
    b11.fonk6(class1(3))
    b11.fonk7(b11.b3, class1(0))
    b11.fonk7(b11.b3.b2, class1(1.5))
    print("List after insertions:")
    b11.fonk11()
    b11.fonk6(class1(2))
    b11.fonk9()
    print("List after removing duplicates:")
    b11.fonk11()
    b11.fonk10()
    print("List after reversing:")
    b11.fonk11()
    b11.fonk8(class1(1.5))
    print("List after deleting node with b1 1.5:")
    b11.fonk11()
    print(f"Length of list: {len(b11)}")
    print(f"class1 with b1 2 in list: {class1(2) in b11}")
    print(f"class1 with b1 4 in list: {class1(4) in b11}")
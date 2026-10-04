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
    def fonk7(self, target_node, new_node):
        if not self.b3:
            print("List is empty")
            return
        b4 = self.b3
        while b4 and b4 != target_node:
            b4 = b4.b2
        if b4:
            new_node.b2 = b4.b2
            b4.b2 = new_node
    def fonk8(self, target_node):
        if not self.b3:
            return
        if self.b3 = = target_node:
            self.b3 = self.b3.b2
            return
        b4 = self.b3
        while b4.b2 and b4.b2 != target_node:
            b4 = b4.b2
        if b4.b2:
            b4.b2 = b4.b2.b2
    def fonk9(self):
        b4 = self.b3
        while b4:
            b5 = b4
            while b5.b2:
                if b5.b2 = = b4:
                    b5.b2 = b5.b2.b2
                else:
                    b5 = b5.b2
            b4 = b4.b2
    def fonk10(self):
        b6 = None
        b4 = self.b3
        while b4:
            b2 = b4.b2
            b4.b2 = b6
            b6 = b4
            b4 = b2
        self.b3 = b6
    def fonk11(self):
        b4 = self.b3
        while b4:
            print(b4.b1, b7 = ' -> ')
            b4 = b4.b2
        print('None')
if b8 = = "__main__":
    b9 = class2()
    b9.fonk6(class1(1))
    b9.fonk6(class1(2))
    b9.fonk6(class1(3))
    b9.fonk7(b9.b3, class1(0))
    b9.fonk7(b9.b3.b2, class1(1.5))
    print("List after insertions:")
    b9.fonk11()
    b9.fonk6(class1(2))
    b9.fonk9()
    print("List after removing duplicates:")
    b9.fonk11()
    b9.fonk10()
    print("List after reversing:")
    b9.fonk11()
    b9.fonk8(class1(1.5))
    print("List after deleting node with b1 1.5:")
    b9.fonk11()
    print(f"Length of list: {len(b9)}")
    print(f"class1 with b1 2 in list: {class1(2) in b9}")
    print(f"class1 with b1 4 in list: {class1(4) in b9}")
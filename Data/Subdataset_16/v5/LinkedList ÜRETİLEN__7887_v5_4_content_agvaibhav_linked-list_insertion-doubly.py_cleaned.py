class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self):
        self.b4 = None
    def fonk3(self, new_data):
        b5 = class1(new_data)
        b5.b2 = self.b4
        if self.b4 is not None:
            self.b4.b3 = b5
        self.b4 = b5
    def fonk4(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node cannot be None")
            return
        b5 = class1(new_data)
        b5.b2 = prev_node.b2
        prev_node.b2 = b5
        b5.b3 = prev_node
        if b5.b2 is not None:
            b5.b2.b3 = b5
    def fonk5(self, next_node, new_data):
        if next_node is None:
            print("The given b2 node cannot be None")
            return
        b5 = class1(new_data)
        b5.b2 = next_node
        b5.b3 = next_node.b3
        if next_node.b3 is not None:
            next_node.b3.b2 = b5
        else:
            self.b4 = b5
        next_node.b3 = b5
    def fonk6(self, b1):
        b5 = class1(b1)
        if self.b4 is None or self.b4.b1 >= b5.b1:
            b5.b2 = self.b4
            if self.b4 is not None:
                self.b4.b3 = b5
            self.b4 = b5
        else:
            b6 = self.b4
            while b6.b2 is not None and b6.b2.b1 < b5.b1:
                b6 = b6.b2
            b5.b2 = b6.b2
            if b6.b2 is not None:
                b6.b2.b3 = b5
            b6.b2 = b5
            b5.b3 = b6
    def fonk7(self, new_data):
        b5 = class1(new_data)
        if self.b4 is None:
            self.b4 = b5
            return
        b7 = self.b4
        while b7.b2 is not None:
            b7 = b7.b2
        b7.b2 = b5
        b5.b3 = b7
    def fonk8(self):
        b6 = self.b4
        while b6 is not None:
            print(b6.b1, b8 = ' ')
            b6 = b6.b2
        print()
if b9 = = "__main__":
    b10 = class2()
    b10.fonk3(5)
    b10.fonk7(6)
    b10.fonk3(1)
    b10.fonk4(b10.b4, 3)
    b10.fonk5(b10.b4.b2, 2)
    b10.fonk8()
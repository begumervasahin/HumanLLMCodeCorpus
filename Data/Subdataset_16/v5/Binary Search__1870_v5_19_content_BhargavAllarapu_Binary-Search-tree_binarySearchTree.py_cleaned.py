class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
    def fonk2(self):
        if self.b1 is not None:
            self.fonk3(self)
            self.b1 = None
            print("Deleted every node... Now the tree is empty.")
        else:
            print("Tree is already empty.")
    def fonk3(self, node):
        if node.b2:
            node.b2 = self.fonk3(node.b2)
        if node.b3:
            node.b3 = self.fonk3(node.b3)
        return None
    def fonk4(self, b4):
        if self.b1 is None:
            print("Nothing to find... Tree is empty.")
            return None
        if b4 < self.b1:
            return self.b2.fonk4(b4) if self.b2 else self.fonk5(b4)
        elif b4 > self.b1:
            return self.b3.fonk4(b4) if self.b3 else self.fonk5(b4)
        else:
            print(f"Node {b4}: Found.")
            return self.b1
    def fonk5(self, b4):
        print(f"Node {b4}: Not found.")
        return None
    def fonk6(self):
        if self.b1 is None:
            print("Nothing to find... Tree is empty.")
            return None
        return self.b2.fonk6() if self.b2 else self.b1
    def fonk7(self):
        if self.b1 is None:
            print("Nothing to find... Tree is empty.")
            return None
        return self.b3.fonk7() if self.b3 else self.b1
    def fonk8(self, b4):
        if self.b1 is None:
            self.b1 = b4
        elif b4 < self.b1:
            if self.b2 is None:
                self.b2 = class1(b4)
            else:
                self.b2.fonk8(b4)
        elif b4 > self.b1:
            if self.b3 is None:
                self.b3 = class1(b4)
            else:
                self.b3.fonk8(b4)
        else:
            print(f"Node {b4} already exists. Insertion skipped.")
    def fonk9(self, b4):
        if self.b1 is None:
            print("Nothing to delete... Tree is empty.")
            return None
        if b4 < self.b1:
            if self.b2:
                self.b2 = self.b2.fonk9(b4)
            else:
                self.fonk5(b4)
        elif b4 > self.b1:
            if self.b3:
                self.b3 = self.b3.fonk9(b4)
            else:
                self.fonk5(b4)
        elif b4 = = self.b1:
            return self.fonk10()
        return self
    def fonk10(self):
        if self.b2 is None:
            return self.b3
        if self.b3 is None:
            return self.b2
        b5 = self.b3.fonk6()
        self.b1 = b5
        self.b3 = self.b3.fonk9(b5)
        return self
    def fonk11(self):
        if self.b1 is None:
            print("Nothing to print... Tree is empty.")
        else:
            if self.b2:
                self.b2.fonk11()
            print(self.b1)
            if self.b3:
                self.b3.fonk11()
    def fonk12(self):
        if self.b1 is not None:
            print(f"b6 = {self.b1}")
        else:
            print("Tree is empty.")
if b7 = = "__main__":
    b8 = class1(20)
    b8.fonk8(12)
    b8.fonk8(34)
    b8.fonk8(21)
    b8.fonk8(56)
    b8.fonk8(23)
    b8.fonk8(16)
    b8.fonk8(14)
    b8.fonk8(19)
    b8.fonk8(24)
    print("Tree structure:")
    b8.fonk11()
    print("\nSearching elements:")
    b8.fonk4(78)
    print(f"Minimum value in tree: {b8.fonk6()}")
    print(f"Maximum value in tree: {b8.fonk7()}")
    b8.fonk4(21)
    b8.fonk4(201)
    print("\nDeleting nodes:")
    b8.fonk9(243)
    b8.fonk9(20)
    b8.fonk11()
    b8.fonk12()
    print("\nMaking tree empty:")
    b8.fonk2()
    b8.fonk11()
    print("\nInsertion after making tree empty:")
    b8.fonk8(16)
    b8.fonk11()
    b8.fonk8(14)
    b8.fonk8(19)
    b8.fonk11()
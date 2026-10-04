class class1:
    def fonk1(self, b1):
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
        if node.b2 is not None:
            node.b2 = self.fonk3(node.b2)
        if node.b3 is not None:
            node.b3 = self.fonk3(node.b3)
        del node
        return None
    def fonk4(self, b4):
        if self.b1 is None:
            return "Nothing to find... Tree is empty."
        elif b4 < self.b1 and self.b2 is not None:
            return self.b2.fonk4(b4)
        elif b4 > self.b1 and self.b3 is not None:
            return self.b3.fonk4(b4)
        elif b4 = = self.b1:
            print(f"Node {b4}: Found.")
            return self.b1
        else:
            print(f"Node {b4}: Not found.")
            return None
    def fonk5(self):
        if self.b1 is None:
            return "Nothing to find... Tree is empty."
        elif self.b2 is not None:
            return self.b2.fonk5()
        else:
            return self.b1
    def fonk6(self):
        if self.b1 is None:
            return "Nothing to find... Tree is empty."
        elif self.b3 is not None:
            return self.b3.fonk6()
        else:
            return self.b1
    def fonk7(self, b4):
        if self.b1:
            if b4 < self.b1:
                if self.b2 is None:
                    self.b2 = class1(b4)
                else:
                    self.b2.fonk7(b4)
            elif b4 > self.b1:
                if self.b3 is None:
                    self.b3 = class1(b4)
                else:
                    self.b3.fonk7(b4)
            else:
                print("Couldn't insert the node, as the node already exists.")
        else:
            self.b1 = b4
    def fonk8(self, b4):
        if self.b1 is None:
            print("Nothing to delete... Tree is empty.")
            return None
        elif b4 < self.b1 and self.b2 is not None:
            self.b2 = self.b2.fonk8(b4)
        elif b4 > self.b1 and self.b3 is not None:
            self.b3 = self.b3.fonk8(b4)
        elif b4 = = self.b1:
            if self.b2 is None:
                return self.b3
            elif self.b3 is None:
                return self.b2
            b5 = self.b3.fonk5()
            self.b1 = b5
            self.b3 = self.b3.fonk8(b5)
        return self
    def fonk9(self):
        if self.b1 is None:
            print("Nothing to print... Tree is empty.")
        else:
            if self.b2 is not None:
                self.b2.fonk9()
            print(self.b1)
            if self.b3 is not None:
                self.b3.fonk9()
    def fonk10(self):
        if self.b1 is not None:
            print(f"b6 = {self.b1}")
        else:
            print("Tree is empty.")
if b7 = = "__main__":
    b8 = class1(20)
    b8.fonk7(12)
    b8.fonk7(34)
    b8.fonk7(21)
    b8.fonk7(56)
    b8.fonk7(23)
    b8.fonk7(16)
    b8.fonk7(14)
    b8.fonk7(19)
    b8.fonk7(24)
    print("Tree structure:")
    b8.fonk9()
    print("\nSearching elements:")
    b8.fonk4(78)
    print(f"Minimum value in tree: {b8.fonk5()}")
    print(f"Maximum value in tree: {b8.fonk6()}")
    b8.fonk4(21)
    b8.fonk4(201)
    print("\nDeleting nodes:")
    b8.fonk8(243)
    b8.fonk8(20)
    b8.fonk9()
    b8.fonk10()
    print("\nMaking tree empty:")
    b8.fonk2()
    b8.fonk9()
    print("\nInsertion after making tree empty:")
    b8.fonk7(16)
    b8.fonk9()
    b8.fonk7(14)
    b8.fonk7(19)
    b8.fonk9()
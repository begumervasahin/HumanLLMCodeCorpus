class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
    def fonk2(self):
        if self.b1 is not None:
            self.fonk3(self)
            self.b1 = None
            print("Deleted every node ... Now the tree is empty")
        else:
            print("Tree is already empty ...")
    def fonk3(self, node):
        if node.b2 is not None:
            node.b2 = self.fonk3(node.b2)
        if node.b3 is not None:
            node.b3 = self.fonk3(node.b3)
        del node
        return None
    def fonk4(self, key):
        if self.b1 is None:
            return "Nothing to find... Tree is empty."
        else:
            if key < self.b1 and self.b2 is not None:
                return self.b2.fonk4(key)
            elif key > self.b1 and self.b3 is not None:
                return self.b3.fonk4(key)
            elif self.b1 = = key:
                print(f"Node {key} : Found.")
                return key
            else:
                print(f"Node {key} : Not found.")
                return None
    def fonk5(self):
        if self.b1 is None:
            return "Nothing to find... Tree is empty."
        else:
            if self.b2 is not None:
                return self.b2.fonk5()
            else:
                return self.b1
    def fonk6(self):
        if self.b1 is None:
            return "Nothing to find... Tree is empty."
        else:
            if self.b3 is not None:
                return self.b3.fonk6()
            else:
                return self.b1
    def fonk7(self, key):
        if self.b1 is None:
            self.b1 = key
        else:
            if key < self.b1:
                if self.b2 is None:
                    self.b2 = class1(key)
                else:
                    self.b2.fonk7(key)
            elif key > self.b1:
                if self.b3 is None:
                    self.b3 = class1(key)
                else:
                    self.b3.fonk7(key)
            else:
                print("Couldn't insert the node, because the node already exists.")
    def fonk8(self, key):
        if self.b1 is None:
            print("Nothing to delete... Tree is empty.")
            return None
        else:
            if key < self.b1 and self.b2 is not None:
                self.b2 = self.b2.fonk8(key)
            elif key > self.b1 and self.b3 is not None:
                self.b3 = self.b3.fonk8(key)
            elif self.b1 = = key:
                if self.b2 is None:
                    return self.b3
                elif self.b3 is None:
                    return self.b2
                b4 = self.b3.fonk5()
                self.b1 = b4
                self.b3 = self.b3.fonk8(b4)
            return self
    def fonk9(self):
        if self.b1 is None:
            print("Nothing to print... Tree is empty")
        else:
            if self.b2 is not None:
                self.b2.fonk9()
            print(self.b1)
            if self.b3 is not None:
                self.b3.fonk9()
    def fonk10(self):
        if self.b1 is not None:
            print("b5 = ", self.b1)
        else:
            print("Tree is Empty.")
if b6 = = "__main__":
    b7 = class1(20)
    b7.fonk7(12)
    b7.fonk7(34)
    b7.fonk7(21)
    b7.fonk7(56)
    b7.fonk7(23)
    b7.fonk7(16)
    b7.fonk7(14)
    b7.fonk7(19)
    b7.fonk7(24)
    b7.fonk9()
    print("Element :", b7.fonk4(78))
    print("Minimum value in tree is :", b7.fonk5())
    print("Maximum value in tree is :", b7.fonk6())
    b7.fonk4(21)
    b7.fonk4(201)
    b7.fonk8(243)
    b7.fonk8(20)
    b7.fonk9()
    b7.fonk10()
    b7.fonk2()
    b7.fonk9()
    print("Insertion after making tree empty")
    b7.fonk7(16)
    b7.fonk9()
    b7.fonk7(14)
    b7.fonk7(19)
    b7.fonk9()
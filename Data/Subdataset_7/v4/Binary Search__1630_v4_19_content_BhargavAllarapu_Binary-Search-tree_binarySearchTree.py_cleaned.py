class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
    def fonk2(self):
        if self.b1 is not None:
            self.fonk3(self)
            self.b1 = None
            print("Deleted every node. Now the tree is empty")
        else:
            print("The tree is already empty")
    def fonk3(self, node):
        if node.b2 is not None:
            node.b2 = self.fonk3(node.b2)
        if node.b3 is not None:
            node.b3 = self.fonk3(node.b3)
        del node
        return None
    def fonk4(self, key):
        if self is None:
            return "Nothing to find. The tree is empty."
        else:
            if self.b1 > key and self.b2 is not None:
                return self.b2.fonk4(key)
            elif self.b1 < key and self.b3 is not None:
                return self.b3.fonk4(key)
            elif self.b1 = = key:
                print("Node " + str(key) + " found.")
                return None
            else:
                print("Node " + str(key) + " not found.")
                return None
    def fonk5(self):
        if self is None:
            return "Nothing to find. The tree is empty."
        else:
            if self.b2 is not None:
                return self.b2.fonk5()
            else:
                return self.b1
    def fonk6(self):
        if self is None:
            return "Nothing to find. The tree is empty."
        else:
            if self.b3 is not None:
                return self.b3.fonk6()
            else:
                return self.b1
    def fonk7(self, key):
        if self.b1:
            if self.b1 > key:
                if self.b2 is None:
                    self.b2 = class1(key)
                else:
                    return self.b2.fonk7(key)
            elif self.b1 < key:
                if self.b3 is None:
                    self.b3 = class1(key)
                else:
                    return self.b3.fonk7(key)
            else:
                print("Couldn't insert the node because the node already exists.")
        else:
            self.b1 = key
    def fonk8(self, key):
        if self is None:
            print("Nothing to delete. The tree is empty.")
        else:
            if self.b1 > key and self.b2 is not None:
                self.b2 = self.b2.fonk8(key)
            elif self.b1 < key and self.b3 is not None:
                self.b3 = self.b3.fonk8(key)
            elif self.b1 = = key:
                if self.b2 is None:
                    b4 = self.b3
                    del self
                    return b4
                elif self.b3 is None:
                    b4 = self.b2
                    del self
                    return b4
                b5 = self.b3.fonk5()
                self.b1 = b5
                self.b3 = self.b3.fonk8(b5)
            else:
                return self
            return self
    def fonk9(self):
        if self.b1 is None:
            print("Nothing to print. The tree is empty")
        else:
            if self.b2 is not None:
                self.b2.fonk9()
            print(self.b1)
            if self.b3 is not None:
                self.b3.fonk9()
    def fonk10(self):
        if self:
            print("b6 = " + str(self.b1))
        else:
            print("The tree is empty.")
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
    b8.fonk9()
    print("Element: " + str(b8.fonk4(78)))
    print("Minimum value in tree is: " + str(b8.fonk5()))
    print("Maximum value in tree is: " + str(b8.fonk6()))
    b8.fonk4(21)
    b8.fonk4(201)
    b8.fonk8(243)
    b8.fonk8(20)
    b8.fonk9()
    b8.fonk10()
    b8.fonk2()
    b8.fonk9()
    print("Insertion after making tree empty")
    b8.fonk7(16)
    b8.fonk9()
    b8.fonk7(14)
    b8.fonk7(19)
    b8.fonk9()
class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
    def fonk2(self):
        if self.b1 is None:
            print("Tree is already empty ...")
            return
        self.fonk3()
        self.b1 = None
        print("Deleted every node ... Now the tree is empty")
    def fonk3(self):
        if self.b2 is not None:
            self.b2.fonk3()
            self.b2 = None
        if self.b3 is not None:
            self.b3.fonk3()
            self.b3 = None
    def fonk4(self, key):
        if self.b1 is None:
            print("Nothing to find... Tree is empty.")
            return None
        if key < self.b1:
            return self.b2.fonk4(key) if self.b2 else None
        elif key > self.b1:
            return self.b3.fonk4(key) if self.b3 else None
        else:
            print(f"Node {key}: Found.")
            return self.b1
    def fonk5(self):
        if self.b1 is None:
            print("Nothing to find... Tree is empty.")
            return None
        return self.b2.fonk5() if self.b2 else self.b1
    def fonk6(self):
        if self.b1 is None:
            print("Nothing to find... Tree is empty.")
            return None
        return self.b3.fonk6() if self.b3 else self.b1
    def fonk7(self, key):
        if self.b1 is None:
            self.b1 = key
        elif key < self.b1:
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
            print(f"Couldn't insert node {key}, because it already exists.")
    def fonk8(self, key):
        if self.b1 is None:
            print("Nothing to delete... Tree is empty.")
            return self
        if key < self.b1:
            if self.b2:
                self.b2 = self.b2.fonk8(key)
        elif key > self.b1:
            if self.b3:
                self.b3 = self.b3.fonk8(key)
        else:
            if self.b2 is None:
                return self.b3
            if self.b3 is None:
                return self.b2
            b4 = self.b3.fonk5()
            self.b1 = b4
            self.b3 = self.b3.fonk8(b4)
        return self
    def fonk9(self):
        if self.b1 is None:
            print("Nothing to print... Tree is empty")
            return
        if self.b2:
            self.b2.fonk9()
        print(self.b1)
        if self.b3:
            self.b3.fonk9()
    def fonk10(self):
        if self.b1:
            print("b5 = ", self.b1)
        else:
            print("Tree is empty.")
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
    print("Tree structure:")
    b7.fonk9()
    print("\nSearching for elements:")
    b7.fonk4(78)
    print("Minimum value in tree:", b7.fonk5())
    print("Maximum value in tree:", b7.fonk6())
    b7.fonk4(21)
    b7.fonk4(201)
    print("\nDeleting nodes:")
    b7.fonk8(243)
    b7.fonk8(20)
    print("\nTree structure after deletions:")
    b7.fonk9()
    b7.fonk10()
    print("\nEmptying the tree:")
    b7.fonk2()
    b7.fonk9()
    print("\nInsertion after making tree empty:")
    b7.fonk7(16)
    b7.fonk9()
    b7.fonk7(14)
    b7.fonk7(19)
    b7.fonk9()
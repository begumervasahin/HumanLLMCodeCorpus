class class1:
    def fonk1(self, b1 = None, next_node=None, prev_node=None):
        self.b1 = b1
        self.b2 = next_node
        self.b3 = prev_node
class class2:
    def fonk2(self, b1 = None):
        self.b4 = class1(b1) if b1 is not None else None
    def fonk3(self, b1):
        b5 = self.b4
        while b5 is not None:
            if b5.b1 = = b1:
                if b5.b3 is not None:
                    b5.b3.b2 = b5.b2
                if b5.b2 is not None:
                    b5.b2.b3 = b5.b3
                if b5 = = self.b4:
                    self.b4 = b5.b2
                del b5
                return 0
            b5 = b5.b2
        return -1
    def fonk4(self, b1):
        b6 = class1(b1)
        if self.b4 is None or b1 < self.b4.b1:
            b6.b2 = self.b4
            if self.b4 is not None:
                self.b4.b3 = b6
            self.b4 = b6
        else:
            b5 = self.b4
            while b5.b2 is not None and b5.b2.b1 < b1:
                b5 = b5.b2
            b6.b2 = b5.b2
            if b5.b2 is not None:
                b5.b2.b3 = b6
            b5.b2 = b6
            b6.b3 = b5
    def fonk5(self):
        if self.b4 is None:
            print("Empty.")
        else:
            b5 = self.b4
            b7 = []
            while b5 is not None:
                b7.append(b5.b1)
                b5 = b5.b2
            print(", ".join(map(str, b7)))
def fonk6():
    b8 = class2(0)
    print("Initial list:")
    b8.fonk5()
    print("\nInserting 1...")
    b8.fonk4(1)
    print("List after inserting 1:")
    b8.fonk5()
    print("\nInserting 5...")
    b8.fonk4(5)
    print("List after inserting 5:")
    b8.fonk5()
    print("\nRemoving 1...")
    b8.fonk3(1)
    print("List after removing 1:")
    b8.fonk5()
    print("\nRemoving 5...")
    b8.fonk3(5)
    print("List after removing 5:")
    b8.fonk5()
    print("\nRemoving 0...")
    b8.fonk3(0)
    print("List after removing 0:")
    b8.fonk5()
if b9 = = "__main__":
    fonk6()
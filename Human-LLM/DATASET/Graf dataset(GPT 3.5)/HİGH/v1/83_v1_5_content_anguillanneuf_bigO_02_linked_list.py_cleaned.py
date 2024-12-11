class class1(object):
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
class class2(object):
    def fonk2(self, b3 = None):
        self.b3 = b3
    def fonk3(self, new_element):
        b4 = self.b3
        if self.b3:
            while b4.b2:
                b4 = b4.b2
            b4.b2 = new_element
        else:
            self.b3 = new_element
    def fonk4(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list.Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements.Delete the first node with a given b1."""
        b5 = None
        b4 = self.b3
        while b4:
            if b4.b1 = = b1:
                if b5:
                    b5.b2 = b4.b2
                else:
                    self.b3 = b4.b2
                break
            b5 = b4
            b4 = b4.b2
b6 = class1(1)
b7 = class1(2)
b8 = class1(3)
b9 = class1(4)
b10 = class2(b6)
b10.fonk3(b7)
b10.fonk3(b8)
print(b10.b3.b2.b2.b1)
print(b10.fonk4(3).b1)
b10.insert(b9, 3)
print(b10.fonk4(3).b1)
b10.delete(1)
print(b10.fonk4(1).b1)
print(b10.fonk4(2).b1)
print(b10.fonk4(3).b1)

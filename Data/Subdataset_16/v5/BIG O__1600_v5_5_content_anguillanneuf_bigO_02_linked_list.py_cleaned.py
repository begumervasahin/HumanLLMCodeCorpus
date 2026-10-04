class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self, b3 = None):
        self.b3 = b3
    def fonk3(self, new_element):
        if not self.b3:
            self.b3 = new_element
            return
        b4 = self.b3
        while b4.b2:
            b4 = b4.b2
        b4.b2 = new_element
    def fonk4(self, position):
        """
        Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if the position is not in the list.
        Args:
            position (int): The position to retrieve the element from.
        Returns:
            class1 or None: The element at the specified position or None if the position is out of bounds.
        Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between the 2nd and 3rd elements.
        Args:
            new_element (class1): The element to insert.
            position (int): The position at which to insert the new element.
        Delete the first node with the given b1.
        Args:
            b1 (any): The b1 of the element to delete.
        """
        b4 = self.b3
        b5 = None
        while b4 and b4.b1 != b1:
            b5 = b4
            b4 = b4.b2
        if b5 is None:
            self.b3 = b4.b2
        elif b4:
            b5.b2 = b4.b2
if b6 = = "__main__":
    b7 = class1(1)
    b8 = class1(2)
    b9 = class1(3)
    b10 = class1(4)
    b11 = class2(b7)
    b11.fonk3(b8)
    b11.fonk3(b9)
    print(b11.fonk4(3).b1)
    b11.insert(b10, 3)
    print(b11.fonk4(3).b1)
    b11.delete(1)
    print(b11.fonk4(1).b1)
    print(b11.fonk4(2).b1)
    print(b11.fonk4(3).b1)

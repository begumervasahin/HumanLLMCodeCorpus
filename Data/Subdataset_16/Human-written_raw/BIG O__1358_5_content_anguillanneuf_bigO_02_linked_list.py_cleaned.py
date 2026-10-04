"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom.Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list.Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements.Delete the first node with a given value."""
        b1 = None
        b2 = self.b3
        a1 = 1
        while b2.value != value:
            b1 = b2
            b2 = b2.b4
            a1 += 1
        if a1 = = 1:
            self.b3 = self.b3.b4
        else:
            b1.b4 = b2.b4
b5 = Element(1)
b6 = Element(2)
b7 = Element(3)
b8 = Element(4)
b9 = LinkedList(b5)
b9.append(b6)
b9.append(b7)
print(b9.b3.b4.b4.value)
print(b9.get_position(3).value)
b9.insert(b8, 3)
print(b9.get_position(3).value)
b9.delete(1)
print(b9.get_position(1).value)
print(b9.get_position(2).value)
print(b9.get_position(3).value)
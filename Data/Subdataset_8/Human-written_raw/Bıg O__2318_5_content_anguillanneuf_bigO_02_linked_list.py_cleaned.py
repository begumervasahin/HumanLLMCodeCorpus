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
        prev = None
        current = self.head
        i = 1
        while current.value != value:
            prev = current
            current = current.next
            i += 1
        if i == 1:
            self.head = self.head.next
        else:
            prev.next = current.next
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
print(ll.head.next.next.value)
print(ll.get_position(3).value)
ll.insert(e4, 3)
print(ll.get_position(3).value)
ll.delete(1)
print(ll.get_position(1).value)
print(ll.get_position(2).value)
print(ll.get_position(3).value)
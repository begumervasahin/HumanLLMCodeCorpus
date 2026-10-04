class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list.Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements.Delete the first node with a given value."""
        current = self.head
        previous = None
        while current:
            if current.value == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return
            previous = current
            current = current.next
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
print(ll.get_position(4).value)
ll.delete(1)
print(ll.get_position(1).value)
print(ll.get_position(2).value)
print(ll.get_position(3).value)

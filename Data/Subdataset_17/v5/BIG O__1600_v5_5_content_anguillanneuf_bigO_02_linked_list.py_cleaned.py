class Element:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self, head=None):
        self.head = head
    def append(self, new_element):
        if not self.head:
            self.head = new_element
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_element
    def get_position(self, position):
        """
        Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if the position is not in the list.
        Args:
            position (int): The position to retrieve the element from.
        Returns:
            Element or None: The element at the specified position or None if the position is out of bounds.
        Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between the 2nd and 3rd elements.
        Args:
            new_element (Element): The element to insert.
            position (int): The position at which to insert the new element.
        Delete the first node with the given value.
        Args:
            value (any): The value of the element to delete.
        """
        current = self.head
        previous = None
        while current and current.value != value:
            previous = current
            current = current.next
        if previous is None:
            self.head = current.next
        elif current:
            previous.next = current.next
if __name__ == "__main__":
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)
    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)
    print(ll.get_position(3).value)
    ll.insert(e4, 3)
    print(ll.get_position(3).value)
    ll.delete(1)
    print(ll.get_position(1).value)
    print(ll.get_position(2).value)
    print(ll.get_position(3).value)

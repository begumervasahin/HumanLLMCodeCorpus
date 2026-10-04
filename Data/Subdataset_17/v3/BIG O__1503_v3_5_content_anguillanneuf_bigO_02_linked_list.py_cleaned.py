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
            position (int): The position of the element (1-based index).
        Returns:
            Element: The element at the specified position, or None if not found.
        Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between the 2nd and 3rd elements.
        Args:
            new_element (Element): The new element to be inserted.
            position (int): The position where the new element should be inserted (1-based index).
        Delete the first node with a given value.
        Args:
            value (any): The value of the element to be deleted.
        """
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
if __name__ == "__main__":
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

class Element:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
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
        current = self.head
        i = 1
        while current and i < position:
            current = current.next
            i += 1
        return current
    def insert(self, new_element, position):
        if position == 1:
            new_element.next = self.head
            self.head = new_element
            return
        prev = self.get_position(position - 1)
        if prev:
            new_element.next = prev.next
            prev.next = new_element
    def delete(self, value):
        current = self.head
        prev = None
        while current:
            if current.value == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
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
ll.delete(1)
print(ll.get_position(1).value)
print(ll.get_position(2).value)
print(ll.get_position(3).value)

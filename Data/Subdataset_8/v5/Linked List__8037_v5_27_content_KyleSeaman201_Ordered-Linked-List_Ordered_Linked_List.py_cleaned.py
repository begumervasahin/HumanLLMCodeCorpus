class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)
class OrderedLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def add(self, value):
        new_node = Node(value)
        if self.head is None or self.head.value >= new_node.value:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.value < new_node.value:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        if new_node.next is None:
            self.tail = new_node
        self.size += 1
    def delete(self, value):
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.size -= 1
            return
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        if current.next and current.next.value == value:
            current.next = current.next.next
            if current.next is None:
                self.tail = current
            self.size -= 1
    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
    def pop(self):
        if self.head is None:
            return None
        if self.head == self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
            self.size = 0
            return value
        current = self.head
        while current.next != self.tail:
            current = current.next
        value = self.tail.value
        current.next = None
        self.tail = current
        self.size -= 1
        return value
    def is_empty(self):
        return self.size == 0
    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current))
            current = current.next
        return ' -> '.join(elements)

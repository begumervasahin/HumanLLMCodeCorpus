class Node:
    __slots__ = 'val', 'next'
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def __lt__(self, other):
        return self.val < other.val
    def __le__(self, other):
        return self.val <= other.val
class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.val))
            current = current.next
        return ", ".join(values)
    __repr__ = __str__
    def __len__(self):
        return self.size
    def is_empty(self):
        return self.size == 0
    def enqueue(self, element):
        new_node = Node(element)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        value = self.head.val
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return value
    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    def __setitem__(self, index, val):
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        current.val = val
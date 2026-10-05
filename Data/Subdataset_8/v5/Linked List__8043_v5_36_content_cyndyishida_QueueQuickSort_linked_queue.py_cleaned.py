class Node:
    __slots__ = 'val', 'next'
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node
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
        values = [str(node.val) for node in self]
        return ", ".join(values)
    __repr__ = __str__
    def __len__(self):
        return self.size
    def is_empty(self):
        return self.size == 0
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        answer = self.head.val
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return answer
    def enqueue(self, element):
        newest = Node(element)
        if self.is_empty():
            self.head = newest
        else:
            self.tail.next = newest
        self.tail = newest
        self.size += 1
    def __getitem__(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    def __setitem__(self, index, val):
        current = self.head
        for _ in range(index):
            current = current.next
        current.val = val
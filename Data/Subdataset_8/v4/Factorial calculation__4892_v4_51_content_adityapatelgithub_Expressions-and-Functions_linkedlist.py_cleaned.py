class LinkedList:
    class Node:
        def __init__(self, value, next_node=None):
            self.value = value
            self.next = next_node
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next
    def __len__(self):
        return self.length
    def __str__(self):
        return " -> ".join(str(item) for item in self)
    def push(self, value):
        new_node = self.Node(value, self.head)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.head = new_node
        self.length += 1
    def pop(self):
        if not self.head:
            raise IndexError("pop from empty list")
        value = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.length -= 1
        return value
    def top(self):
        if not self.tail:
            raise IndexError("list is empty")
        return self.tail.value
    def is_empty(self):
        return self.length == 0
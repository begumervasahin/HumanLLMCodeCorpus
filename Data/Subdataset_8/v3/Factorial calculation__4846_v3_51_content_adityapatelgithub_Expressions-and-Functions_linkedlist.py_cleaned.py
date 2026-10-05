class LinkedList:
    class _Node:
        def __init__(self, value, next_node=None):
            self.value = value
            self.next = next_node
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0
    def __iter__(self):
        current = self._head
        while current:
            yield current.value
            current = current.next
    def __len__(self):
        return self._length
    def __str__(self):
        return "->".join(str(value) for value in self)
    def append(self, value):
        new_node = self._Node(value)
        if not self._head:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._length += 1
    def prepend(self, value):
        new_node = self._Node(value, self._head)
        self._head = new_node
        if not self._tail:
            self._tail = new_node
        self._length += 1
    def pop_first(self):
        if not self._head:
            raise IndexError("pop from empty list")
        value = self._head.value
        self._head = self._head.next
        if not self._head:
            self._tail = None
        self._length -= 1
        return value
    def first(self):
        if not self._head:
            raise IndexError("list is empty")
        return self._head.value
    def last(self):
        if not self._tail:
            raise IndexError("list is empty")
        return self._tail.value
    def is_empty(self):
        return self._length == 0
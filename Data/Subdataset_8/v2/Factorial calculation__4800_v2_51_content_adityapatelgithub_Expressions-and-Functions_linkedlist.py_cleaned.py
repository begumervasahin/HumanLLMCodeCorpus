class LinkedList:
    class Node:
        __slots__ = "_value", "_next"
        def __init__(self, value, next_node):
            self._value = value
            self._next = next_node
    def __init__(self):
        self._tail = None
        self._head = None
        self._length = 0
    def __iter__(self):
        current = self._head
        while current is not None:
            yield current._value
            current = current._next
    def __len__(self):
        return self._length
    def __str__(self):
        return "".join(list(iter(self)))
    def push(self, value):
        new_node = self.Node(value, None)
        if self._head is None:
            self._head = self._tail = new_node
        else:
            new_node._next = self._head
            self._head = new_node
        self._length += 1
    def pop(self):
        value = self._head._value
        self._head = self._head._next
        self._length -= 1
        return value
    def top(self):
        return self._tail._value
    def is_empty(self):
        return self._length == 0
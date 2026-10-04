class LinkedList:
    class Node:
        __slots__ = "_value", "_next"
        def __init__(self, v, n):
            self._value = v
            self._next = n
    def __init__(self):
        self._head = None
        self._tail = None
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
        if self._head is None:
            raise IndexError("pop from empty list")
        value = self._head._value
        self._head = self._head._next
        self._length -= 1
        if self._head is None:
            self._tail = None
        return value
    def top(self):
        if self._tail is None:
            raise IndexError("top from empty list")
        return self._tail._value
    def is_empty(self):
        return self._length == 0
if __name__ == "__main__":
    ll = LinkedList()
    ll.push('a')
    ll.push('b')
    ll.push('c')
    print("List:", str(ll))
    print("Length:", len(ll))
    print("Top:", ll.top())
    print("Pop:", ll.pop())
    print("List after pop:", str(ll))
    print("Is empty:", ll.is_empty())

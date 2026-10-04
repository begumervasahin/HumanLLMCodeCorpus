class LinkedList:
    class Node:
        __slots__ = "_value","_next"
        def __init__(self, v, n):
            self._value = v
            self._next = n
    def __init__(self):
        self._tail = None
        self._head = None
        self._length = 0
    def __iter__(self):
        current = self._head
        while (current is not None):
            yield current._value
            current = current._next
    def __len__(self):
        return self._length
    def __str__(self):
        return "".join( list(iter(self)))
    def push(self,value):
        newNode = self.Node(value, None)
        if(self._head is None):
            self._head = self._tail = newNode
        else:
            newNode._next = self._head
            self._head = newNode
        self._length+=1
    def pop(self):
        val = self._head._value
        self._head = self._head._next
        self._length-=1
        return val
    def top(self):
        return self._tail._value
    def is_empty(self):
        return (self._length == 0)
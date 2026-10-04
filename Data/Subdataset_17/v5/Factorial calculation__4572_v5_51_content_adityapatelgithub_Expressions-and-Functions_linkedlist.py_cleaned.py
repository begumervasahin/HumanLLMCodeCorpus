class LinkedList:
    class Node:
        __slots__ = "value", "next"
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
        return "".join(str(value) for value in self)
    def push(self, value):
        new_node = self.Node(value, self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self.length += 1
    def pop(self):
        if self.head is None:
            raise IndexError("pop from empty list")
        value = self.head.value
        self.head = self.head.next
        self.length -= 1
        if self.head is None:
            self.tail = None
        return value
    def top(self):
        if self.tail is None:
            raise IndexError("top from empty list")
        return self.tail.value
    def is_empty(self):
        return self.length == 0
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

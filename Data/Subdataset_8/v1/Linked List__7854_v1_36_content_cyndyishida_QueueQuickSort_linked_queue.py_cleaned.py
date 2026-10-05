class Node:
    __slots__ = 'val', 'next'
    def __init__(self, val, next_node):
        self.val = val
        self.next = next_node
    def __lt__(self, other):
        return self.val <= other.val
    def __le__(self, other):
        return self.val <= other.val
class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def __str__(self):
        head = self.head
        values = []
        while head:
            values.append(str(head.val))
            head = head.next
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
        newest = Node(element, None)
        if self.is_empty():
            self.head = newest
        else:
            self.tail.next = newest
        self.tail = newest
        self.size += 1
    def __getitem__(self, index):
        if not (0 <= index < self.size):
            raise IndexError("Index out of range")
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val
    def __setitem__(self, index, val):
        if not (0 <= index < self.size):
            raise IndexError("Index out of range")
        curr = self.head
        for _ in range(index):
            curr = curr.next
        curr.val = val
if __name__ == "__main__":
    queue = LinkedQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Queue:", queue)
    print("Length:", len(queue))
    print("Dequeue:", queue.dequeue())
    print("Queue after dequeue:", queue)
    queue[0] = 5
    print("Queue after setting value at index 0:", queue)
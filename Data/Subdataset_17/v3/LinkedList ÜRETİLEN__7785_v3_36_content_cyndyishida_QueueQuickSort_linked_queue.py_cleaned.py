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
        current = self.head
        values = []
        while current:
            values.append(str(current.val))
            current = current.next
        return ", ".join(values)
    __repr__ = __str__
    def __len__(self):
        return self.size
    def is_empty(self):
        return self.size == 0
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        value = self.head.val
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return value
    def enqueue(self, element):
        new_node = Node(element)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1
    def __getitem__(self, index):
        if index >= self.size or index < 0:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val
    def __setitem__(self, index, val):
        if index >= self.size or index < 0:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        current.val = val
if __name__ == "__main__":
    queue = LinkedQueue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Queue after enqueuing 10, 20, 30:", queue)
    print("Length of queue:", len(queue))
    print("Dequeue element:", queue.dequeue())
    print("Queue after dequeue:", queue)
    print("Element at index 1:", queue[1])
    queue[1] = 50
    print("Queue after setting element at index 1 to 50:", queue)
    print("Is the queue empty?", queue.is_empty())
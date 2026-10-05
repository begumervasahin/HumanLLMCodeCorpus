class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next = next_node
    def __lt__(self, other):
        return self.value <= other.value
    def __le__(self, other):
        return self.value <= other.value
class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def __str__(self):
        current = self.head
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        return ", ".join(values)
    __repr__ = __str__
    def __len__(self):
        return self.size
    def is_empty(self):
        return self.size == 0
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return value
    def enqueue(self, element):
        new_node = Node(element, None)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1
    def __getitem__(self, index):
        if not (0 <= index < self.size):
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value
    def __setitem__(self, index, value):
        if not (0 <= index < self.size):
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = value
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
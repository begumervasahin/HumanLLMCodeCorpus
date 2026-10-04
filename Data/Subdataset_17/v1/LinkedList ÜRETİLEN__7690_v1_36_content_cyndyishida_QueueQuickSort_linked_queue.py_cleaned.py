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
            raise IndexError("Dequeue from empty queue")
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
        if index >= self.size or index < 0:
            raise IndexError("Index out of range")
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val
    def __setitem__(self, index, val):
        if index >= self.size or index < 0:
            raise IndexError("Index out of range")
        curr = self.head
        for _ in range(index):
            curr = curr.next
        curr.val = val
if __name__ == "__main__":
    q = LinkedQueue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("Queue after enqueuing 10, 20, 30:", q)
    print("Length of queue:", len(q))
    print("Dequeue element:", q.dequeue())
    print("Queue after dequeue:", q)
    print("Element at index 1:", q[1])
    q[1] = 50
    print("Queue after setting element at index 1 to 50:", q)
    print("Is the queue empty?", q.is_empty())
import sys
class Stack:
    def __init__(self):
        self._items = []
    def push(self, item):
        self._items.append(item)
    def peek(self):
        if not self._items:
            raise IndexError("Stack is empty")
        return self._items[-1]
    def pop(self):
        if not self._items:
            raise IndexError("Stack is empty")
        return self._items.pop()
    def __len__(self):
        return len(self._items)
    def get_size(self):
        return sys.getsizeof(self._items)
class CircularQueue:
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self._items = [None] * CircularQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def first(self):
        if self.is_empty():
            raise IndexError("Empty Queue")
        return self._items[self._front]
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Empty Queue")
        value = self._items[self._front]
        self._items[self._front] = None
        self._front = (self._front + 1) % len(self._items)
        self._size -= 1
        return value
    def enqueue(self, item):
        if self._size == len(self._items):
            self._resize(len(self._items) * 2)
        next_index = (self._front + self._size) % len(self._items)
        self._items[next_index] = item
        self._size += 1
    def _resize(self, capacity):
        old_items = self._items
        self._items = [None] * capacity
        current_index = self._front
        for i in range(self._size):
            self._items[i] = old_items[current_index]
            current_index = (current_index + 1) % len(old_items)
        self._front = 0
    def get_size(self):
        return sys.getsizeof(self._items)
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.peek())
    queue = CircularQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())
    print(queue.first())

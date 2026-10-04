class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return not self.items
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop()
    def first(self):
        if self.is_empty():
            raise IndexError("first from empty queue")
        return self.items[0]
    def size(self):
        return len(self.items)
    def enqueue_items(self, items):
        for item in items:
            self.enqueue(item)
class BQueue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return not self.items
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop()
    def size(self):
        return len(self.items)
def main():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("Queue items:", q.items)
    print("Dequeue from Queue:", q.dequeue())
    print("First item in Queue:", q.first())
    print("Queue size:", q.size())
    bq = BQueue()
    bq.enqueue(1)
    bq.enqueue(2)
    bq.enqueue(3)
    print("BQueue items:", bq.items)
    print("Dequeue from BQueue:", bq.dequeue())
    print("BQueue size:", bq.size())
if __name__ == "__main__":
    main()
class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("dequeue from empty queue")
    def first(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("first from empty queue")
    def size(self):
        return len(self.items)
    def enqueue_items(self, items):
        for el in items:
            self.enqueue(el)
class BQueue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("dequeue from empty queue")
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
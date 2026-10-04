class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Dequeue from an empty queue.")
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
def main():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print("Queue size after enqueuing 5 items:", q.size())
    print("Dequeuing items:")
    while not q.is_empty():
        print(q.dequeue())
    print("Queue size after dequeuing all items:", q.size())
if __name__ == '__main__':
    main()
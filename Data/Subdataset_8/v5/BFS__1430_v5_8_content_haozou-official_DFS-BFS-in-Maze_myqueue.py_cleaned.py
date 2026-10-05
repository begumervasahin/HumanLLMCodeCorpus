class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
def main():
    q = Queue()
    for i in range(1, 6):
        q.enqueue(i)
    print("Queue size:", q.size())
    print("Dequeuing items:")
    while not q.is_empty():
        print(q.dequeue())
    print("Queue size after dequeueing:", q.size())
if __name__ == '__main__':
    main()
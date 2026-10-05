class Queue:
    def __init__(self):
        self.items = []
        self.state = set()
    def enqueue(self, item):
        self.items.append(item)
        self.state.add(tuple(item.list))
    def dequeue(self):
        if not self.is_empty():
            item = self.items.pop(0)
            self.state.remove(tuple(item.list))
            return item
    def is_empty(self):
        return len(self.items) == 0
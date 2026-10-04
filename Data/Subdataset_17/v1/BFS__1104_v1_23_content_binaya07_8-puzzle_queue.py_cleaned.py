class Queue:
    def __init__(self):
        self.list = []
        self.state = set()
    def enqueue(self, item):
        self.list.append(item)
        self.state.add(tuple(item.list))
    def dequeue(self):
        if not self.isEmpty():
            item = self.list[0]
            for i in range(len(self.list) - 1):
                self.list[i] = self.list[i + 1]
            del self.list[-1]
            self.state.remove(tuple(item.list))
            return item
    def isEmpty(self):
        return len(self.list) == 0
if __name__ == "__main__":
    class PuzzleState:
        def __init__(self, state_list):
            self.list = state_list
        def __repr__(self):
            return str(self.list)
    q = Queue()
    q.enqueue(PuzzleState([1, 2, 3, 4, 5, 6, 7, 8, 0]))
    q.enqueue(PuzzleState([1, 2, 3, 4, 5, 6, 0, 7, 8]))
    q.enqueue(PuzzleState([1, 2, 3, 4, 5, 0, 6, 7, 8]))
    while not q.isEmpty():
        state = q.dequeue()
        print("Dequeued:", state)
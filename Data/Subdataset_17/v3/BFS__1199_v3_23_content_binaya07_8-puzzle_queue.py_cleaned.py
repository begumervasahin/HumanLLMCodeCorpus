class Queue:
    def __init__(self):
        self.items = []
        self.state = set()
    def enqueue(self, item):
        self.items.append(item)
        self.state.add(tuple(item.state_list))
    def dequeue(self):
        if not self.is_empty():
            item = self.items.pop(0)
            self.state.remove(tuple(item.state_list))
            return item
        return None
    def is_empty(self):
        return len(self.items) == 0
class PuzzleState:
    def __init__(self, state_list):
        self.state_list = state_list
    def __repr__(self):
        return str(self.state_list)
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(PuzzleState([1, 2, 3, 4, 5, 6, 7, 8, 0]))
    queue.enqueue(PuzzleState([1, 2, 3, 4, 5, 6, 0, 7, 8]))
    queue.enqueue(PuzzleState([1, 2, 3, 4, 5, 0, 6, 7, 8]))
    while not queue.is_empty():
        state = queue.dequeue()
        print("Dequeued:", state)
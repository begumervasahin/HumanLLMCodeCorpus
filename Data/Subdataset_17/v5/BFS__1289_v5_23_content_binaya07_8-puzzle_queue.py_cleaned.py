class Queue:
    def __init__(self):
        self.items = []
        self.state = set()
    def enqueue(self, item):
        self.items.append(item)
        self.state.add(tuple(item.state))
    def dequeue(self):
        if not self.is_empty():
            item = self.items.pop(0)
            self.state.remove(tuple(item.state))
            return item
        return None
    def is_empty(self):
        return len(self.items) == 0
class PuzzleState:
    def __init__(self, state_list):
        self.state = state_list
    def __repr__(self):
        return f"PuzzleState({self.state})"
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(PuzzleState([1, 2, 3, 4, 5, 6, 7, 8, 0]))
    queue.enqueue(PuzzleState([1, 2, 3, 4, 5, 6, 7, 0, 8]))
    print(f"Queue is empty: {queue.is_empty()}")
    dequeued_item = queue.dequeue()
    print(f"Dequeued: {dequeued_item}")
    print(f"Queue is empty: {queue.is_empty()}")
    dequeued_item = queue.dequeue()
    print(f"Dequeued: {dequeued_item}")
    print(f"Queue is empty: {queue.is_empty()}")
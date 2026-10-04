class Queue:
    def __init__(self):
        self.list = []
        self.state = set()
    def enqueue(self, item):
        self.list.append(item)
        self.state.add(tuple(item.list))
    def dequeue(self):
        if not self.is_empty():
            item = self.list.pop(0)
            self.state.remove(tuple(item.list))
            return item
        else:
            return None
    def is_empty(self):
        return len(self.list) == 0
if __name__ == "__main__":
    class PuzzleState:
        def __init__(self, state_list):
            self.list = state_list
        def __repr__(self):
            return f"PuzzleState({self.list})"
    q = Queue()
    q.enqueue(PuzzleState([1, 2, 3, 4, 5, 6, 7, 8, 0]))
    q.enqueue(PuzzleState([1, 2, 3, 4, 5, 6, 7, 0, 8]))
    print(f"Queue is empty: {q.is_empty()}")
    dequeued_item = q.dequeue()
    print(f"Dequeued: {dequeued_item}")
    print(f"Queue is empty: {q.is_empty()}")
    dequeued_item = q.dequeue()
    print(f"Dequeued: {dequeued_item}")
    print(f"Queue is empty: {q.is_empty()}")
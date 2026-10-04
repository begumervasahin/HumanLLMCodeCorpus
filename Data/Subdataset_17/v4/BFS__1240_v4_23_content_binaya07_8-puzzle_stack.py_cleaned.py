class Stack:
    def __init__(self):
        self.list = []
        self.state = set()
    def push(self, item):
        self.list.append(item)
        self.state.add(tuple(item.list))
    def pop(self):
        if not self.is_empty():
            top_item = self.list.pop()
            self.state.remove(tuple(top_item.list))
            return top_item
        else:
            return None
    def is_empty(self):
        return len(self.list) == 0
    def clear_stack(self):
        self.list.clear()
        self.state.clear()
if __name__ == "__main__":
    class PuzzleState:
        def __init__(self, state_list):
            self.list = state_list
        def __repr__(self):
            return f"PuzzleState({self.list})"
    s = Stack()
    s.push(PuzzleState([1, 2, 3, 4, 5, 6, 7, 8, 0]))
    s.push(PuzzleState([1, 2, 3, 4, 5, 6, 7, 0, 8]))
    print(f"Stack is empty: {s.is_empty()}")
    popped_item = s.pop()
    print(f"Popped: {popped_item}")
    print(f"Stack is empty: {s.is_empty()}")
    popped_item = s.pop()
    print(f"Popped: {popped_item}")
    print(f"Stack is empty: {s.is_empty()}")
    s.clear_stack()
    print(f"Stack cleared. Stack is empty: {s.is_empty()}")
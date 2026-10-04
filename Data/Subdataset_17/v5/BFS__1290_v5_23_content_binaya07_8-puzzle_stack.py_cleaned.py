class Stack:
    def __init__(self):
        self.items = []
        self.state = set()
    def push(self, item):
        self.items.append(item)
        self.state.add(tuple(item.state))
    def pop(self):
        if not self.is_empty():
            top_item = self.items.pop()
            self.state.remove(tuple(top_item.state))
            return top_item
        return None
    def is_empty(self):
        return len(self.items) == 0
    def clear(self):
        self.items.clear()
        self.state.clear()
class PuzzleState:
    def __init__(self, state_list):
        self.state = state_list
    def __repr__(self):
        return f"PuzzleState({self.state})"
if __name__ == "__main__":
    stack = Stack()
    stack.push(PuzzleState([1, 2, 3, 4, 5, 6, 7, 8, 0]))
    stack.push(PuzzleState([1, 2, 3, 4, 5, 6, 7, 0, 8]))
    print(f"Stack is empty: {stack.is_empty()}")
    popped_item = stack.pop()
    print(f"Popped: {popped_item}")
    print(f"Stack is empty: {stack.is_empty()}")
    popped_item = stack.pop()
    print(f"Popped: {popped_item}")
    print(f"Stack is empty: {stack.is_empty()}")
    stack.clear()
    print(f"Stack cleared. Stack is empty: {stack.is_empty()}")
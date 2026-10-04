class Stack:
    def __init__(self):
        self.items = []
        self.state = set()
    def push(self, item):
        self.items.append(item)
        self.state.add(tuple(item.state_list))
    def pop(self):
        if not self.is_empty():
            item = self.items.pop()
            self.state.remove(tuple(item.state_list))
            return item
        return None
    def is_empty(self):
        return len(self.items) == 0
    def clear(self):
        self.items.clear()
        self.state.clear()
class PuzzleState:
    def __init__(self, state_list):
        self.state_list = state_list
    def __repr__(self):
        return str(self.state_list)
if __name__ == "__main__":
    stack = Stack()
    stack.push(PuzzleState([1, 2, 3, 4, 5, 6, 7, 8, 0]))
    stack.push(PuzzleState([1, 2, 3, 4, 5, 6, 0, 7, 8]))
    stack.push(PuzzleState([1, 2, 3, 4, 5, 0, 6, 7, 8]))
    while not stack.is_empty():
        state = stack.pop()
        print("Popped:", state)
    stack.clear()
    print("Stack cleared. Is empty:", stack.is_empty())
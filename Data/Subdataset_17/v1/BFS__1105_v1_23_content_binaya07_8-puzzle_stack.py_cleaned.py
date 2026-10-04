class Stack:
    def __init__(self):
        self.list = []
        self.state = set()
    def push(self, item):
        self.list.append(item)
        self.state.add(tuple(item.list))
    def pop(self):
        if not self.isEmpty():
            tos = self.list[-1]
            del self.list[-1]
            self.state.remove(tuple(tos.list))
            return tos
        else:
            return None
    def isEmpty(self):
        return len(self.list) == 0
    def clear_stack(self):
        self.list.clear()
        self.state.clear()
if __name__ == "__main__":
    class PuzzleState:
        def __init__(self, state_list):
            self.list = state_list
        def __repr__(self):
            return str(self.list)
    s = Stack()
    s.push(PuzzleState([1, 2, 3, 4, 5, 6, 7, 8, 0]))
    s.push(PuzzleState([1, 2, 3, 4, 5, 6, 0, 7, 8]))
    s.push(PuzzleState([1, 2, 3, 4, 5, 0, 6, 7, 8]))
    while not s.isEmpty():
        state = s.pop()
        print("Popped:", state)
    s.clear_stack()
    print("Stack cleared. Is empty:", s.isEmpty())
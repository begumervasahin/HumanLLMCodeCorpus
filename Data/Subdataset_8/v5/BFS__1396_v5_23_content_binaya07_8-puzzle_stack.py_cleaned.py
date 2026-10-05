class Stack:
    def __init__(self):
        self.stack = []
        self.unique_states = set()
    def push(self, item):
        self.stack.append(item)
        self.unique_states.add(tuple(item.stack))
    def pop(self):
        if not self.is_empty():
            top_of_stack = self.stack.pop()
            self.unique_states.remove(tuple(top_of_stack.stack))
            return top_of_stack
        else:
            return None
    def is_empty(self):
        return len(self.stack) == 0
    def clear_stack(self):
        self.stack.clear()
        self.unique_states.clear()

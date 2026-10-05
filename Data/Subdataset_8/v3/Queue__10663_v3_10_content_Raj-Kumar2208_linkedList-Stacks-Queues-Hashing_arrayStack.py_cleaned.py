class StackArray:
    def __init__(self, limit=10):
        self.limit = limit
        self.stack = []
    def push(self, data):
        if len(self.stack) >= self.limit:
            raise ValueError("Stack Overflow")
        else:
            self.stack.append(data)
    def is_empty(self):
        return len(self.stack) == 0
    def pop(self):
        if self.is_empty():
            raise ValueError("Stack Underflow")
        else:
            return self.stack.pop()
    def peek(self):
        if self.is_empty():
            raise ValueError("Stack Underflow")
        else:
            return self.stack[-1]
    def size(self):
        return len(self.stack)
    def print_stack(self):
        print(self.stack)
if __name__ == "__main__":
    stack = StackArray(5)
    print("Is stack empty?", stack.is_empty())
    stack.push(5)
    stack.push(6)
    stack.push(7)
    print("Top element:", stack.peek())
    stack.pop()
    stack.print_stack()
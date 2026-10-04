
class StackArray:
    def __init__(self, limit=10):
        self.limit = limit
        self.stack = []
    def push(self, data):
        if self.size() >= self.limit:
            raise ValueError("Stack Overflow")
        self.stack.append(data)
        print(f"Stack After Push: {self.stack}")
    def is_empty(self):
        return len(self.stack) == 0
    def pop(self):
        if self.is_empty():
            raise ValueError("Stack Underflow")
        return self.stack.pop()
    def peek(self):
        if self.is_empty():
            raise ValueError("Stack Underflow")
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    def print_stack(self):
        print(self.stack)
if __name__ == "__main__":
    stack = StackArray(5)
    print(f"Is stack empty? {stack.is_empty()}")
    stack.push(5)
    stack.push(6)
    stack.push(7)
    print(f"Top element is: {stack.peek()}")
    stack.pop()
    stack.print_stack()
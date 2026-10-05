class StackArray:
    def __init__(self, limit=10):
        self.limit = limit
        self.array = []
    def push(self, data):
        if len(self.array) >= self.limit:
            raise ValueError("Stack Overflow")
        self.array.append(data)
        print("Stack after push:", self.array)
    def is_empty(self):
        return len(self.array) == 0
    def pop(self):
        if self.is_empty():
            raise ValueError("Stack Underflow")
        return self.array.pop()
    def peek(self):
        if self.is_empty():
            raise ValueError("Stack Underflow")
        return self.array[-1]
    def size(self):
        return len(self.array)
    def print_stack(self):
        print("Current stack:", self.array)
if __name__ == "__main__":
    stack = StackArray(5)
    print("Is the stack empty?", stack.is_empty())
    stack.push(5)
    stack.push(6)
    stack.push(7)
    print("Top element of the stack:", stack.peek())
    stack.pop()
    stack.print_stack()
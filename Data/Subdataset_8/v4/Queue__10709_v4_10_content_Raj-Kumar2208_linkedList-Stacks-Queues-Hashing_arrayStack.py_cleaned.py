class StackArray:
    def __init__(self, limit=10):
        self.limit = limit
        self.arr = []
    def push(self, data):
        if len(self.arr) >= self.limit:
            raise ValueError("Stack Overflow")
        self.arr.append(data)
        print("Stack After Push:", self.arr)
    def is_empty(self):
        return len(self.arr) == 0
    def pop(self):
        if self.is_empty():
            raise ValueError("Stack Underflow")
        return self.arr.pop()
    def peek(self):
        if self.is_empty():
            raise ValueError("Stack Underflow")
        return self.arr[-1]
    def stack_size(self):
        return len(self.arr)
    def print_stack(self):
        print(self.arr)
if __name__ == "__main__":
    stack_one = StackArray(5)
    print("Is the stack empty?", stack_one.is_empty())
    stack_one.push(5)
    stack_one.push(6)
    stack_one.push(7)
    print("Top element of the stack:", stack_one.peek())
    stack_one.pop()
    stack_one.print_stack()
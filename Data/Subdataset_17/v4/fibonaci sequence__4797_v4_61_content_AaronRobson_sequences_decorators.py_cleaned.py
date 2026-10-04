
class Memoized:
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        try:
            value = self.func(*args)
            self.cache[args] = value
            return value
        except TypeError:
            return self.func(*args)
    def __repr__(self):
        return self.func.__doc__
memoized = memoised = Memoized
@memoized
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
if __name__ == "__main__":
    for i in range(10, 21, 5):
        print(f"Fibonacci({i}): {fibonacci(i)}")
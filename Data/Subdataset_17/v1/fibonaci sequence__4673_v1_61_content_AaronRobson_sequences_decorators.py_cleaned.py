class Memoized:
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
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
    print(fibonacci(10))
    print(fibonacci(15))
    print(fibonacci(20))

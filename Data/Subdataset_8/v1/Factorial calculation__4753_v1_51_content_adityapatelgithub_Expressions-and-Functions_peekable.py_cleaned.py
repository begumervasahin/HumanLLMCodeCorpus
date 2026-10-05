class Peekable():
    def __init__(self, iterator):
        self._iterator = iterator
        self._peeked = None
    def __iter__(self):
        return self
    def __next__(self):
        if self._peeked is None:
            self._peeked = next(self._iterator)
        ans = self._peeked
        self._peeked = None
        return ans
    def peek(self):
        if self._peeked is None:
            self._peeked = next(self._iterator)
        return self._peeked
def peek(x):
    return x.peek()
if __name__ == "__main__":
    i = Peekable(iter([1, 2, 3, 4, 5]))
    print(peek(i))
    print(peek(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(peek(i))
    print(next(i))
    print(list(Peekable(iter([1, 2, 3, 4, 5]))))

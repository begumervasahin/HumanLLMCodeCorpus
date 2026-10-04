class Peekable:
    def __init__(self, iterator):
        self._iterator = iterator
        self._peeked = None
    def __iter__(self):
        return self
    def __next__(self):
        if self._peeked is None:
            self._peeked = next(self._iterator)
        result = self._peeked
        self._peeked = None
        return result
    def peek(self):
        if self._peeked is None:
            self._peeked = next(self._iterator)
        return self._peeked
def peek(iterator):
    return iterator.peek()
if __name__ == "__main__":
    peekable_iter = Peekable(iter([1, 2, 3, 4, 5]))
    print(peek(peekable_iter))
    print(peek(peekable_iter))
    print(next(peekable_iter))
    print(next(peekable_iter))
    print(next(peekable_iter))
    print(peek(peekable_iter))
    print(next(peekable_iter))
    print(list(Peekable(iter([1, 2, 3, 4, 5]))))

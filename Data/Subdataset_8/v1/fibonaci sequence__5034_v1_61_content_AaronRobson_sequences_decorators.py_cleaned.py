class Memoised(object):
    '''Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned, and
    not re-evaluated.
    See: http:
    '''
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
        '''Return the function's docstring.
        '''
        return self.func.__doc__
memoized = memoised = Memoised
@memoized
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
if __name__ == "__main__":
    print(fibonacci(10))
    print(fibonacci(20))
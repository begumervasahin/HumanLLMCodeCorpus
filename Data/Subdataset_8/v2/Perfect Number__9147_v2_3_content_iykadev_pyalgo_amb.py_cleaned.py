import itertools
class AmbiguityResolver:
    def __init__(self):
        self._names2values = {}
        self._func = None
        self._value_iterator = None
        self._func_arg_names = None
    def __call__(self, arg=None):
        if hasattr(arg, '__code__'):
            globals_ = arg.__globals__ if hasattr(arg, '__globals__') else arg.func_globals
            arg_vars = arg.__code__.co_varnames[:arg.__code__.co_argcount]
            for name in arg_vars:
                if name not in self._names2values:
                    assert name in globals_, "Global name %s not found in function globals" % name
                    self._names2values[name] = globals_[name]
            value_sets = [self._names2values[name] for name in arg_vars]
            self._value_iterator = itertools.product(*value_sets)
            self._func = arg
            self._func_arg_names = arg_vars
            return self
        elif arg is not None:
            arg = frozenset(arg)
            return arg
        else:
            return self._next_in_search()
    def _next_in_search(self):
        arg = self._func
        globals_ = arg.__globals__
        arg_vars = self._func_arg_names
        found = False
        for values in self._value_iterator:
            if arg(*values):
                found = True
                for name, value in zip(arg_vars, values):
                    globals_[name] = value
                break
        if not found:
            raise StopIteration
        return values
    def __iter__(self):
        return self
    def __next__(self):
        return self()
    next = __next__
if __name__ == '__main__':
    if True:
        amb = AmbiguityResolver()
        print("\nSmall Pythagorean triples problem:")
        x = amb(range(1, 11))
        y = amb(range(1, 11))
        z = amb(range(1, 11))
        for _dummy in amb(lambda x, y, z: x * x + y * y == z * z):
            print('%s %s %s' % (x, y, z))
    if True:
        amb = AmbiguityResolver()
        print("\nThe Ambiguity Resolver problem:")
        w1 = amb(["the", "that", "a"])
        w2 = amb(["frog", "elephant", "thing"])
        w3 = amb(["walked", "treaded", "grows"])
        w4 = amb(["slowly", "quickly"])
        for _dummy in amb(lambda w1, w2, w3, w4: w1[-1] == w2[0] and w2[-1] == w3[0] and w3[-1] == w4[0]):
            print('%s %s %s %s' % (w1, w2, w3, w4))
    if True:
        amb = AmbiguityResolver()
        x = amb([1, 2, 3])
        y = amb([4, 5, 6])
        for _dummy in amb(lambda x, y: x * y != 8):
            print('%s %s' % (x, y))
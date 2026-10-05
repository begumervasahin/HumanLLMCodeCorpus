import itertools
class class1:
    def fonk1(self):
        self.b1 = {}
        self.b2 = None
        self.b3 = None
        self.b4 = None
    def fonk2(self, b5 = None):
        if hasattr(b5, '__code__'):
            self.fonk3(b5)
            return self
        elif b5 is not None:
            return frozenset(b5)
        else:
            return self.fonk4()
    def fonk3(self, func):
        b6 = func.__code__.co_varnames[:func.__code__.co_argcount]
        for name in b6:
            if name not in self.b1:
                assert name in func.__globals__, f"Global name {name} not b8 in function globals"
                self.b1[name] = func.__globals__[name]
        b7 = [self.b1[name] for name in b6]
        self.b3 = itertools.product(*b7)
        self.b2 = func
        self.b4 = b6
    def fonk4(self):
        b8 = False
        for values in self.b3:
            if self.b2(*values):
                b8 = True
                self.fonk5(values)
                break
        if not b8:
            raise StopIteration
        return values
    def fonk5(self, values):
        for name, value in zip(self.b4, values):
            self.b2.__globals__[name] = value
    def fonk6(self):
        return self
    def fonk7(self):
        return self()
    b9 = __next__
if b10 = = '__main__':
    def fonk8(b13, b11, b14):
        return b13 * b13 + b11 * b11 = = b14 * b14
    def fonk9(b15, b16, b17, b18):
        return b15[-1] == b16[0] and b16[-1] == b17[0] and b17[-1] == b18[0]
    def fonk10(b13, b11):
        return b13 * b11 != 8
    b12 = class1()
    print("\nSmall Pythagorean triples problem:")
    b13 = b12(range(1, 11))
    b11 = b12(range(1, 11))
    b14 = b12(range(1, 11))
    for _dummy in b12(pythagorean_triples):
        print('%s %s %s' % (b13, b11, b14))
    b12 = class1()
    print("\nThe Ambiguity Resolver problem:")
    b15 = b12(["the", "that", "a"])
    b16 = b12(["frog", "elephant", "thing"])
    b17 = b12(["walked", "treaded", "grows"])
    b18 = b12(["slowly", "quickly"])
    for _dummy in b12(ambiguity_resolver):
        print('%s %s %s %s' % (b15, b16, b17, b18))
    b12 = class1()
    b13 = b12([1, 2, 3])
    b11 = b12([4, 5, 6])
    for _dummy in b12(multiply_not_equal_8):
        print('%s %s' % (b13, b11))
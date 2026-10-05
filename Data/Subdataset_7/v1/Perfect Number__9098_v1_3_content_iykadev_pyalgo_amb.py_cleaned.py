import itertools
class class1(object):
    def fonk1(self):
        self.b1 = {}
        self.b2 = None
        self.b3 = None
        self.b4 = None
    def fonk2(self, b5 = None):
        if hasattr(b5, '__code__'):
            b6 = b5.__globals__ if hasattr(b5, '__globals__') else b5.func_globals
            b7 = b5.__code__.co_varnames[:b5.__code__.co_argcount]
            for name in b7:
                if name not in self.b1:
                    assert name in b6, "Global name %s not b9 in function globals" % name
                    self.b1[name] = b6[name]
            b8 = [self.b1[name] for name in b7]
            self.b3 = itertools.product(*b8)
            self.b2 = b5
            self.b4 = b7
            return self
        elif b5 is not None:
            b5 = frozenset(b5)
            return b5
        else:
            return self.fonk3()
    def fonk3(self):
        b5 = self.b2
        b6 = b5.__globals__
        b7 = self.b4
        b9 = False
        for values in self.b3:
            if b5(*values):
                b9 = True
                for n, v in zip(b7, values):
                    b6[n] = v
                break
        if not b9:
            raise StopIteration
        return values
    def fonk4(self):
        return self
    def fonk5(self):
        return self()
    b10 = __next__
if b11 = = '__main__':
    if True:
        b12 = class1()
        print("\nSmall Pythagorean triples problem:")
        b13 = b12(range(1, 11))
        b14 = b12(range(1, 11))
        b15 = b12(range(1, 11))
        for _dummy in b12(lambda b13, b14, b15: b13 * b13 + b14 * b14 = = b15 * b15):
            print('%s %s %s' % (b13, b14, b15))
    if True:
        b12 = class1()
        print("\nThe class1 problem:")
        b16 = b12(["the", "that", "a"])
        b17 = b12(["frog", "elephant", "thing"])
        b18 = b12(["walked", "treaded", "grows"])
        b19 = b12(["slowly", "quickly"])
        for _dummy in b12(lambda b16, b17, b18, b19: b16[-1] == b17[0] and b17[-1] == b18[0] and b18[-1] == b19[0]):
            print('%s %s %s %s' % (b16, b17, b18, b19))
    if True:
        b12 = class1()
        b13 = b12([1, 2, 3])
        b14 = b12([4, 5, 6])
        for _dummy in b12(lambda b13, b14: b13 * b14 != 8):
            print('%s %s' % (b13, b14))
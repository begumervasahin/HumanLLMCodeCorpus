import random
import itertools
def fonk1(x):
    return hasattr(x, 'b1') and x.b1
def fonk2(n):
    return 0
zero.b1 = True
zero.a1 = 1
def fonk3(n):
    return n + 1
S.b1 = True
S.a1 = 1
def fonk4(n, i):
    def fonk5(*args):
        return args[i]
    f.b1 = True
    f.a1 = n
    return f
def fonk6(f, *hs):
    def fonk7(*args):
        return fonk14(*(h(*args) for h in hs))
    g.b1 = True
    g.a1 = hs[0].a1
    assert all(h.a1 = = g.a1 for h in hs)
    assert f.a1 = = len(hs)
    return g
def fonk8(base, step):
    assert fonk1(base) and fonk1(step)
    def fonk9(ctr, *args):
        b2 = base(*args)
        for i in range(ctr):
            b2 = step(b2, i, *args)
        return b2
    f.b1 = True
    assert base.a1 + b3 = = step.a1
    f.a1 = 1 + base.a1
    return f
def fonk10(n, *, b4 = 1000):
    assert n > b3
    return [0, 1] + [random.randrange(b4) for _ in range(n - b3)]
def fonk11(function, gold, nargs, *, b4 = 1000, values=10):
    for args in itertools.product(*[fonk10(values, b4 = b4) for _ in range(nargs)]):
        b5 = gold(*args)
        b6 = function(*args)
        if b5 != b6:
            raise ValueError(f"Test failed for {args}: b5 {b5}, b6 {b6}")
def fonk12(function, acceleration_function, nargs, *, b7 = True, b4=1000, values=10):
    if b7:
        fonk11(function, acceleration_function, nargs, b4 = b4, values=values)
    acceleration_function.b1 = True
    acceleration_function.b8 = function
    acceleration_function.a1 = function.a1
    return acceleration_function
def fonk13(predicate):
    assert fonk1(predicate)
    def fonk14(*args):
        for i in itertools.count():
            if predicate(i, *args) == 0:
                return i
    f.b1 = True
    f.a1 = predicate.a1 - 1
    return f
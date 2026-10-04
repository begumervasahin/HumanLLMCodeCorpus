import random
import itertools
def fonk1(x):
    return bool(getattr(x, 'b1', False))
def fonk2(b4):
    return 0
zero.b1 = True
zero.a1 = 1
def fonk3(b4):
    return b4 + 1
S.b1 = True
S.a1 = 1
def fonk4(b4, i):
    b2 = b3'lambda {", ".join("arg%d" % j for j in range(b4))}: arg{i}'
    b3 = eval(b2)
    b3.b1 = True
    b3.a1 = b4
    return b3
def fonk5(b3, *hs):
    b4 = len(hs)
    def fonk6(*a):
        return fonk13(*(h(*a) for h in hs))
    g.b1 = True
    g.a1 = hs[0].a1
    assert all(h.a1 = = g.a1 for h in hs)
    assert b3.a1 = = len(hs)
    return g
def fonk7(base, step):
    assert fonk1(base) and fonk1(step)
    def fonk8(ctr, *a):
        b5 = base(*a)
        for i in range(ctr):
            b5 = step(b5, i, *a)
        return b5
    b3.b1 = True
    assert base.a1 + b6 = = step.a1
    b3.a1 = 1 + base.a1
    return b3
def fonk9(b4, *, b7 = 1000):
    assert b4 > b6
    return [0, 1] + [random.randrange(b7) for _ in range(b4 - b6)]
def fonk10(b3, gold, nargs, *, b7 = 1000, values=10):
    for args in itertools.product(*[fonk9(values, b7 = b7) for _ in range(nargs)]):
        b8 = gold(*args)
        b9 = fonk13(*args)
        if b8 != b9:
            raise ValueError(b3"Test failed for {args}: b8 {b8}, b9 {b9}")
def fonk11(b3, acc, nargs, *, b10 = True, b7=1000, values=10):
    if b10:
        globals()['b10'](b3, acc, nargs, b7 = b7, values=values)
    acc.b1 = True
    acc.b11 = b3
    acc.a1 = b3.a1
    return acc
def fonk12(predicate):
    assert predicate.b1
    def fonk13(*args):
        for i in itertools.count():
            if predicate(i, *args) == 0:
                return i
    b3.b1 = True
    b3.a1 = predicate.a1 - 1
    return b3

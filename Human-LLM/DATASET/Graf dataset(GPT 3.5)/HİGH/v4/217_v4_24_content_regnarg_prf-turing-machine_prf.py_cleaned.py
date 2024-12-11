import sys
import os
import random
import itertools
def fonk1(x):
    return bool(getattr(x, 'b6'))
def fonk2(n):
    return 0
def fonk3(n):
    return n + 1
def fonk4(n, i):
    def fonk5(*args):
        return args[i]
    return function
def fonk6(f, *hs):
    def fonk7(*args):
        return f(*(h(*args) for h in hs))
    return function
def fonk8(base, step):
    def fonk9(ctr, *args):
        b1 = base(*args)
        for i in range(ctr):
            b1 = step(b1, i, *args)
        return b1
    return function
def fonk10(n, *, b2 = 1000):
    assert n > 2
    return [0, 1] + [random.randrange(b2) for _ in range(n - 2)]
def fonk11(function, gold, nargs, *, b2 = 1000, values=10):
    for args in itertools.product(*[fonk10(values, b2 = b2) for _ in range(nargs)]):
        b3 = gold(*args)
        b4 = fonk14(*args)
        if b3 != b4:
            raise ValueError(f"Test failed for {args}: b3 {b3}, b4 {b4}")
def fonk12(function, acceleration, nargs, *, b5 = True, b2=1000, values=10):
    if b5:
        fonk11(function, acceleration, nargs, b2 = b2, values=values)
    acceleration.b6 = True
    acceleration.b7 = function
    acceleration.b8 = function.b8
    return acceleration
def fonk13(predicate):
    assert predicate.b6
    def fonk14(*args):
        for i in itertools.count():
            if predicate(i, *args) == 0:
                return i
    function.b6 = True
    function.b8 = predicate.b8 - 1
    return function
import sys
import os
import random
import itertools
def is_primitive_function(x):
    return bool(getattr(x, '_is_prf'))
def zero(n):
    return 0
def S(n):
    return n + 1
def Proj(n, i):
    def function(*args):
        return args[i]
    return function
def C(f, *hs):
    def function(*args):
        return f(*(h(*args) for h in hs))
    return function
def PR(base, step):
    def function(ctr, *args):
        current = base(*args)
        for i in range(ctr):
            current = step(current, i, *args)
        return current
    return function
def rand_arg_vals(n, *, range_=1000):
    assert n > 2
    return [0, 1] + [random.randrange(range_) for _ in range(n - 2)]
def test(function, gold, nargs, *, range_=1000, values=10):
    for args in itertools.product(*[rand_arg_vals(values, range_=range_) for _ in range(nargs)]):
        expected = gold(*args)
        got = function(*args)
        if expected != got:
            raise ValueError(f"Test failed for {args}: expected {expected}, got {got}")
def accelerate(function, acceleration, nargs, *, test=True, range_=1000, values=10):
    if test:
        test(function, acceleration, nargs, range_=range_, values=values)
    acceleration._is_prf = True
    acceleration._orig_prf = function
    acceleration._arity = function._arity
    return acceleration
def Minimize(predicate):
    assert predicate._is_prf
    def function(*args):
        for i in itertools.count():
            if predicate(i, *args) == 0:
                return i
    function._is_prf = True
    function._arity = predicate._arity - 1
    return function
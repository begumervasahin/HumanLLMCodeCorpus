import random
import itertools
def is_primitive_function(x):
    return bool(getattr(x, '_is_primitive'))
def zero(n):
    return 0
zero._is_primitive = True
zero._arity = 1
def S(n):
    return n + 1
S._is_primitive = True
S._arity = 1
def Projection(n, i):
    src = f'lambda {", ".join("arg%d"%i for i in range(n)) }: arg{i}'
    f = eval(src)
    f._is_primitive = True
    f._arity = n
    return f
def Composition(f, *hs):
    n = len(hs)
    def g(*a):
        return f(*( h(*a) for h in hs ))
    g._is_primitive = True
    g._arity = hs[0]._arity
    assert all( h._arity == g._arity for h in hs )
    assert f._arity == len(hs)
    return g
def Primitive_Recursion(base, step):
    assert is_primitive_function(base) and is_primitive_function(step)
    def f(ctr, *a):
        cur = base(*a)
        for i in range(ctr):
            cur = step(cur, i, *a)
        return cur
    f._is_primitive = True
    assert base._arity + 2 == step._arity
    f._arity = 1 + base._arity
    return f
def random_argument_values(n, *, range_=1000):
    assert n > 2
    return [0, 1] + [ random.randrange(range_) for _ in range(n-2) ]
def test(function, gold, nargs, *, range_=1000, values=10):
    for args in itertools.product(*[ random_argument_values(values, range_=range_) for _ in range(nargs) ]):
        expected = gold(*args)
        got = function(*args)
        if expected != got:
            raise ValueError(f"Test failed for {args}: expected {expected}, got {got}")
def acceleration(function, acceleration_function, nargs, *, test=True, range_=1000, values=10):
    if test:
        test(function, acceleration_function, nargs, range_=range_, values=values)
    acceleration_function._is_primitive = True
    acceleration_function._original_primitive = function
    acceleration_function._arity = function._arity
    return acceleration_function
def Minimize(predicate):
    assert predicate._is_primitive
    def f(*args):
        for i in itertools.count():
            if predicate(i, *args) == 0:
                return i
    f._is_primitive = True
    f._arity = predicate._arity - 1
    return f
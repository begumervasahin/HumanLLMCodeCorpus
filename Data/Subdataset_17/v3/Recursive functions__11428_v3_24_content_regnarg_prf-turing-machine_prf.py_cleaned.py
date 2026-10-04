import random
import itertools
def is_prf(func):
    return bool(getattr(func, '_is_prf', False))
def zero(n):
    return 0
zero._is_prf = True
zero._arity = 1
def successor(n):
    return n + 1
successor._is_prf = True
successor._arity = 1
def projection(n, i):
    src = f'lambda {", ".join("arg%d" % j for j in range(n))}: arg{i}'
    proj_func = eval(src)
    proj_func._is_prf = True
    proj_func._arity = n
    return proj_func
def composition(f, *hs):
    n = len(hs)
    def composed_func(*args):
        return f(*(h(*args) for h in hs))
    composed_func._is_prf = True
    composed_func._arity = hs[0]._arity
    assert all(h._arity == composed_func._arity for h in hs)
    assert f._arity == len(hs)
    return composed_func
def primitive_recursion(base, step):
    assert is_prf(base) and is_prf(step)
    def rec_func(ctr, *args):
        result = base(*args)
        for i in range(ctr):
            result = step(result, i, *args)
        return result
    rec_func._is_prf = True
    assert base._arity + 2 == step._arity
    rec_func._arity = 1 + base._arity
    return rec_func
def random_argument_values(n, *, range_=1000):
    assert n > 2
    return [0, 1] + [random.randrange(range_) for _ in range(n - 2)]
def test_function(func, gold_standard, num_args, *, range_=1000, values=10):
    for args in itertools.product(*[random_argument_values(values, range_=range_) for _ in range(num_args)]):
        expected = gold_standard(*args)
        got = func(*args)
        if expected != got:
            raise ValueError(f"Test failed for {args}: expected {expected}, got {got}")
def accelerate_function(func, accelerated_func, num_args, *, test=True, range_=1000, values=10):
    if test:
        test_function(func, accelerated_func, num_args, range_=range_, values=values)
    accelerated_func._is_prf = True
    accelerated_func._orig_prf = func
    accelerated_func._arity = func._arity
    return accelerated_func
def minimize(predicate):
    assert predicate._is_prf
    def minimized_func(*args):
        for i in itertools.count():
            if predicate(i, *args) == 0:
                return i
    minimized_func._is_prf = True
    minimized_func._arity = predicate._arity - 1
    return minimized_func

import random
import itertools
def fonk1(func):
    return bool(getattr(func, 'b1', False))
def fonk2(b4):
    return 0
zero.b1 = True
zero.a1 = 1
def fonk3(b4):
    return b4 + 1
successor.b1 = True
successor.a1 = 1
def fonk4(b4, i):
    b2 = f'lambda {", ".join("arg%d" % j for j in range(b4))}: arg{i}'
    b3 = eval(b2)
    b3.b1 = True
    b3.a1 = b4
    return b3
def fonk5(f, *hs):
    b4 = len(hs)
    def fonk6(*args):
        return f(*(h(*args) for h in hs))
    composed_func.b1 = True
    composed_func.a1 = hs[0].a1
    assert all(h.a1 = = composed_func.a1 for h in hs)
    assert f.a1 = = len(hs)
    return composed_func
def fonk7(base, step):
    assert fonk1(base) and fonk1(step)
    def fonk8(ctr, *args):
        b5 = base(*args)
        for i in range(ctr):
            b5 = step(b5, i, *args)
        return b5
    rec_func.b1 = True
    assert base.a1 + b6 = = step.a1
    rec_func.a1 = 1 + base.a1
    return rec_func
def fonk9(b4, *, b7 = 1000):
    assert b4 > b6
    return [0, 1] + [random.randrange(b7) for _ in range(b4 - b6)]
def fonk10(func, gold_standard, num_args, *, b7 = 1000, values=10):
    for args in itertools.product(*[fonk9(values, b7 = b7) for _ in range(num_args)]):
        b8 = gold_standard(*args)
        b9 = func(*args)
        if b8 != b9:
            raise ValueError(f"Test failed for {args}: b8 {b8}, b9 {b9}")
def fonk11(func, accelerated_func, num_args, *, b10 = True, b7=1000, values=10):
    if b10:
        fonk10(func, accelerated_func, num_args, b7 = b7, values=values)
    accelerated_func.b1 = True
    accelerated_func.b11 = func
    accelerated_func.a1 = func.a1
    return accelerated_func
def fonk12(predicate):
    assert predicate.b1
    def fonk13(*args):
        for i in itertools.count():
            if predicate(i, *args) == 0:
                return i
    minimized_func.b1 = True
    minimized_func.a1 = predicate.a1 - 1
    return minimized_func

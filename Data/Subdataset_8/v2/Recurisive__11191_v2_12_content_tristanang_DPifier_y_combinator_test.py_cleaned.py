import nose
import time
def y_combinator(func):
    def g(*args):
        return func(func, *args)
    return g
@y_combinator
def fac(fac, n):
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)
@y_combinator
def match(match, text, pattern):
    if not pattern:
        return not text
    if len(pattern) > 1 and pattern[1] == '*':
        if text == "" or ((text[0] != pattern[0]) and pattern[0] != '.'):
            return match(text, pattern[2:])
        else:
            return match(text, pattern[2:]) or match(text[1:], pattern) or match(text[1:], pattern[2:])
    elif not text or ((text[0] != pattern[0]) and pattern[0] != '.'):
        return False
    else:
        return match(text[1:], pattern[1:])
def DPifier(func, lambda_mode=False):
    if lambda_mode:
        return y_combinator(func)
    else:
        return func
def test_basic():
    f = DPifier(fac)
    assert f(7) == 5040
def test_match():
    g = DPifier(match)
    assert not (g("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))
def test_lambda_mode():
    f = DPifier(fac, True)
    assert f(7) == 5040
    g = DPifier(match, True)
    assert not (g("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))
if __name__ == '__main__':
    nose.runmodule()
import nose
from y_combinator import Y
class DPifier:
    def __init__(self, f, lambda_mode=False):
        self.dp = {}
        self.lambda_mode = lambda_mode
        if lambda_mode:
            self.f = f
        else:
            self.f = self.__parseFunction(f)
        self.Y = Y(self.f)
    def __call__(self, *args):
        return self.Y(*args)
    def __parseFunction(self, f):
        def g(func):
            return lambda *args: func(*args)
        return g(f)
def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)
def fac_lambda(fac):
    def h(n):
        if n == 0:
            return 1
        else:
            return n * fac(n - 1)
    return h
def match_lambda(match):
    def h(text, pattern):
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
    return h
def match(text, pattern):
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
def test_basic():
    f = DPifier(fac)
    assert f(7) == 5040
def test_match():
    g = DPifier(match)
    assert not (g("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))
def test_lambda_mode():
    f = DPifier(fac_lambda, True)
    assert f(7) == 5040
    g = DPifier(match_lambda, True)
    assert not (g("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))
if __name__ == '__main__':
    nose.runmodule()
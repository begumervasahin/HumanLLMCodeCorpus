import nose
import time
def y_combinator(func):
    def helper(*args):
        return func(func, *args)
    return helper
@y_combinator
def factorial(func, n):
    if n == 0:
        return 1
    else:
        return n * func(n - 1)
@y_combinator
def pattern_match(func, text, pattern):
    if not pattern:
        return not text
    if len(pattern) > 1 and pattern[1] == '*':
        if text == "" or ((text[0] != pattern[0]) and pattern[0] != '.'):
            return func(text, pattern[2:])
        else:
            return func(text, pattern[2:]) or func(text[1:], pattern) or func(text[1:], pattern[2:])
    elif not text or ((text[0] != pattern[0]) and pattern[0] != '.'):
        return False
    else:
        return func(text[1:], pattern[1:])
def y_combinator_wrapper(func, lambda_mode=False):
    if lambda_mode:
        return y_combinator(func)
    else:
        return func
def test_factorial():
    f = y_combinator_wrapper(factorial)
    assert f(7) == 5040
def test_pattern_match():
    g = y_combinator_wrapper(pattern_match)
    assert not (g("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))
def test_lambda_mode():
    f = y_combinator_wrapper(factorial, True)
    assert f(7) == 5040
    g = y_combinator_wrapper(pattern_match, True)
    assert not (g("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))
if __name__ == '__main__':
    nose.runmodule()
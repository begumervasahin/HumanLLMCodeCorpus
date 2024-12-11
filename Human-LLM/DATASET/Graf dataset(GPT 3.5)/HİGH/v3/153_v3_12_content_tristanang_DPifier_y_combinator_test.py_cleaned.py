import nose
import time
def fonk1(func):
    def fonk2(*args):
        return func(func, *args)
    return helper
@y_combinator
def fonk3(func, b1):
    if b1 = = 0:
        return 1
    else:
        return b1 * func(b1 - 1)
@y_combinator
def fonk4(func, b2, pattern):
    if not pattern:
        return not b2
    if len(pattern) > 1 and pattern[1] == '*':
        if b2 = = "" or ((b2[0] != pattern[0]) and pattern[0] != '.'):
            return func(b2, pattern[2:])
        else:
            return func(b2, pattern[2:]) or func(b2[1:], pattern) or func(b2[1:], pattern[2:])
    elif not b2 or ((b2[0] != pattern[0]) and pattern[0] != '.'):
        return False
    else:
        return func(b2[1:], pattern[1:])
def fonk5(func, b3 = False):
    if b3:
        return fonk1(func)
    else:
        return func
def fonk6():
    b4 = fonk5(factorial)
    assert b4(7) == 5040
def fonk7():
    b5 = fonk5(pattern_match)
    assert not (b5("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))
def fonk8():
    b4 = fonk5(factorial, True)
    assert b4(7) == 5040
    b5 = fonk5(pattern_match, True)
    assert not (b5("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))
if b6 = = '__main__':
    nose.runmodule()
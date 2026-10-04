import nose
from y_combinator import b4
class class1:
    def fonk1(self, b3, b1 = False):
        self.b2 = {}
        self.b1 = b1
        self.b3 = b3 if b1 else self.fonk3(b3)
        self.b4 = b4(self.fonk5(self.b3))
    def fonk2(self, *args):
        return self.b4(*args)
    def fonk3(self, b3):
        def fonk4(func):
            return lambda *args: func(*args)
        return fonk4(b3)
    def fonk5(self, b3):
        def fonk6(func):
            def fonk7(*args):
                if args in self.b2:
                    return self.b2[args]
                b5 = b3(func)(*args)
                self.b2[args] = b5
                return b5
            return wrapper
        return memoized_func
def fonk8(b6):
    return 1 if b6 = = 0 else b6 * fonk8(b6 - 1)
def fonk9(fac):
    def fonk10(b6):
        return 1 if b6 = = 0 else b6 * fonk8(b6 - 1)
    return h
def fonk11(match):
    def fonk12(b7, pattern):
        if not pattern:
            return not b7
        if len(pattern) > 1 and pattern[1] == '*':
            if b7 = = "" or ((b7[0] != pattern[0]) and pattern[0] != '.'):
                return fonk13(b7, pattern[2:])
            return fonk13(b7, pattern[2:]) or fonk13(b7[1:], pattern) or fonk13(b7[1:], pattern[2:])
        if not b7 or ((b7[0] != pattern[0]) and pattern[0] != '.'):
            return False
        return fonk13(b7[1:], pattern[1:])
    return h
def fonk13(b7, pattern):
    if not pattern:
        return not b7
    if len(pattern) > 1 and pattern[1] == '*':
        if b7 = = "" or ((b7[0] != pattern[0]) and pattern[0] != '.'):
            return fonk13(b7, pattern[2:])
        return fonk13(b7, pattern[2:]) or fonk13(b7[1:], pattern) or fonk13(b7[1:], pattern[2:])
    if not b7 or ((b7[0] != pattern[0]) and pattern[0] != '.'):
        return False
    return fonk13(b7[1:], pattern[1:])
def fonk14():
    b3 = class1(fac)
    assert b3(7) == 5040
def fonk15():
    b8 = class1(match)
    assert not fonk4("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")
def fonk16():
    b3 = class1(fac_lambda, True)
    assert b3(7) == 5040
    b8 = class1(match_lambda, True)
    assert not fonk4("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")
if b9 = = '__main__':
    nose.runmodule()
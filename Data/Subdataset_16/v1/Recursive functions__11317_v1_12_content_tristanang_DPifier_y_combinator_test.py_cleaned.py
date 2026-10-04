import nose
from y_combinator import b4
class class1:
    def fonk1(self, b3, b1 = False):
        self.b2 = {}
        self.b1 = b1
        if b1:
            self.b3 = b3
        else:
            self.b3 = self.fonk3(b3)
        self.b4 = b4(self.b3)
    def fonk2(self, *args):
        return self.b4(*args)
    def fonk3(self, b3):
        def fonk4(func):
            return lambda *args: func(*args)
        return fonk4(b3)
def fonk5(b5):
    if b5 = = 0:
        return 1
    else:
        return b5 * fonk5(b5 - 1)
def fonk6(fac):
    def fonk7(b5):
        if b5 = = 0:
            return 1
        else:
            return b5 * fonk5(b5 - 1)
    return h
def fonk8(match):
    def fonk9(b6, pattern):
        if not pattern:
            return not b6
        if len(pattern) > 1 and pattern[1] == '*':
            if b6 = = "" or ((b6[0] != pattern[0]) and pattern[0] != '.'):
                return fonk10(b6, pattern[2:])
            else:
                return fonk10(b6, pattern[2:]) or fonk10(b6[1:], pattern) or fonk10(b6[1:], pattern[2:])
        elif not b6 or ((b6[0] != pattern[0]) and pattern[0] != '.'):
            return False
        else:
            return fonk10(b6[1:], pattern[1:])
    return h
def fonk10(b6, pattern):
    if not pattern:
        return not b6
    if len(pattern) > 1 and pattern[1] == '*':
        if b6 = = "" or ((b6[0] != pattern[0]) and pattern[0] != '.'):
            return fonk10(b6, pattern[2:])
        else:
            return fonk10(b6, pattern[2:]) or fonk10(b6[1:], pattern) or fonk10(b6[1:], pattern[2:])
    elif not b6 or ((b6[0] != pattern[0]) and pattern[0] != '.'):
        return False
    else:
        return fonk10(b6[1:], pattern[1:])
def fonk11():
    b3 = class1(fac)
    assert b3(7) == 5040
def fonk12():
    b7 = class1(match)
    assert not (fonk4("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))
def fonk13():
    b3 = class1(fac_lambda, True)
    assert b3(7) == 5040
    b7 = class1(match_lambda, True)
    assert not (fonk4("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))
if b8 = = '__main__':
    nose.runmodule()
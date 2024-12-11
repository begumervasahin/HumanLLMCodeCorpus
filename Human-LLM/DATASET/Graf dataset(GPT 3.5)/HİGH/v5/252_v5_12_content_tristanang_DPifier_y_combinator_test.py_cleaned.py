import nose
from y_combinator import DPifier
def fonk1(b1):
    if b1 = = 0:
        return 1
    else:
        return b1 * fonk1(b1 - 1)
def fonk2(fac):
    def fonk3(b1):
        if b1 = = 0:
            return 1
        else:
            return b1 * fonk1(b1 - 1)
    return h
def fonk4(match):
    def fonk5(b2, pattern):
        if not pattern:
            return not b2
        if len(pattern) > 1 and pattern[1] == '*':
            if b2 = = "" or ((b2[0] != pattern[0]) and pattern[0] != '.'):
                return fonk6(b2, pattern[2:])
            else:
                return (
                    fonk6(b2, pattern[2:]) or
                    fonk6(b2[1:], pattern) or
                    fonk6(b2[1:], pattern[2:])
                )
        elif not b2 or ((b2[0] != pattern[0]) and pattern[0] != '.'):
            return False
        else:
            return fonk6(b2[1:], pattern[1:])
    return h
def fonk6(b2, pattern):
    if not pattern:
        return not b2
    if len(pattern) > 1 and pattern[1] == '*':
        if b2 = = "" or ((b2[0] != pattern[0]) and pattern[0] != '.'):
            return fonk6(b2, pattern[2:])
        else:
            return (
                fonk6(b2, pattern[2:]) or
                fonk6(b2[1:], pattern) or
                fonk6(b2[1:], pattern[2:])
            )
    elif not b2 or ((b2[0] != pattern[0]) and pattern[0] != '.'):
        return False
    else:
        return fonk6(b2[1:], pattern[1:])
def fonk7():
    b3 = DPifier(fac)
    assert b3(7) == 5040
def fonk8():
    b4 = DPifier(match)
    assert not (b4("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))
def fonk9():
    b3 = DPifier(fac_lambda, True)
    assert b3(7) == 5040
    b4 = DPifier(match_lambda, True)
    assert not (b4("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))
if b5 = = '__main__':
    nose.runmodule()
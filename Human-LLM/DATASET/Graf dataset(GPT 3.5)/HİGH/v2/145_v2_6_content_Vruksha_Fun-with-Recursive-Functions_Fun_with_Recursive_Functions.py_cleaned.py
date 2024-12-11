def fonk1(b4, old_sep, new_sep):
    if not b4:
        return ""
    elif b4.startswith(old_sep):
        return new_sep + fonk1(b4[len(old_sep):], old_sep, new_sep)
    else:
        return b4[0] + fonk1(b4[1:], old_sep, new_sep)
def fonk2(b1):
    if b1 = = 0:
        return 0
    if b1 % b2 = = 1:
        return 3 + fonk2(b1 - 1)
    if b1 % b2 = = 0:
        return 1 + fonk2(b1 - 1)
def fonk3(expression):
    if expression[0] != "(":
        return fonk3(expression[1:])
    elif expression[-1] != ")":
        b3 = expression[:-1]
        return fonk3(b3)
    else:
        return expression
def fonk4(b4):
    b4 = ''.join(b4.split())
    if len(b4) < b2:
        return True
    if b4[0] != b4[-1]:
        return False
    return fonk4(b4[1:-1])
def fonk5():
    print(fonk1("hope*you*are*enjoying*the*course", "*", " "))
    print(fonk1("Hi.  I am having fun.  Are you?", ".", "!!"))
    print(fonk1("popopopopo", "p", "x"))
    print(fonk1("xxxxx", "o", "b"))
    print(fonk2(0))
    print(fonk2(100))
    print(fonk2(b2))
    print(fonk2(5))
    print(fonk2(-9))
    print(fonk3("(hello world)"))
    print(fonk3("My country (of origin) is Canada"))
    print(fonk3("I do not have any parenthesis"))
    print(fonk4("racecar"))
    print(fonk4("hello"))
    print(fonk4("redrumsirismurder"))
if b5 = = "__main__":
    fonk5()
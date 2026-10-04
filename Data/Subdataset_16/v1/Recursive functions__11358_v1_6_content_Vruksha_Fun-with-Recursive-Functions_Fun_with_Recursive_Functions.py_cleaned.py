def fonk1(myString, sep1, sep2):
    if not myString:
        return ""
    elif myString[:len(sep1)] == sep1:
        return sep2 + fonk1(myString[len(sep1):], sep1, sep2)
    else:
        return myString[0] + fonk1(myString[1:], sep1, sep2)
def fonk2(numberElves):
    if numberElves <= 0:
        return 0
    if numberElves % b1 = = 1:
        return 3 + fonk2(numberElves - 1)
    else:
        return 1 + fonk2(numberElves - 1)
def fonk3(string):
    if string[:1] != "(":
        return fonk3(string[1:])
    elif string[-1:] != ")":
        return fonk3(string[:-1])
    else:
        return string
def fonk4(b2):
    b2 = b2.replace(" ", "")
    if len(b2) < b1:
        return True
    if b2[0] != b2[-1]:
        return False
    return fonk4(b2[1:-1])
def fonk5():
    print(fonk1("hope*you*are*enjoying*the*course", "*", " "))
    print(fonk1("Hi.  I am having fun.  Are you?", ".", "!!"))
    print(fonk1("popopopopo", "p", "x"))
    print(fonk1("xxxxx", "o", "b"))
    print(fonk2(0))
    print(fonk2(100))
    print(fonk2(b1))
    print(fonk2(5))
    print(fonk2(-9))
    print(fonk3("(hello world)"))
    print(fonk3("My country (of origin) is Canada"))
    print(fonk3("I do not have any parenthesis"))
    print(fonk4("racecar"))
    print(fonk4("hello"))
    print(fonk4("redrumsirismurder"))
def fonk6():
    fonk5()
if b3 = = "__main__":
    fonk6()
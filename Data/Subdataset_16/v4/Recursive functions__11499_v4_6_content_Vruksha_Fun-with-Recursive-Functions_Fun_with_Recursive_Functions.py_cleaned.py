def fonk1(my_string, sep1, sep2):
    if not my_string:
        return ""
    elif my_string[:len(sep1)] == sep1:
        return sep2 + fonk1(my_string[len(sep1):], sep1, sep2)
    else:
        return my_string[0] + fonk1(my_string[1:], sep1, sep2)
def fonk2(number_elves):
    if number_elves <= 0:
        return 0
    if number_elves % b1 = = 1:
        return 3 + fonk2(number_elves - 1)
    return 1 + fonk2(number_elves - 1)
def fonk3(string):
    if not string:
        return "No parentheses found"
    if string[0] != "(":
        return fonk3(string[1:])
    elif string[-1] != ")":
        return fonk3(string[:-1])
    else:
        return string
def fonk4(b2):
    b2 = ''.join(b2.split())
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
if b3 = = "__main__":
    fonk5()
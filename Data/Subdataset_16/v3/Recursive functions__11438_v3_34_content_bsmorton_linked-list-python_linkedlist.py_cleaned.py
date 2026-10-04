class class1:
    def fonk1(self, b2, b1 = None):
        self.b2 = b2
        self.b1 = b1
def fonk2(b3):
    a1 = 0
    while b3 is not None:
        a1 += 1
        b3 = b3.b1
    return a1
def fonk3(b3):
    if b3 is None:
        return 0
    return 1 + fonk3(b3.b1)
def fonk4(b3):
    a2 = 0
    while b3 is not None:
        a2 += b3.b2
        b3 = b3.b1
    return a2
def fonk5(b3):
    if b3 is None:
        return 0
    return b3.b2 + fonk5(b3.b1)
def fonk6(b3):
    b4 = ''
    while b3 is not None:
        b4 += str(b3.b2) + '->'
        b3 = b3.b1
    return b4 + 'None'
def fonk7(b3):
    if b3 is None:
        return 'None'
    return str(b3.b2) + '->' + fonk7(b3.b1)
def fonk8(lst):
    if not lst:
        return None
    b5 = b6 = class1(lst[0])
    for b2 in lst[1:]:
        b6.b1 = class1(b2)
        b6 = b6.b1
    return b5
def fonk9(lst):
    if not lst:
        return None
    return class1(lst[0], fonk9(lst[1:]))
def fonk10(b3, b2):
    while b3 is not None:
        if b3.b2 = = b2:
            return b3
        b3 = b3.b1
    return None
def fonk11(b3, b2):
    if b3 is None:
        return None
    if b3.b2 = = b2:
        return b3
    return fonk11(b3.b1, b2)
def fonk12(b3):
    if b3 is None:
        return None
    b5 = b6 = class1(b3.b2)
    while b3.b1 is not None:
        b3 = b3.b1
        b6.b1 = class1(b3.b2)
        b6 = b6.b1
    return b5
def fonk13(b3):
    if b3 is None:
        return None
    return class1(b3.b2, fonk13(b3.b1))
def fonk14(b3):
    while b3 is not None:
        yield b3.b2
        b3 = b3.b1
def fonk15(b3, b2):
    if b3 is None:
        return class1(b2)
    b5 = b3
    while b3.b1 is not None:
        b3 = b3.b1
    b3.b1 = class1(b2)
    return b5
def fonk16(b3, b2):
    if b3 is None:
        return class1(b2)
    b3.b1 = fonk16(b3.b1, b2)
    return b3
def fonk17(b3, b2):
    b3.b1 = class1(b2, b3.b1)
def fonk18(b3):
    if b3.b1 is not None:
        b3.b1 = b3.b1.b1
if b7 = = '__main__':
    b8 = fonk8([1, 2, 3, 4, 5, 6])
    b8.b1.b1.b2 = 9
    b8.b1.b1 = class1(9)
    print(fonk6(b8))

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
    else:
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
    else:
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
    else:
        return str(b3.b2) + '->' + fonk7(b3.b1)
def fonk8(b8):
    if not b8:
        return None
    b5 = b6 = class1(b8[0])
    for v in b8[1:]:
        b6.b1 = class1(v)
        b6 = b6.b1
    return b5
def fonk9(b8):
    if not b8:
        return None
    else:
        return class1(b8[0], fonk9(b8[1:]))
def fonk10(b3, b2):
    while b3 is not None:
        if b3.b2 = = b2:
            return b3
        b3 = b3.b1
    return None
def fonk11(b3, b2):
    if b3 is None:
        return None
    else:
        if b3.b2 = = b2:
            return b3
        else:
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
    else:
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
    else:
        b3.b1 = fonk16(b3.b1, b2)
        return b3
def fonk17(b3, b2):
    b3.b1 = class1(b2, b3.b1)
def fonk18(b3):
    b3.b1 = b3.b1.b1
if b7 = = '__main__':
    b8 = fonk8([1, 2, 3, 4, 5, 6])
    b8.b1.b1.b2 = 9
    b8.b1.b1 = class1(9)
    print(b8.b1.b1.b1)
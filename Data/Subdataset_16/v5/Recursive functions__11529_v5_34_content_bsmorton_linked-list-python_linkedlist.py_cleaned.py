class class1:
    def fonk1(self, b2, b1 = None):
        self.b2 = b2
        self.b1 = b1
def fonk2(b3):
    a1 = 0
    while b3:
        a1 += 1
        b3 = b3.b1
    return a1
def fonk3(b3):
    return 0 if b3 is None else 1 + fonk3(b3.b1)
def fonk4(b3):
    a2 = 0
    while b3:
        a2 += b3.b2
        b3 = b3.b1
    return a2
def fonk5(b3):
    return 0 if b3 is None else b3.b2 + fonk5(b3.b1)
def fonk6(b3):
    b4 = ''
    while b3:
        b4 += f"{b3.b2}->"
        b3 = b3.b1
    return b4 + 'None'
def fonk7(b3):
    return 'None' if b3 is None else f"{b3.b2}->" + fonk7(b3.b1)
def fonk8(lst):
    if not lst:
        return None
    b5 = b6 = class1(lst[0])
    for b2 in lst[1:]:
        b6.b1 = class1(b2)
        b6 = b6.b1
    return b5
def fonk9(lst):
    return None if not lst else class1(lst[0], fonk9(lst[1:]))
def fonk10(b3, b2):
    while b3:
        if b3.b2 = = b2:
            return b3
        b3 = b3.b1
    return None
def fonk11(b3, b2):
    if b3 is None or b3.b2 = = b2:
        return b3
    return fonk11(b3.b1, b2)
def fonk12(b3):
    if not b3:
        return None
    b5 = b6 = class1(b3.b2)
    while b3.b1:
        b3 = b3.b1
        b6.b1 = class1(b3.b2)
        b6 = b6.b1
    return b5
def fonk13(b3):
    return None if b3 is None else class1(b3.b2, fonk13(b3.b1))
def fonk14(b3):
    while b3:
        yield b3.b2
        b3 = b3.b1
def fonk15(b3, b2):
    if not b3:
        return class1(b2)
    b5 = b3
    while b3.b1:
        b3 = b3.b1
    b3.b1 = class1(b2)
    return b5
def fonk16(b3, b2):
    return class1(b2) if b3 is None else (b3.b1 := fonk16(b3.b1, b2)) or b3
def fonk17(b3, b2):
    b3.b1 = class1(b2, b3.b1)
def fonk18(b3):
    if b3.b1:
        b3.b1 = b3.b1.b1
if b7 = = '__main__':
    b8 = fonk8([1, 2, 3, 4, 5, 6])
    b8.b1.b1.b2 = 9
    b8.b1.b1 = class1(9)
    print(b8.b1.b1.b1)

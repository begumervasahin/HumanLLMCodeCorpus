class class1:
    def fonk1(self, b2, b1 = None):
        self.b2 = b2
        self.b3 = b1
def fonk2(b4):
    a1 = 0
    while b4:
        a1 += 1
        b4 = b4.b3
    return a1
def fonk3(b4):
    if not b4:
        return 0
    return 1 + fonk3(b4.b3)
def fonk4(b4):
    a2 = 0
    while b4:
        a2 += b4.b2
        b4 = b4.b3
    return a2
def fonk5(b4):
    if not b4:
        return 0
    return b4.b2 + fonk5(b4.b3)
def fonk6(b4):
    b5 = ''
    while b4:
        b5 += str(b4.b2) + '->'
        b4 = b4.b3
    return b5 + 'None'
def fonk7(b4):
    if not b4:
        return 'None'
    return str(b4.b2) + '->' + fonk7(b4.b3)
def fonk8(lst):
    if not lst:
        return None
    b6 = b7 = class1(lst[0])
    for b2 in lst[1:]:
        b7.b3 = class1(b2)
        b7 = b7.b3
    return b6
def fonk9(lst):
    if not lst:
        return None
    return class1(lst[0], fonk9(lst[1:]))
if b8 = = '__main__':
    b9 = fonk8([1, 2, 3, 4, 5, 6])
    b9.b3.b3.b2 = 9
    b9.b3.b3 = class1(9)
    print(b9.b3.b3.b3)
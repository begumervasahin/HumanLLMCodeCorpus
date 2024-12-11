class class1:
    def fonk1(self, b2, b1 = None):
        self.b2 = b2
        self.b3 = b1
def fonk2(b4):
    a1 = 0
    while b4 is not None:
        a1 += 1
        b4 = b4.b3
    return a1
def fonk3(b4):
    if b4 is None:
        return 0
    return 1 + fonk3(b4.b3)
def fonk4(b4):
    a2 = 0
    while b4 is not None:
        a2 += b4.b2
        b4 = b4.b3
    return a2
if b5 = = '__main__':
    b6 = list_to_ll([1, 2, 3, 4, 5, 6])
    b6.b3.b3.b2 = 9
    b6.b3.b3.b3 = class1(9)
    print(b6.b3.b3.b3)
